<?php
	$bg=array('1.jpg','2.jpg','3.jpg','4.jpg','5.jpg','6.jpg','7.jpg','8.jpg');
	$i=rand(0, count($bg)-1);
	$selectedBg=$bg[$i];
?>

<!DOCTYPE html>
<html>
<head>
	<title>DB Project Main Page</title>
	<meta http-equiv="content-type" content="text/html; charset=UTF-8" />

	<style type="text/css">
		#body{
		background: url(image/<?php echo $selectedBg; ?>);
		background-size: contain;
		background-repeat: no-repeat;
		background-position: right;
		top: 0;
		bottom: 0;
		}
	</style>

	<div id="body"/>

</head>
<body>
	<h1>공팔포에버</h1>
	<h2>선수 검색</h2>
	<form action="player.php" method="get">
		<input type=text name="searchKey" />
		<input type=submit value="선수 검색" />
	</form>
	<h2>순위 TOP N</h2>
	<form action="top.php" method="get">
		TOP N : <input type=number name="rank" value=10 /><br />
		추가 선수 이름(띄어쓰기로 구분) : <input type=text name="name" />
		<input type=submit value="순위 보기">
	</form>
	<h2>팀 정보 보기</h2>
	<form action="team_page.php" method="get">
		팀 순위 및 기타 정보 보기 : <input type=submit value="순위 보기">
	</form>
	<h3>승부 예측</h3>
	<form action="match.php" method="get">
		타자 이름 : <input type=text name="batterName"><br />
		투수 이름 : <input type=text name="pitcherName">
		<input type=submit value="승부 예측하기">
	</form>
	<h4>관리</h4>
	<form method="post" action="clean_daily.php">
		<input type=submit value="플레이어 날짜별 기록 삭제">
	</form>
	<form method="post" action="crawler.php">
		<input type=submit value="웹 크롤러 돌리기(주의)">
	</form>
</body>
</html>
