<!DOCTYPE html>
<html>
<head>
	<title>플레이어 날짜별 기록 삭제</title>
	<meta http-equiv="content-type" content="text/html; charset=UTF-8" />
</head>
<body>
<?php
exec("/home/jsryu21/clean_daily.py", $output);
foreach ($output as $value) {
	echo $value;
	echo "<br />";
}
?>
	플레이어 날짜별 기록 삭제 완료.<br />
	<form method="post" action="index.php">
		<button type="submit">메인 페이지로 돌아가기</button>
	</form>
</body>
</html>
