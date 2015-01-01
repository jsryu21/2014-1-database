<html>
<head>
	<title>Top 10 Players!</title>
	<meta http-equiv="Content-Type" content="text/html; charset=utf-8">
</head>
<body>
<?php
$con = mysql_connect('localhost', 'root', 'asdf1234') or die('Could not connect: ' . mysql_error() . "</br>");
mysql_query("set names utf8");
mysql_select_db('dbproject') or die('Could not select database </br>');
echo "RANKINGS </br>";

echo "</br>pitcher";
echo "</br>";

echo "</br>ERA</br>";
$sql = 'SELECT name,era FROM player natural join pitcher ORDER BY era LIMIT 10';
$result = mysql_query($sql);
$i = 1;
while($row = mysql_fetch_array($result)){
	echo $i . $row['name'] . " " .$row['era'];
	echo "</br>";
	$i = $i+1;
}
echo "</br>G</br>";
$sql = "SELECT name,g FROM player natural join pitcher ORDER BY g DESC LIMIT 10";
$result = mysql_query($sql);
$i = 1;
while($row = mysql_fetch_array($result)){
	echo $i . $row['name'] . " " .$row['g'];
	echo "</br>";
	$i = $i+1;
}
echo "</br>SHO</br>";
$sql = "SELECT name,sho FROM player natural join pitcher ORDER BY sho DESC LIMIT 10";
$result = mysql_query($sql);
$i = 1;
while($row = mysql_fetch_array($result)){
	echo $i . $row['name'] . " " .$row['sho'];
	echo "</br>";
	$i = $i+1;
}
echo "</br>CG</br>";
$sql = "SELECT name,cg FROM player natural join pitcher ORDER BY cg DESC LIMIT 10";
$result = mysql_query($sql);
$i = 1;
while($row = mysql_fetch_array($result)){
	echo $i . $row['name'] . " " .$row['cg'];
	echo "</br>";
	$i = $i+1;
}
echo "</br>W</br>";
$sql = "SELECT name,w FROM player natural join pitcher ORDER BY w DESC LIMIT 10";
$result = mysql_query($sql);
$i = 1;
while($row = mysql_fetch_array($result)){
	echo $i . $row['name'] . " " .$row['w'];
	echo "</br>";
	$i = $i+1;
}
echo "</br>L</br>";
$sql = "SELECT name,l FROM player natural join pitcher ORDER BY l DESC LIMIT 10";
$result = mysql_query($sql);
$i = 1;
while($row = mysql_fetch_array($result)){
	echo $i . $row['name'] . " " .$row['l'];
	echo "</br>";
	$i = $i+1;
}
echo "</br>SV</br>";
$sql = "SELECT name,sv FROM player natural join pitcher ORDER BY sv DESC LIMIT 10";
$result = mysql_query($sql);
$i = 1;
while($row = mysql_fetch_array($result)){
	echo $i . $row['name'] . " " .$row['sv'];
	echo "</br>";
	$i = $i+1;
}
echo "</br>HLD</br>";
$sql = "SELECT name,hld FROM player natural join pitcher ORDER BY hld DESC LIMIT 10";
$result = mysql_query($sql);
$i = 1;
while($row = mysql_fetch_array($result)){
	echo $i . $row['name'] . " " .$row['hld'];
	echo "</br>";
	$i = $i+1;
}
echo "</br>WPCT</br>";
$sql = "SELECT name,wpct FROM player natural join pitcher ORDER BY wpct DESC LIMIT 10";
$result = mysql_query($sql);
$i = 1;
while($row = mysql_fetch_array($result)){
	echo $i . $row['name'] . " " .$row['wpct'];
	echo "</br>";
	$i = $i+1;
}
echo "</br>TBF</br>";
$sql = "SELECT name,tbf FROM player natural join pitcher ORDER BY tbf DESC LIMIT 10";
$result = mysql_query($sql);
$i = 1;
while($row = mysql_fetch_array($result)){
	echo $i . $row['name'] . " " .$row['tbf'];
	echo "</br>";
	$i = $i+1;
}
echo "<br>NP<br>";
$sql = "SELECT name,np FROM player natural join pitcher ORDER BY np DESC LIMIT 10";
$result = mysql_query($sql);
$i = 1;
while($row = mysql_fetch_array($result)){
	echo $i . $row['name'] . " " .$row['np'];
	echo "</br>";
	$i = $i+1;
}
echo "</br>IP</br>";
$sql = "SELECT name,ip FROM player natural join pitcher ORDER BY ip DESC LIMIT 10";
$result = mysql_query($sql);
$i = 1;
while($row = mysql_fetch_array($result)){
	echo $i . $row['name'] . " " .$row['ip'];
	echo "</br>";
	$i = $i+1;
}
echo "</br>AH</br>";
$sql = "SELECT name,ah FROM player natural join pitcher ORDER BY ah DESC LIMIT 10";
$result = mysql_query($sql);
$i = 1;
while($row = mysql_fetch_array($result)){
	echo $i . $row['name'] . " " .$row['ah'];
	echo "</br>";
	$i = $i+1;
}
echo "</br>A2B</br>";
$sql = "SELECT name,a2b FROM player natural join pitcher ORDER BY a2b DESC LIMIT 10";
$result = mysql_query($sql);
$i = 1;
while($row = mysql_fetch_array($result)){
	echo $i . $row['name'] . " " .$row['a2b'];
	echo "</br>";
	$i = $i+1;
}
echo "</br>A3B</br>";
$sql = "SELECT name,a3b FROM player natural join pitcher ORDER BY a3b DESC LIMIT 10";
$result = mysql_query($sql);
$i = 1;
while($row = mysql_fetch_array($result)){
	echo $i . $row['name'] . " " .$row['a3b'];
	echo "</br>";
	$i = $i+1;
}
echo "</br>AHR</br>";
$sql = "SELECT name,ahr FROM player natural join pitcher ORDER BY ahr DESC LIMIT 10";
$result = mysql_query($sql);
$i = 1;
while($row = mysql_fetch_array($result)){
	echo $i . $row['name'] . " " .$row['ahr'];
	echo "</br>";
	$i = $i+1;
}
echo "</br>ASAC</br>";
$sql = "SELECT name,asac FROM player natural join pitcher ORDER BY asac DESC LIMIT 10";
$result = mysql_query($sql);
$i = 1;
while($row = mysql_fetch_array($result)){
	echo $i . $row['name'] . " " .$row['asac'];
	echo "</br>";
	$i = $i+1;
}
echo "</br>ASF</br>";
$sql = "SELECT name,asf FROM player natural join pitcher ORDER BY asf DESC LIMIT 10";
$result = mysql_query($sql);
$i = 1;
while($row = mysql_fetch_array($result)){
	echo $i . $row['name'] . " " .$row['asf'];
	echo "</br>";
	$i = $i+1;
}
echo "</br>ABB</br>";
$sql = "SELECT name,abb FROM player natural join pitcher ORDER BY abb DESC LIMIT 10";
$result = mysql_query($sql);
$i = 1;
while($row = mysql_fetch_array($result)){
	echo $i . $row['name'] . " " .$row['abb'];
	echo "</br>";
	$i = $i+1;
}
echo "</br>AIBB</br>";
$sql = "SELECT name,aibb FROM player natural join pitcher ORDER BY aibb DESC LIMIT 10";
$result = mysql_query($sql);
$i = 1;
while($row = mysql_fetch_array($result)){
	echo $i . $row['name'] . " " .$row['aibb'];
	echo "</br>";
	$i = $i+1;
}
echo "</br>AHBP</br>";
$sql = "SELECT name,ahbp FROM player natural join pitcher ORDER BY ahbp DESC LIMIT 10";
$result = mysql_query($sql);
$i = 1;
while($row = mysql_fetch_array($result)){
	echo $i . $row['name'] . " " .$row['ahbp'];
	echo "</br>";
	$i = $i+1;
}
echo "</br>K</br>";
$sql = "SELECT name,k FROM player natural join pitcher ORDER BY k DESC LIMIT 10";
$result = mysql_query($sql);
$i = 1;
while($row = mysql_fetch_array($result)){
	echo $i . $row['name'] . " " .$row['k'];
	echo "</br>";
	$i = $i+1;
}
echo "</br>WP</br>";
$sql = "SELECT name,wp FROM player natural join pitcher ORDER BY wp DESC LIMIT 10";
$result = mysql_query($sql);
$i = 1;
while($row = mysql_fetch_array($result)){
	echo $i . $row['name'] . " " .$row['wp'];
	echo "</br>";
	$i = $i+1;
}
echo "</br>BK</br>";
$sql = "SELECT name,bk FROM player natural join pitcher ORDER BY bk DESC LIMIT 10";
$result = mysql_query($sql);
$i = 1;
while($row = mysql_fetch_array($result)){
	echo $i . $row['name'] . " " .$row['bk'];
	echo "</br>";
	$i = $i+1;
}
echo "</br>AR</br>";
$sql = "SELECT name,ar FROM player natural join pitcher ORDER BY ar DESC LIMIT 10";
$result = mysql_query($sql);
$i = 1;
while($row = mysql_fetch_array($result)){
	echo $i . $row['name'] . " " .$row['ar'];
	echo "</br>";
	$i = $i+1;
}
echo "</br>AER</br>";
$sql = "SELECT name,aer FROM player natural join pitcher ORDER BY aer DESC LIMIT 10";
$result = mysql_query($sql);
$i = 1;
while($row = mysql_fetch_array($result)){
	echo $i . $row['name'] . " " .$row['aer'];
	echo "</br>";
	$i = $i+1;
}
echo "</br>BS</br>";
$sql = "SELECT name,bs FROM player natural join pitcher ORDER BY bs DESC LIMIT 10";
$result = mysql_query($sql);
$i = 1;
while($row = mysql_fetch_array($result)){
	echo $i . $row['name'] . " " .$row['bs'];
	echo "</br>";
	$i = $i+1;
}
echo "</br>WHIP</br>";
$sql = "SELECT name,whip FROM player natural join pitcher ORDER BY whip DESC LIMIT 10";
$result = mysql_query($sql);
$i = 1;
while($row = mysql_fetch_array($result)){
	echo $i . $row['name'] . " " .$row['whip'];
	echo "</br>";
	$i = $i+1;
}
echo "</br>AAVG</br>";
$sql = "SELECT name,aavg FROM player natural join pitcher ORDER BY aavg LIMIT 10";
$result = mysql_query($sql);
$i = 1;
while($row = mysql_fetch_array($result)){
	echo $i . $row['name'] . " " .$row['aavg'];
	echo "</br>";
	$i = $i+1;
}
echo "</br>QS</br>";
$sql = "SELECT name,qs FROM player natural join pitcher ORDER BY qs LIMIT 10";
$result = mysql_query($sql);
$i = 1;
while($row = mysql_fetch_array($result)){
	echo $i . $row['name'] . " " .$row['qs'];
	echo "</br>";
	$i = $i+1;
}

echo "</br>";
echo "BATTER";
echo "</br>";

echo "</br>AVG</br>";
$sql = "SELECT name,avg FROM player natural join batter ORDER BY avg LIMIT 10";
$result = mysql_query($sql);
$i = 1;
while($row = mysql_fetch_array($result)){
	echo $i . $row['name'] . " " .$row['avg'];
	echo "</br>";
	$i = $i+1;
}
echo "</br>G</br>";
$sql = "SELECT name,g FROM player natural join batter ORDER BY g DESC LIMIT 10";
$result = mysql_query($sql);
$i = 1;
while($row = mysql_fetch_array($result)){
	echo $i . $row['name'] . " " .$row['g'];
	echo "</br>";
	$i = $i+1;
}
echo "</br>PA</br>";
$sql = "SELECT name,pa FROM player natural join batter ORDER BY pa DESC LIMIT 10";
$result = mysql_query($sql);
$i = 1;
while($row = mysql_fetch_array($result)){
	echo $i . $row['name'] . " " .$row['pa'];
	echo "</br>";
	$i = $i+1;
}
echo "</br>AB</br>";
$sql = "SELECT name,ab FROM player natural join batter ORDER BY ab DESC LIMIT 10";
$result = mysql_query($sql);
$i = 1;
while($row = mysql_fetch_array($result)){
	echo $i . $row['name'] . " " .$row['ab'];
	echo "</br>";
	$i = $i+1;
}
echo "</br>R</br>";
$sql = "SELECT name,r FROM player natural join batter ORDER BY r DESC LIMIT 10";
$result = mysql_query($sql);
$i = 1;
while($row = mysql_fetch_array($result)){
	echo $i . $row['name'] . " " .$row['r'];
	echo "</br>";
	$i = $i+1;
}
echo "</br>HIT</br>";
$sql = "SELECT name,hit FROM player natural join batter ORDER BY hit DESC LIMIT 10";
$result = mysql_query($sql);
$i = 1;
while($row = mysql_fetch_array($result)){
	echo $i . $row['name'] . " " .$row['hit'];
	echo "</br>";
	$i = $i+1;
}
echo "</br>2B</br>";
$sql = "SELECT name,2b FROM player natural join batter ORDER BY 2b DESC LIMIT 10";
$result = mysql_query($sql);
$i = 1;
while($row = mysql_fetch_array($result)){
	echo $i . $row['name'] . " " .$row['2b'];
	echo "</br>";
	$i = $i+1;
}
echo "</br>3B</br>";
$sql = "SELECT name,3b FROM player natural join batter ORDER BY 3b DESC LIMIT 10";
$result = mysql_query($sql);
$i = 1;
while($row = mysql_fetch_array($result)){
	echo $i . $row['name'] . " " .$row['3b'];
	echo "</br>";
	$i = $i+1;
}
echo "</br>HR</br>";
$sql = "SELECT name,hr FROM player natural join batter ORDER BY hr DESC LIMIT 10";
$result = mysql_query($sql);
$i = 1;
while($row = mysql_fetch_array($result)){
	echo $i . $row['name'] . " " .$row['hr'];
	echo "</br>";
	$i = $i+1;
}
echo "</br>TB</br>";
$sql = "SELECT name,tb FROM player natural join batter ORDER BY tb DESC LIMIT 10";
$result = mysql_query($sql);
$i = 1;
while($row = mysql_fetch_array($result)){
	echo $i . $row['name'] . " " .$row['tb'];
	echo "</br>";
	$i = $i+1;
}
echo "</br>PBI</br>";
$sql = "SELECT name,pbi FROM player natural join batter ORDER BY pbi DESC LIMIT 10";
$result = mysql_query($sql);
$i = 1;
while($row = mysql_fetch_array($result)){
	echo $i . $row['name'] . " " .$row['pbi'];
	echo "</br>";
	$i = $i+1;
}
echo "</br>SB</br>";
$sql = "SELECT name,sb FROM player natural join batter ORDER BY sb DESC LIMIT 10";
$result = mysql_query($sql);
$i = 1;
while($row = mysql_fetch_array($result)){
	echo $i . $row['name'] . " " .$row['sb'];
	echo "</br>";
	$i = $i+1;
}
echo "</br>CS</br>";
$sql = "SELECT name,cs FROM player natural join batter ORDER BY cs DESC LIMIT 10";
$result = mysql_query($sql);
$i = 1;
while($row = mysql_fetch_array($result)){
	echo $i . $row['name'] . " " .$row['cs'];
	echo "</br>";
	$i = $i+1;
}
echo "</br>SAC</br>";
$sql = "SELECT name,sac FROM player natural join batter ORDER BY sac DESC LIMIT 10";
$result = mysql_query($sql);
$i = 1;
while($row = mysql_fetch_array($result)){
	echo $i . $row['name'] . " " .$row['sac'];
	echo "</br>";
	$i = $i+1;
}
echo "</br>SF</br>";
$sql = "SELECT name,sf FROM player natural join batter ORDER BY sf DESC LIMIT 10";
$result = mysql_query($sql);
$i = 1;
while($row = mysql_fetch_array($result)){
	echo $i . $row['name'] . " " .$row['sf'];
	echo "</br>";
	$i = $i+1;
}
echo "</br>BB</br>";
$sql = "SELECT name,bb FROM player natural join batter ORDER BY bb DESC LIMIT 10";
$result = mysql_query($sql);
$i = 1;
while($row = mysql_fetch_array($result)){
	echo $i . $row['name'] . " " .$row['bb'];
	echo "</br>";
	$i = $i+1;
}
echo "</br>IBB</br>";
$sql = "SELECT name,ibb FROM player natural join batter ORDER BY ibb DESC LIMIT 10";
$result = mysql_query($sql);
$i = 1;
while($row = mysql_fetch_array($result)){
	echo $i . $row['name'] . " " .$row['ibb'];
	echo "</br>";
	$i = $i+1;
}
echo "</br>HBP</br>";
$sql = "SELECT name,hbp FROM player natural join batter ORDER BY hbp DESC LIMIT 10";
$result = mysql_query($sql);
$i = 1;
while($row = mysql_fetch_array($result)){
	echo $i . $row['name'] . " " .$row['hbp'];
	echo "</br>";
	$i = $i+1;
}
echo "</br>SO</br>";
$sql = "SELECT name,so FROM player natural join batter ORDER BY so DESC LIMIT 10";
$result = mysql_query($sql);
$i = 1;
while($row = mysql_fetch_array($result)){
	echo $i . $row['name'] . " " .$row['so'];
	echo "</br>";
	$i = $i+1;
}
echo "</br>GDP</br>";
$sql = "SELECT name,gdp FROM player natural join batter ORDER BY gdp DESC LIMIT 10";
$result = mysql_query($sql);
$i = 1;
while($row = mysql_fetch_array($result)){
	echo $i . $row['name'] . " " .$row['gdp'];
	echo "</br>";
	$i = $i+1;
}
echo "</br>SLG</br>";
$sql = "SELECT name,slg FROM player natural join batter ORDER BY slg DESC LIMIT 10";
$result = mysql_query($sql);
$i = 1;
while($row = mysql_fetch_array($result)){
	echo $i . $row['name'] . " " .$row['slg'];
	echo "</br>";
	$i = $i+1;
}
echo "</br>OBP</br>";
$sql = "SELECT name,obp FROM player natural join batter ORDER BY obp DESC LIMIT 10";
$result = mysql_query($sql);
$i = 1;
while($row = mysql_fetch_array($result)){
	echo $i . $row['name'] . " " .$row['obp'];
	echo "</br>";
	$i = $i+1;
}
echo "</br>ERR</br>";
$sql = "SELECT name,err FROM player natural join batter ORDER BY err DESC LIMIT 10";
$result = mysql_query($sql);
$i = 1;
while($row = mysql_fetch_array($result)){
	echo $i . $row['name'] . " " .$row['err'];
	echo "</br>";
	$i = $i+1;
}
echo "</br>SR</br>";
$sql = "SELECT name,sr FROM player natural join batter ORDER BY sr DESC LIMIT 10";
$result = mysql_query($sql);
$i = 1;
while($row = mysql_fetch_array($result)){
	echo $i . $row['name'] . " " .$row['sr'];
	echo "</br>";
	$i = $i+1;
}
echo "</br>BBK</br>";
$sql = "SELECT name,bbk FROM player natural join batter ORDER BY bbk DESC LIMIT 10";
$result = mysql_query($sql);
$i = 1;
while($row = mysql_fetch_array($result)){
	echo $i . $row['name'] . " " .$row['bbk'];
	echo "</br>";
	$i = $i+1;
}
echo "</br>SLGR</br>";
$sql = "SELECT name,slgr FROM player natural join batter ORDER BY slgr DESC LIMIT 10";
$result = mysql_query($sql);
$i = 1;
while($row = mysql_fetch_array($result)){
	echo $i . $row['name'] . " " .$row['slgr'];
	echo "</br>";
	$i = $i+1;
}
echo "</br>MH</br>";
$sql = "SELECT name,mh FROM player natural join batter ORDER BY mh DESC LIMIT 10";
$result = mysql_query($sql);
$i = 1;
while($row = mysql_fetch_array($result)){
	echo $i . $row['name'] . " " .$row['mh'];
	echo "</br>";
	$i = $i+1;
}
echo "</br>OPS</br>";
$sql = "SELECT name,ops FROM player natural join batter ORDER BY ops DESC LIMIT 10";
$result = mysql_query($sql);
$i = 1;
while($row = mysql_fetch_array($result)){
	echo $i . $row['name'] . " " .$row['ops'];
	echo "</br>";
	$i = $i+1;
}
echo "</br>SAVG</br>";
$sql = "SELECT name,savg FROM player natural join batter ORDER BY savg DESC LIMIT 10";
$result = mysql_query($sql);
$i = 1;
while($row = mysql_fetch_array($result)){
	echo $i . $row['name'] . " " .$row['savg'];
	echo "</br>";
	$i = $i+1;
}
echo "</br>PAVG</br>";
$sql = "SELECT name,pavg FROM player natural join batter ORDER BY pavg DESC LIMIT 10";
$result = mysql_query($sql);
$i = 1;
while($row = mysql_fetch_array($result)){
	echo $i . $row['name'] . " " .$row['pavg'];
	echo "</br>";
	$i = $i+1;
}

mysql_close($con);
?>
</body>
</html>
