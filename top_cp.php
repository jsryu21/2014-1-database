<html>
<head>
	<title>Top Player!</title>
	<meta http-equiv="Content-Type" content="text/html" charset="utf-8">
</head>
<body>
<?php
$con = mysql_connect('localhost','root','asdf1234') or die('Could not connect: '.mysql_Error()."</br>");
mysql_query("set names utf8");
mysql_select_db('dbproject');

$engToKor=array(
	'name'	=>	'이름',
// BATTER stat
	'avg'	=>	'타율',
	'g'	=>	'경기',
	'pa'	=>	'타석',
	'ab'	=>	'타수',
	'r'	=>	'득점',
	'hit'	=>	'안타',
	'2b'	=>	'2루타',
	'3b'	=>	'3루타',
	'hr'	=>	'홈런',
	'tb'	=>	'루타',
	'pbi'	=>	'타점',
	'sb'	=>	'도루',
	'cs'	=>	'도루실패',
	'sac'	=>	'희타',
	'sf'	=>	'희비',
	'bb'	=>	'피볼넷',
	'ibb'	=>	'피고의4구',
	'hbp'	=>	'피사구',
	'so'	=>	'피삼진',
	'gdp'	=>	'병살',
	'slg'	=>	'장타율',
	'obp'	=>	'출루율',
	'err'	=>	'실책',
	'sr'	=>	'도루 성공율',
	'bbk'	=>	'피볼넷/피삼진',
	'slgr'	=>	'장타/안타',
	'mh'	=>	'멀티히트',
	'ops'	=>	'OPS',
	'savg'	=>	'득점권 타율',
	'pavg'	=>	'대타 타율',
	'isop'	=>	'순수장타율',
	'isod'	=>	'순수출루율',
	'1b'	=>	'1루타',
	'BatterFP'=>	'타자포에버포인트',

// PITCHER stat
	'era'	=>	'평균자책점',
	'sho'	=>	'완투',
	'cg'	=>	'완봉',
	'w'	=>	'승',
	'l'	=>	'패',
	'sv'	=>	'세',
	'hld'	=>	'홀',
	'wpct'	=>	'승률',
	'tbf'	=>	'상대타자',
	'np'	=>	'투구수',
	'ip'	=>	'이닝',
	'ah'	=>	'피안타',
	'a2b'	=>	'피2루타',
	'a3b'	=>	'피3루타',
	'ahr'	=>	'피홈런',
	'asac'	=>	'피희타',
	'asf'	=>	'피희비',
	'abb'	=>	'볼넷',
	'aibb'	=>	'고의4구',
	'ahbp'	=>	'사구',
	'k'	=>	'탈삼진',
	'wp'	=>	'폭투',
	'bk'	=>	'보크',
	'ar'	=>	'실점',
	'aer'	=>	'자책점',
	'bs'	=>	'블론세이브',
	'whip'	=>	'WHIP',
	'aavg'	=>	'피안타율',
	'qs'	=>	'QS',
	'aab'	=>	'상대타수',
	'aobp'	=>	'피출루율',
	'aslg'	=>	'피장타율',
	'kpi'	=>	'이닝당 탈삼진',
	'npi'	=>	'이닝당투구수',
	'a1b'	=>	'피1루타',
	'PitcherFP'=>	'투수포에버포인트'
);

$exception=array('player_id','team_id','t_g');
$specialCase=array('era','aobp','aslg','aavg','whip','avg','obg','slg','ops','isod','isop','savg');


$n=$_GET['rank'];
if(!$n){
	$n=10;
}
$pStat=$_GET['pStat'];
if(!$pStat){
	$pStat='era';
}
$bStat=$_GET['bStat'];
if(!$bStat){
	$bStat='avg';
}
$name=$_GET['name'];

$result=mysql_query("SELECT player_id FROM player WHERE name='$name'");
$pID=array();
while($row=mysql_fetch_assoc($result)){
	$pID[$row['player_id']]=false;
}

//create table for pitcher rank
mysql_query("CREATE TABLE t_pitcher (SELECT * FROM (SELECT name,player_id FROM player) AS p NATURAL JOIN (SELECT player_id,team_id FROM playerinfo) AS pi NATURAL JOIN (SELECT * FROM pitcher AS p1 WHERE g=(SELECT MAX(g) FROM pitcher AS p2 WHERE p1.player_id=p2.player_id)) AS pit NATURAL JOIN (SELECT team_id,t_g FROM teaminfo AS t1 WHERE t_g=(SELECT MAX(t_g) FROM teaminfo AS t2 where t1.team_id=t2.team_id)) AS ti)");

//create table for batter rank
mysql_query("CREATE TABLE t_batter (SELECT * FROM (SELECT name,player_id FROM player) AS p NATURAL JOIN (SELECT player_id,team_id FROM playerinfo) AS pi NATURAL JOIN (SELECT * FROM batter AS b1 WHERE g=(SELECT MAX(g) FROM batter AS b2 WHERE b1.player_id=b2.player_id)) AS bat NATURAL JOIN (SELECT team_id,t_g FROM teaminfo AS t1 WHERE t_g=(SELECT MAX(t_g) FROM teaminfo AS t2 where t1.team_id=t2.team_id)) AS ti)");
echo "<div id=\"top\"></div>";
echo "<a href=\"#pitcherRank\">투수순위</a></br>";
echo "<a href=\"#batterRank\">타자순위</a></br>";
echo "<a href=\"index.html\">메인페이지로 가기</a></br></br>";
echo "<div id=\"pitcherRank\"></div>";
echo "<a href=\"#top\">↑위로↑</a>";
echo "</br>투수스탯";
$result=mysql_query("SELECT COLUMN_NAME FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_NAME='t_pitcher'");
echo "<table border=1>";
echo "<tr>";
echo "<td>순위</td>";
while($row=mysql_fetch_assoc($result)){
	if(in_array($row['COLUMN_NAME'],$exception)){
		continue;
	}
	if($colName=$engToKor[$row['COLUMN_NAME']]){
		echo "<td><a href=/top.php?rank={$_GET['rank']}&pStat={$row['COLUMN_NAME']}&bStat={$_GET['bStat']}&name={$_GET['name']}>{$colName}</a></td>";
	}else{
		echo "<td><a href=/top.php?rank={$_GET['rank']}&pStat={$row['COLUMN_NAME']}&bStat={$_GET['bStat']}&name={$_GET['name']}>{$row['COLUMN_NAME']}</a></td>";
	}
}
echo "</tr>";

if(in_array($pStat,$specialCase)){
	if($pStat=='era'||$pStat=='aobp'||$pStat=='aslg'||$key=='aavg'){
		if(!$result=mysql_query("SELECT * FROM (SELECT (SELECT COUNT(*)+1 FROM t_pitcher WHERE ip>=t_g AND $pStat<t.$pStat) AS rank,t.* FROM (SELECT * FROM t_pitcher WHERE ip>=t_g) AS t ORDER BY rank) AS rt WHERE rank<=$n OR name='$name'")){
			die('query error');
		}
	}else{
		if(!$result=mysql_query("SELECT * FROM (SELECT (SELECT COUNT(*)+1 FROM t_pitcher WHERE ip>=t_g AND $pStat>t.$pStat) AS rank,t.* FROM (SELECT * FROM t_pitcher WHERE ip>=t_g) AS t ORDER BY rank) AS rt WHERE rank<=$n OR name='$name'")){
			die('query error');
		}
	}
}else{
	if(!$result=mysql_query("SELECT * FROM (SELECT (SELECT COUNT(*)+1 FROM t_pitcher WHERE $pStat>t.$pStat) AS rank,t.* FROM t_pitcher AS t ORDER BY rank) AS rt WHERE rank<=$n OR name='$name'")){
		die("querry error");
	}
}

while($row=mysql_fetch_assoc($result)){
	echo "<tr>";
	foreach($row as $key => $val){
		if($key=='player_id'){
			if(array_key_exists($val,$pID)){
				$pID[$val]=true;
			}
			continue;
		}
		if(in_array($key,$exception)){
			continue;
		}
		if($key=='name'){
			echo "<td><a href=/player.php?searchKey=$val>$val</a></td>";
		}else{
			echo "<td>$val</td>";
		}
	}
	echo "</tr>";
}
foreach($pID as $ID => $bool){
	if(!$bool){
		$result=mysql_query("SELECT * FROM t_pitcher WHERE player_id=$ID");
		while($row=mysql_fetch_assoc($result)){
			echo "<tr><td>-</td>";
			foreach($row as $key => $val){
				if(in_array($key,$exception)){
					continue;
				}
				if($key=='name'){
					echo "<td><a href=/player.php?searchKey=$val>$val</a></td>";
				}else{
					echo "<td>$val</td>";
				}
			}
			echo "</tr>";
		}
	}
}
/*
if(!$nameCheck){
	$result=mysql_query("SELECT * FROM t_pitcher WHERE name='$name'");
	while($row=mysql_fetch_assoc($result)){
		echo "<tr><td>-</td>";
		foreach($row as $key => $val){
			if(in_array($key,$exception)){
				continue;
			}
			if($key=='name'){
				echo "<td><a href=/player.php?searchKey=$val>$val</a></td>";
			}else{
				echo "<td>$val</td>";
			}
		}
		echo "</tr>";
	}
}
*/
echo "</table>";
echo "</br>";
echo "<div id=\"batterRank\"></div>";
echo "<a href=\"#top\">↑위로↑</a>";
echo "</br>타자스탯";
$result=mysql_query("SELECT COLUMN_NAME FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_NAME='t_batter'");
echo "<table border=1>";
echo "<tr>";
echo "<td>순위</td>";
while($row=mysql_fetch_assoc($result)){
	if(in_array($row['COLUMN_NAME'],$exception)){
		continue;
	}
	if($colName=$engToKor[$row['COLUMN_NAME']]){
		echo "<td><a href=/top.php?rank={$_GET['rank']}&pStat={$_GET['pStat']}&bStat={$row['COLUMN_NAME']}&name={$_GET['name']}>{$colName}</a></td>";
	}else{
		echo "<td><a href=/top.php?rank={$_GET['rank']}&pStat={$_GET['pStat']}&bStat={$row['COLUMN_NAME']}&name={$_GET['name']}>{$row['COLUMN_NAME']}</a></td>";
	}
}
echo "</tr>";

if(in_array($bStat,$specialCase)){
	if(!$result=mysql_query("SELECT * FROM (SELECT (SELECT COUNT(*)+1 FROM t_batter WHERE pa>=t_g*3.1 AND $bStat>t.$bStat) AS rank,t.* FROM (SELECT * FROM t_batter WHERE pa>=t_g*3.1) AS t ORDER BY rank) AS rt WHERE rank<=$n OR name='$name'")){
		die('query error');
	}
}else{
	if(!$result=mysql_query("SELECT * FROM (SELECT (SELECT COUNT(*)+1 FROM t_batter WHERE $bStat>t.$bStat) AS rank,t.* FROM t_batter AS t ORDER BY rank) AS rt WHERE rank<=$n OR name='$name'")){
		die("querry error");
	}
}

while($row=mysql_fetch_assoc($result)){
	echo "<tr>";
	foreach($row as $key => $val){
		if($key=='player_id'){
			if(array_key_exists($val,$pID)){
				$pID[$val] = true;
			}
			continue;
		}
		if(in_array($key,$exception)){
			continue;
		}
		if($key=='name'){
			echo "<td><a href=/player.php?searchKey=$val>$val</a></td>";
		}elseif($key=='pavg'&&$val==-1){
			echo "<td>-</td>";
		}else{
			echo "<td>$val</td>";
		}
	}
	echo "</tr>";
}
foreach($pID as $ID => $bool){
	if(!$bool){
		$result=mysql_query("SELECT * FROM t_batter WHERE player_id=$ID");
		while($row=mysql_fetch_assoc($result)){
			echo "<tr><td>-</td>";
			foreach($row as $key => $val){
				if(in_array($key,$exception)){
					continue;
				}
				if($key=='name'){
					echo "<td><a href=/player.php?searchKey=$val>$val</a></td>";
				}else{
					echo "<td>$val</td>";
				}
			}
			echo "</tr>";
		}
	}
}
/*
if(!$nameCheck){
	$result=mysql_query("SELECT * FROM t_batter WHERE name='$name'");
	while($row=mysql_fetch_assoc($result)){
		echo "<tr><td>-</td>";
		foreach($row as $key => $val){
			if(in_array($key,$exception)){
				continue;
			}
			if($key=='name'){
				echo "<td><a href=/player.php?searchKey=$val>$val</a></td>";
			}else{
				echo "<td>$val</td>";
			}
		}
		echo "</tr>";
	}
}
*/
echo "</table>";

echo "<a href=\"#top\">↑위로↑</a></br>";
echo "<a href=\"index.html\">메인페이지로 돌아가기</a>";
mysql_query("DROP TABLE t_pitcher");
mysql_query("DROP TABLE t_batter");
mysql_close($con);
?>
</body>
</html>
