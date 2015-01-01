<!DOCTYPE html>
<html>
<head>
	<title>웹 크롤러 실행</title>
	<meta http-equiv="content-type" content="text/html; charset=UTF-8" />
</head>
<body>
<?php
exec("/home/jsryu21/crawler.py");
?>
	웹 크롤링 완료.<br />
	<form method="post" action="index.php">
		<button type="submit">메인 페이지로 돌아가기</button>
	</form>
</body>
</html>
