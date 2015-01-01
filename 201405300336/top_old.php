<html>
<head>
	<title>Top Players!</title>
	<meta http-equiv="Content-Type" content="text/html" charset="utf-8">
</head>
<body>
<?php
$con = mysql_connect('localhost','root','asdf1234') or die('Could not connect: ' . mysql_Error() . "</br>");
mysql_query("set names utf8");
mysql_select_db('dbproject');

$n = $_GET['rank'];
//if(empty($n)) {
//	$n = 10
//}
$engToKor=array(
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
	'tbf'	=>	'타자',
	'np'	=>	'투구수',
	'ip'	=>	'이닝',
	'ah'	=>	'피안타',
	'a2b'	=>	'2루타',
	'a3b'	=>	'3루타',
	'ahr'	=>	'피홈런',
	'asac'	=>	'희타',
	'asf'	=>	'희비',
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
	'aobp'	=>	'피출루율',
	'aslg'	=>	'피장타율',
	'kpi'	=>	'이닝당 탈삼진',
	'a1b'	=>	'피1루타',
	'PitcherFP'=>	'투수포에버포인트'
);

echo "<div id=\"top\"></div>";
echo "<a href=\"#pitcher\">투수순위</a></br>";
echo "<a href=\"#batter\">타자순위</a></br>";
echo "</br></br>";

echo "<div id=\"pitcher\"></div>투수 스탯</br></br>";

$pitResult = mysql_query("SELECT * FROM player NATURAL JOIN pitcher");
$colName = mysql_fetch_assoc($pitResult);

$noDupPitcher="SELECT * FROM pitcher AS p1 WHERE g=(SELECT MAX(g) FROM pitcher AS p2 WHERE p1.player_id=p2.player_id)";
$noDupTeaminfo="SELECT team_id,t_g FROM teaminfo AS t1 WHERE t_g=(SELECT MAX(t_g) FROM teaminfo AS t2 WHERE t1.team_id=t2.team_id)";
$specialCase=array('whip','avg','obg','slg','ops','isod','isop','savg');

echo "<div id=\"pitcher\"></div>";
foreach($colName as $key => $val){
	$exceptionList=array('player_id','name','birth','height','weight','team_id');
	
	if(in_array($key,$exceptionList)){
		continue;
	}

	if(!$statName=$engToKor[$key]){
		echo $key."</br>";
	}else{
		echo $statName."</br>";
	}

	if($key=='era'||$key=='aobp'|$key=='aslg'||$key=='aavg'){
		if(!$result=mysql_query("SELECT name,{$key} FROM player NATURAL JOIN playerinfo NATURAL JOIN ({$noDupPitcher}) AS tmp1 NATURAL JOIN ({$noDupTeaminfo}) AS tmp2 WHERE ip>=t_g ORDER BY {$key} LIMIT {$n}")){
			die("query execution error " . mysql_error());
		}
	}elseif(in_array($key,$specialCase)){
		if(!$result=mysql_query("SELECT name,{$key} FROM player NATURAL JOIN playerinfo NATURAL JOIN ({$noDupPitcher}) AS tmp1 NATURAL JOIN ({$noDupTeaminfo}) AS tmp2 WHERE ip>=t_g ORDER BY {$key} DESC LIMIT {$n}")){
			die("query excution error " . mysql_error());
		}
	}else{
		if(!$result=mysql_query("SELECT name,{$key} FROM player NATURAL JOIN ({$noDupPitcher}) AS t ORDER BY {$key} DESC LIMIT {$n}")){
			die("query execution error" . mysql_errno());
		}
	}
			

	$resultCopy=$result;

	$i = 1;
	echo "<table border='1'>";
	while($row = mysql_fetch_array($result)){
		echo "<tr><td>".$i."</td><td>".$row['name']."</td><td>".$row[$key]."</td></tr>";
		$i = $i+1;
	}

	echo "</table>";
	echo "</br>";
}

echo "</br>";

echo "<a href=\"#top\">↑↑위로↑↑</a>";
$batResult = mysql_query("SELECT * FROM player NATURAL JOIN batter");
$colName = mysql_fetch_assoc($batResult);
$noDupBatter="SELECT * FROM batter AS b1 WHERE g=(SELECT MAX(g) FROM batter AS b2 WHERE b1.player_id=b2.player_id)";
echo "<div id=\"batter\"></div>타자 스탯</br></br>";

foreach($colName as $key => $val){
	$exceptionList=array('player_id','name','birth','height','weight','team_id');
	if(in_array($key,$exceptionList)){
		continue;
	}
	
	if(!$statName=$engToKor[$key]){
		echo $key."</br>";
	}else{
		echo $statName."</br>";
	}
	if(in_array($key,$specialCase)){
		if(!$result=mysql_query("SELECT name,{$key} FROM player NATURAL JOIN playerinfo NATURAL JOIN ({$noDupBatter}) AS tmp1 NATURAL JOIN ({$noDupTeaminfo}) AS tmp2 WHERE pa>=t_g*3.1 ORDER BY {$key} DESC LIMIT {$n}")){
			die("query excution error " . mysql_error());
		}
	}else{
		if(!$result=mysql_query("SELECT name,{$key} FROM player NATURAL JOIN ({$noDupBatter}) AS t ORDER BY {$key} DESC LIMIT {$n}")){
			die("query excution error " . mysql_error());
		}
	}

	$i = 1;
	echo "<table border='1'>";
	while($row = mysql_fetch_array($result)){
		echo "<tr><td>".$i."</td><td>".$row['name']."</td><td>".$row[$key]."</td></tr>";
		$i = $i+1;
	}
	echo "</table>";
	echo "</br>";
}

echo "<a href=\"#top\">↑↑위로↑↑</a></br>";
echo "<a href=\"/index.html\">메인 페이지로 돌아가기</a>";


mysql_close($con);
?>
</body>
</html>
