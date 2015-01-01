<?php
echo "<meta charset=\"utf-8\">";
$con = new mysqli("localhost","root","asdf1234","dbproject") or die ("Failed to connect to MySqL: " . mysql_error());

if(mysqli_connect_errno()){
	die("Connect failed :".mysqli_connect_error());
}

mysqli_query($con,"set names utf8");


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
	'npi'	=>	'이닝당 투구수',
	'a1b'	=>	'피1루타',
	'PitcherFP'=>	'투수포에버포인트',

// daily
	'date'	=>	'경기날짜',
	'competitor_team_id'	=>	'상대팀',
	'result'=>	'경기결과'
);

//prepared statement
$pStmt = $con->prepare("SELECT * FROM player NATURAL JOIN playerinfo WHERE name=?");
if(false===$pStmt){
	die("prepare() failed: ".htmlspecialchars($con->error));
}

$rc=$pStmt->bind_param('s',$searchKey);
if(false===$rc){
	die("bind failed: ".htmlspecialchars($pStmt->error));
}

// get basic player info
$rc=$pStmt->execute();
if(false===$rc){
	die("execute() failed: ".htmlspecialchars($pStmt->erro));
}

$result=$pStmt->get_result();

$pStmt->close();
echo "<div id=\"top\"></div>";
if($result->num_rows>0){
	if($result->num_rows>1){
		$i=1;
		echo "<table border=1>";
		echo "<tr><td>no</td><td>이름</td><td>소속팀</td><td>등번호</td></tr>";
		while($row=$result->fetch_assoc()){
			$team=mysqli_query($con,"SELECT name FROM team WHERE team_id={$row['team_id']}");
			$team=mysqli_fetch_assoc($team);
			echo "<tr><td>$i</td><td><a href=\"#no".$i."\">".$row['name']."</a></td><td>".$team['name']."</td><td>".$row['no']."</td></tr>";
			$i=$i+1;
		}
		echo "</table>";
		$result->data_seek(0);
	}
	echo "</br>";
	$i=1;
	while($row=$result->fetch_assoc()){
		$id = $row['player_id'];
		if($result->num_rows>1){
			echo "<div id=\"no".$i."\"></div>";
			echo "<a href=\"#top\">↑위로↑</a></br></br>";
		}
		echo "<table border='1'>";
		echo "<tr>";
		foreach ($row as $key => $val){
			if($key=='player_id'){
				continue;
			}else if($key=='team_id'){
				$teamName=mysqli_query($con,"SELECT name FROM team WHERE team_id={$val}");
				$teamName=mysqli_fetch_array($teamName);
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
		$info = mysqli_query($con,"SELECT * FROM pitcher WHERE player_id=$id ORDER BY g DESC LIMIT 5");
		if (mysqli_num_rows($info)>0){
			echo "투수기록";
			echo "<table border='1'>";
			$isColumn=true;
			while($row = mysqli_fetch_assoc($info)){
				if($isColumn){
					echo "<tr>";
					foreach ($row as $key => $val){
						if($key=='player_id'||$key=='team_id'){
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
			
			echo "날짜별 기록";	
			$daily = mysqli_query($con,"SELECT * FROM (SELECT * FROM daily_pitcher WHERE player_id=$id ORDER BY date DESC LIMIT 10) AS t ORDER BY date");
			echo "<table border='1'>";
			$isColumn=true;
			while($row=mysqli_fetch_assoc($daily)){
				if($isColumn){
					echo "<tr>";
					foreach ($row as $key => $val){
						if($key=='player_id'){
							continue;
						}
						if(!$statName=$engToKor[$key]){
							echo "<td>".$key."</td>";
						}else{
							echo "<td>".$statName."</td>";
						}
						$isColumn=false;
					}
					echo "</tr>";
				}
				echo "</tr>";
				foreach ($row as $key => $val){
					if($key=='player_id'){
						continue;
					}
					if($key=='competitor_team_id'){
						$teamName=mysqli_query($con,"SELECT name FROM team WHERE team_id={$val}");
						$teamName=mysqli_fetch_array($teamName);
						$val=$teamName['name'];
					}
					echo "<td>".$val."</td>";
				}
				echo "</tr>";
			}
			echo "</table>";
			echo "</br>";
		}else{
			echo "타자기록";
			$info = mysqli_query($con,"SELECT * FROM batter date WHERE player_id=$id ORDER BY g DESC LIMIT 5");
			echo "<table border='1'>";
			$isColumn=true;
			while($row = mysqli_fetch_assoc($info)){
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
				
			echo "날짜별 기록";
			$daily = mysqli_query($con,"SELECT * FROM (SELECT * FROM daily_batter WHERE player_id=$id ORDER BY date DESC LIMIT 10) AS t ORDER BY date");
			echo "<table border='1'>";
			$isColumn=true;
			while($row=mysqli_fetch_assoc($daily)){
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
						$teamName=mysqli_query($con,"SELECT name FROM team WHERE team_id={$val}");
						$teamName=mysqli_fetch_array($teamName);
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
mysqli_close($con);
echo "<a href=\"#top\">↑위로↑</a></br></br>";
echo "<a href=\"index.html\">메인페이지로 돌아가기</a>";
?>
