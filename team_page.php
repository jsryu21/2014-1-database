<!DOCTYPE html>
<html>
<head>
	<title>팀 정보/순위</title>
	<meta http-equiv="content-type" content="text/html; charset=UTF-8" />
</head>
<body>
<?php

$conn=mysql_connect('localhost','root','asdf1234') or die("Could not connect: ".mysql_error()."</br>");
mysql_query("set names utf8");
mysql_select_db('dbproject') or die("Failed to select database: ".mysql_error()."</br>");

$engToKor=array(
	'name'	=>	'팀명',
	't_era'	=>	'팀 평균자책점',
	't_g'	=>	'팀 게임 수',
	't_sho'	=>	'팀 완투',
	't_cg'	=>	'팀 완봉',
	't_w'	=>	'팀 승',
	't_l'	=>	'팀 패',
	't_sv'	=>	'팀 세',
	't_hld'	=>	'팀 홀',
	't_wavg'=>	'팀 승률',
	't_tbf'	=>	'팀 상대타자',
	't_np'	=>	'팀 투구수',
	't_ip'	=>	'팀 이닝',
	't_ah'	=>	'팀 피안타',
	't_a2b'	=>	'팀 피2루타',
	't_a3b'	=>	'팀 피3루타',
	't_ahr'	=>	'팀 피홈런',
	't_asac'=>	'팀 피희타',
	't_asf'	=>	'팀 피희비',
	't_abb'	=>	'팀 볼넷',
	't_aibb'=>	'팀 고의4구',
	't_ahbp'=>	'팀 사구',
	't_k'	=>	'팀 탈삼진',
	't_wp'	=>	'팀 폭투',
	't_bk'	=>	'팀 보크',
	't_ar'	=>	'팀 실점',
	't_aer'	=>	'팀 자책점',
	't_bs'	=>	'팀 블론세이브',
	't_whip'=>	'팀 WHIP',
	't_aavg'=>	'팀 피안타율',
	't_qs'	=>	'팀 QS',
	't_avg'	=>	'팀 타율',
	't_pa'	=>	'팀 타석',
	't_ab'	=>	'팀 타수',
	't_r'	=>	'팀 득점',
	't_hit'	=>	'팀 안타',
	't_2b'	=>	'팀 2루타',
	't_3b'	=>	'팀 3루타',
	't_hr'	=>	'팀 홈런',
	't_tb'	=>	'팀 루타',
	't_rbi'	=>	'팀 타점',
	't_sb'	=>	'팀 도루',
	't_cs'	=>	'팀 도루실패',
	't_sac'	=>	'팀 희타',
	't_sf'	=>	'팀 희비',
	't_bb'	=>	'팀 피볼넷',
	't_ibb'	=>	'팀 피고의4구',
	't_hbp'	=>	'팀 피사구',
	't_so'	=>	'팀 피삼진',
	't_gdp'	=>	'팀 병살',
	't_slg'	=>	'팀 장타율',
	't_obp'	=>	'팀 출루율',
	't_err'	=>	'팀 실책',
	't_slgr'=>	'팀 장타/안타',
	't_mh'	=>	'팀 멀티히트',
	't_ops'	=>	'팀 OPS',
	't_savg'=>	'팀 득점권 타율',
	't_pavg'=>	'팀 대타 타율',
	't_rank'=>	'팀순위',
	't_tie'	=>	'무승부',
	't_diff'=>	'diff',
	't_seq'	=>	'연승기록'
);
$ASCCase=array('t_rank','t_era','t_aobp','t_aslg','t_aavg');

$stat=$_GET['stat'];
if(!$stat){
	$stat='t_rank';
}

mysql_query("CREATE TABLE t_team (SELECT * FROM team NATURAL JOIN (SELECT * FROM teaminfo AS t1 WHERE t_g=(SELECT MAX(t_g) FROM teaminfo AS t2 WHERE t1.team_id=t2.team_id)) AS t)") or die("create table error");
mysql_query("ALTER TABLE t_team MODIFY COLUMN t_rank INT AFTER name") or die("alter error");;
$columns=mysql_query("SELECT COLUMN_NAME FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_NAME='t_team'") or die("Query error colName");
if(in_array($stat,$ASCCase)){
	$result=mysql_query("SELECT * FROM t_team ORDER BY $stat") or die("Query error result");
}else{
	$result=mysql_query("SELECT * FROM t_team ORDER BY $stat DESC") or die ("Query error result");
}
echo "<div id=\"top\" />";
echo "<table border=1>";
echo "<thead>";
echo "<tr>";

while($colName=mysql_fetch_assoc($columns)){
	if($colName['COLUMN_NAME']=='team_id'){
		continue;
	}
	echo "<th>";
	if($col=$engToKor[$colName['COLUMN_NAME']]){
		echo "<a href=\"team_page.php?stat={$colName['COLUMN_NAME']}\">{$col}</a>";
	}else{
		echo "<a href=\"team_page.php?stat={$colName['COLUMN_NAME']}\">{$colName['COLUMN_NAME']}</a>";
	}
	echo "</th>";
}
echo "</tr>";
echo "</thead>";
echo "<tbody>";
while($row=mysql_fetch_assoc($result)){
	echo "<tr>";
	foreach($row as $key => $val){
		if($key=='team_id'){
			continue;
		}
		echo "<td>$val</td>";
	}
	echo "</tr>";
}
echo "</table>";
echo "<a href=\"#top\">TOP</a><br />";

mysql_query("DROP TABLE t_team");
?>
	<form method="post" action="index.php">
		<button type="submit">메인 페이지로 돌아가기</button>
	</form>
</body>
</html>
