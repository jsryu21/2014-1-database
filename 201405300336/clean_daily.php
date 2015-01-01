<?php
exec('/home/jsryu21/clean_daily.py', $output);
foreach ($output as $value) {
	echo $value;
}
echo "Daily player records Deleted!";
?>
<form method="post" action="index.html">
	<button type="submit">돌아가기</button>
</form>
