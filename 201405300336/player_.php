<?php
echo "<meta charset=\"utf-8\">";

$con = mysql_connect("localhost","root","asdf1234") or die ("Failed to connect to MySqL: " . mysql_error());

mysql_query("set names utf8");

mysql_select_db("dbproject") or die ("Failed to select DB");

$searchKey = $_GET['searchKey'];

$exceptionList=array('player_id','team_id');


$engToKor=array(
// player info
	'name'	=>	'이름',
	'birth'	=>	'생년월일',
	'height'=>	'신장',
	'weight'=>	'체중',
	'updated_date'=>'업데이트 날짜',
	'team_id'=>	'소속팀',
	'no'	=>	'등번호',
	'pos'	=>	'포지션',
	'dep'	=>	'계약금',
	'sal'	=>	'연봉',
	'year'	=>	'입단년도',
	'career'=>	'경력',

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
	'cs'	=>	'도실',
	'sac'	=>	'희타',
	'sf'	=>	'희비',
	'bb'	=>	'볼넷',
	'ibb'	=>	'고의4구',
	'hbp'	=>	'사구',
	'so'	=>	'삼진',
	'gdp'	=>	'병살',
	'slg'	=>	'장타율',
	'obp'	=>	'출루율',
	'err'	=>	'실책',
	'sr'	=>	'도루 성공율',
	'bbk'	=>	'BB/K',
	'slgr'	=>	'장타/안타',
	'mh'	=>	'멀티히트',
	'ops'	=>	'OPS',
	'savg'	=>	'득점권 타율',
	'pavg'	=>	'대타 타율',

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

// daily
	'date'	=>	'경기날짜',
	'competitor_team_id'	=>	'상대팀'
);

// get basic player info

//$pStmt->execute();
//$pStmt->store_result();

$result = mysql_query("SELECT * FROM player NATURAL JOIN playerinfo WHERE name='$searchKey'");
echo "</br>";

if(mysql_num_rows($result)>0){
	if(mysql_num_rows($result)>1){
		echo "Multiple players found</br>";
		$IDs=$result['player_id'];
		while($row=mysql_fetch_array($result)){
			echo "id : ".$row['player_id']."</br>";
		}
		echo "</br>";
		mysql_data_seek($result,0);
	}
	$i=1;
	while($row=mysql_fetch_assoc($result)){
		
		$id = $row['player_id'];
	
		echo "Search result no.".$i."</br>";	
	
		echo "<table border='1'>";
		echo "<tr>";
		foreach ($row as $key => $val){
			if($key=='player_id'){
				continue;
			}else if($key=='team_id'){
				$teamName=mysql_query("SELECT name FROM team WHERE team_id={$val}");
				$teamName=mysql_fetch_array($teamName);
				$val=$teamName['name'];
			}
			if($key=='sal'||$key=='dep'){
				echo "<tr><td>".$engToKor[$key]."</td><td>".$val."만원</td></tr>";
			}else{
				echo "<tr><td>".$engToKor[$key]."</td><td>".$val."</td></tr>";
			}
		}
		echo "</tr>";
		echo "</table>";
		echo "</br>";

		$info = mysql_query("SELECT * FROM pitcher WHERE player_id=$id ORDER BY g DESC LIMIT 5");
		if (mysql_num_rows($info)>0){
			echo "</br>Pitcher</br>";
			echo "<table border='1'>";
			$isColumn=true;
			while($row = mysql_fetch_assoc($info)){
				if($isColumn){
					echo "<tr>";
					foreach ($row as $key => $val){
						if(in_array($key,$excetionList)){
							continue;
						}
						if(!$statName=$engToKor[$key]){
							echo "<td>".$key."</td>";
						}else{
							echo "<td>".$statName."</td>";
						}
					}
					$isColumn=false;
					echo "</tr>";
				}
				echo "<tr>";
				foreach ($row as $key => $val){
					if(in_array($key,$exceptionList)){
						continue;
					}
					echo "<td>".$val."</td>";
				}
				echo "</tr>";
			}
			echo "</table>";
			echo "</br>";
			
			echo "</br>Daily Info</br>";	
			$daily = mysql_query("SELECT * FROM daily_pitcher WHERE player_id=$id ORDER BY date DESC LIMIT 10");
			echo "<table border='1'>";
			$isColumn=true;
			while($row=mysql_fetch_assoc($daily)){
				if($isColumn){
					echo "<tr>";
					foreach ($row as $key => $val){
						if(in_array($key,$exceptionList)){
							continue;
						}
						if(!$statName=$engToKor[$key]){
							echo "<td>".$key."</td>";
						}else{
							echo "<td>".$statName."</td>";
						}
						echo "<td>".$key."</td>";
						$isColumn=false;
					}
					echo "</tr>";
				}
				echo "</tr>";
				foreach ($row as $key => $val){
					if($key=='competitor_team_id'){
						$teamName=mysql_query("SELECT name FROM team WHERE team_id={$val}");
						$teamName=mysql_fetch_array($teamName);
						$val=$teamName['name'];
					}
					echo "<td>".$val."</td>";
				}
				echo "</tr>";
			}
			echo "</table>";
			echo "</br>";
		}else{
			echo "</br>Batter</br>";
			$info = mysql_query("SELECT * FROM batter date WHERE player_id=$id ORDER BY g DESC LIMIT 5");
			echo "<table border='1'>";
			$isColumn=true;
			while($row = mysql_fetch_assoc($info)){
				if($isColumn){
					echo "<tr>";
					foreach ($row as $key => $val){
						if(in_array($key,$exceptionList)){
							continue;
						}
						if(!$statName=$engToKor[$key]){
							echo "<td>".$key."</td>";
						}else{
							echo "<td>".$statName."</td>";
						}
					}
					echo "</tr>";
					$isColumn=false;
				}
				echo "<tr>";
				foreach ($row as $key => $val){
					if(in_array($key,$exceptionList)){
						continue;
					}
					if($key=='pavg' && $val==-1){
						$val='-';
					}
					echo "<td>".$val."</td>";
				}
				echo "</tr>";
			}
			echo "</table>";
			echo "</br>";
				
			echo "</br>Daily Info</br>";
			$daily = mysql_query("SELECT * FROM daily_batter WHERE player_id=$id ORDER BY date DESC LIMIT 10");
			echo "<table border='1'>";
			$isColumn=true;
			while($row=mysql_fetch_assoc($daily)){
				if($isColumn){
					echo "<tr>";
					foreach ($row as $key => $val){
						if(in_array($key,$exceptionList)){
							continue;
						}
						if(!$statName=$engToKor[$key]){
							echo "<td>".$key."</td>";
						}else{
							echo "<td>".$statName."</td>";
						}
					}
					echo "</tr>";
					$isColumn=false;
				}
				echo "<tr>";
				foreach ($row as $key => $val){
					if(in_array($key,$exceptionList)){
						continue;
					}
					if($key=='competitor_team_id'){
						$teamName=mysql_query("SELECT name FROM team WHERE team_id={$val}");
						$teamName=mysql_fetch_array($teamName);
						$val=$teamName['name'];
					}
					echo "<td>".$val."</td>";
				}
				echo "</tr>";
			}
			echo "</table>";
			echo "</br>";
			$isColumn=true;
			$i=$i+1;			
		}
	}
}else{
	echo "No Result</br>";
}
mysql_close($con);

?>
