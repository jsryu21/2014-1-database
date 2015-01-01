import sys
import datetime
import urllib
from bs4 import BeautifulSoup
import MySQLdb
import operator

def PlayerUrls():
	pitcherUrls = []
	batterUrls = []
	for url in kboPitcherSearchUrls:
		data = urllib.urlopen(url)
		soup = BeautifulSoup(data)
		playerLists = soup.find_all("ul", {"class" : "playerList"})
		for playerList in playerLists:
			for a in playerList.find_all("a"):
				pitcherUrls.append(kboUrl + a["href"])
	for url in kboBatterSearchUrls:
		data = urllib.urlopen(url)
		soup = BeautifulSoup(data)
		playerLists = soup.find_all("ul", {"class" : "playerList"})
		for playerList in playerLists:
			for a in playerList.find_all("a"):
				batterUrls.append(kboUrl + a["href"])
	return (pitcherUrls, batterUrls)

def PlayerCode(playerUrl):
	if isinstance(playerUrl, str):
		i = playerUrl.find("=")
		if i == -1:
			return -1
		else:
			return int(playerUrl[i + 1:])
	else:
		return -1

def PitcherInfo(playerUrl):
	data = urllib.urlopen(playerUrl)
	soup = BeautifulSoup(data)
	playerBox = soup.find_all("div", {"class":"playerBox"})
	lis = playerBox[0].find_all("li")
	player = (PlayerCode(playerUrl)
		, GetStrSndContent(lis[0])
		, unicode("-".join([i[:-1] for i in lis[2].contents[1].strip().split()])).encode("utf-8")
		, int(lis[4].contents[1].split("/")[0].strip()[:-2])
		, int(lis[4].contents[1].split("/")[1].strip()[:-2]))
	playerInfo = (PlayerCode(playerUrl)
		, teams[unicode(playerBox[0].h4.contents[2].strip().split()[0]).encode("utf-8")]
		, int(lis[1].contents[1].strip()[3:])
		, GetStrSndContent(lis[3])
		, GetIntSndContent(lis[7])
		, GetIntSndContent(lis[6])
		, GetStrSndContent(lis[9])
		, GetStrSndContent(lis[5]))
	scores = soup.find_all("table", {"class":"tData"})
	tds = scores[0].find_all("tr")[1].find_all("td")
	tds2 = scores[1].find_all("tr")[1].find_all("td")
	pitcherInfo = () if len(tds) <= 1 or len(tds2) <= 1 else (PlayerCode(playerUrl)
		, teams[unicode(tds[0].contents[0].strip()).encode("utf-8")]
    	, float(tds[1].contents[0].strip())
    	, int(tds[2].contents[0].strip())
    	, int(tds[3].contents[0].strip())
    	, int(tds[4].contents[0].strip())
    	, int(tds[5].contents[0].strip())
    	, int(tds[6].contents[0].strip())
    	, int(tds[7].contents[0].strip())
    	, int(tds[8].contents[0].strip())
    	, float(tds[9].contents[0].strip())
    	, int(tds[10].contents[0].strip())
    	, int(tds[11].contents[0].strip())
    	, float(".".join([i.split("/")[0] for i in tds[12].contents[0].strip().split()]))
    	, int(tds[13].contents[0].strip())
    	, int(tds[14].contents[0].strip())
    	, int(tds[15].contents[0].strip())
    	, int(tds[16].contents[0].strip())
    	, int(tds2[0].contents[0].strip())
    	, int(tds2[1].contents[0].strip())
    	, int(tds2[2].contents[0].strip())
    	, int(tds2[3].contents[0].strip())
    	, int(tds2[4].contents[0].strip())
    	, int(tds2[5].contents[0].strip())
    	, int(tds2[6].contents[0].strip())
    	, int(tds2[7].contents[0].strip())
    	, int(tds2[8].contents[0].strip())
    	, int(tds2[9].contents[0].strip())
    	, int(tds2[10].contents[0].strip())
    	, float(tds2[11].contents[0].strip())
    	, float(tds2[12].contents[0].strip())
    	, int(tds2[13].contents[0].strip()))
	return (player, playerInfo, pitcherInfo)

def GetIntSndContent(li):
	return 0 if len(li.contents) <= 1 else int(li.contents[1].strip()[:-2])

def GetStrSndContent(li):
	return "" if len(li.contents) <= 1 else unicode(li.contents[1].strip()).encode("utf-8")

def DailyPitcherInfo(playerUrl):
	data = urllib.urlopen("http://www.koreabaseball.com/Record/PitcherDetail2.aspx?pcode=" + str(PlayerCode(playerUrl)))
	soup = BeautifulSoup(data)
	scores = soup.find_all("table", {"class":"tData"})
	ret = []
	player_id = PlayerCode(playerUrl)
	for score in scores:
		trs = score.find_all("tr")
		for tr in trs:
			tds = tr.find_all("td")
			if len(tds) > 1:
				ret.append((player_id
				, "2014-" + "-".join(unicode(tds[0].contents[0].strip()).encode("utf-8").split("."))
				, teams[unicode(tds[1].contents[0].strip()).encode("utf-8")]
				, unicode(tds[2].contents[0].strip()).encode("utf-8")
				, float(tds[3].contents[0].strip())
				, unicode(tds[4].contents[0].strip()).encode("utf-8")
				, int(tds[5].contents[0].strip())
				, float(".".join([i.split("/")[0] for i in tds[6].contents[0].strip().split()]))
				, int(tds[7].contents[0].strip())
				, int(tds[8].contents[0].strip())
				, int(tds[9].contents[0].strip())
				, int(tds[10].contents[0].strip())
				, int(tds[11].contents[0].strip())
				, int(tds[12].contents[0].strip())
				, int(tds[13].contents[0].strip())
				, float(tds[14].contents[0].strip())))
	return ret

def BatterInfo(playerUrl):
	data = urllib.urlopen(playerUrl)
	soup = BeautifulSoup(data)
	playerBox = soup.find_all("div", {"class":"playerBox"})
	lis = playerBox[0].find_all("li")
	player = (PlayerCode(playerUrl)
		, GetStrSndContent(lis[0])
		, unicode("-".join([i[:-1] for i in lis[2].contents[1].strip().split()])).encode("utf-8")
		, int(lis[4].contents[1].split("/")[0].strip()[:-2])
		, int(lis[4].contents[1].split("/")[1].strip()[:-2]))
	playerInfo = (PlayerCode(playerUrl)
		, teams[unicode(playerBox[0].h4.contents[2].strip().split()[0]).encode("utf-8")]
		, int(lis[1].contents[1].strip()[3:])
		, GetStrSndContent(lis[3])
		, GetIntSndContent(lis[7])
		, GetIntSndContent(lis[6])
		, GetStrSndContent(lis[9])
		, GetStrSndContent(lis[5]))
	scores = soup.find_all("table", {"class":"tData"})
	tds = scores[0].find_all("tr")[1].find_all("td")
	tds2 = scores[1].find_all("tr")[1].find_all("td")
	batterInfo = () if len(tds) <= 1 or len(tds2) <= 1 else (PlayerCode(playerUrl)
		, teams[unicode(tds[0].contents[0].strip()).encode("utf-8")]
		, float(tds[1].contents[0].strip())
    	, int(tds[2].contents[0].strip())
    	, int(tds[3].contents[0].strip())
    	, int(tds[4].contents[0].strip())
    	, int(tds[5].contents[0].strip())
    	, int(tds[6].contents[0].strip())
    	, int(tds[7].contents[0].strip())
    	, int(tds[8].contents[0].strip())
    	, int(tds[9].contents[0].strip())
    	, int(tds[10].contents[0].strip())
    	, int(tds[11].contents[0].strip())
    	, int(tds[12].contents[0].strip())
    	, int(tds[13].contents[0].strip())
    	, int(tds[14].contents[0].strip())
    	, int(tds[15].contents[0].strip())
    	, int(tds2[0].contents[0].strip())
    	, int(tds2[1].contents[0].strip())
    	, int(tds2[2].contents[0].strip())
    	, int(tds2[3].contents[0].strip())
    	, int(tds2[4].contents[0].strip())
    	, float(tds2[5].contents[0].strip())
    	, float(tds2[6].contents[0].strip())
    	, int(tds2[7].contents[0].strip())
    	, float(tds2[8].contents[0].strip()[:-1].encode("utf-8"))
    	, float(tds2[9].contents[0].strip())
    	, float(tds2[10].contents[0].strip())
    	, int(tds2[11].contents[0].strip())
    	, float(tds2[12].contents[0].strip())
    	, float(tds2[13].contents[0].strip())
		, -1.0 if "-" in tds2[14].contents[0].strip() else float(tds2[14].contents[0].strip())) 
	return (player, playerInfo, batterInfo)

def DailyBatterInfo(playerUrl):
	data = urllib.urlopen("http://www.koreabaseball.com/Record/HitterDetail2.aspx?pcode=" + str(PlayerCode(playerUrl)))
	soup = BeautifulSoup(data)
	scores = soup.find_all("table", {"class":"tData"})
	player_id = PlayerCode(playerUrl)
	ret = []
	for score in scores:
		trs = score.find_all("tr")
		for tr in trs:
			tds = tr.find_all("td")
			if len(tds) > 1:
				ret.append((player_id
				, "2014-" + "-".join(unicode(tds[0].contents[0].strip()).encode("utf-8").split("."))
				, teams[unicode(tds[1].contents[0].strip()).encode("utf-8")]
				, float(tds[2].contents[0].strip())
				, int(tds[3].contents[0].strip())
				, int(tds[4].contents[0].strip())
				, int(tds[5].contents[0].strip())
				, int(tds[6].contents[0].strip())
				, int(tds[7].contents[0].strip())
				, int(tds[8].contents[0].strip())
				, int(tds[9].contents[0].strip())
				, int(tds[10].contents[0].strip())
				, int(tds[11].contents[0].strip())
				, int(tds[12].contents[0].strip())
				, int(tds[13].contents[0].strip())
				, int(tds[14].contents[0].strip())
				, int(tds[15].contents[0].strip())))
	return ret

def Teams():
	data = urllib.urlopen("http://www.koreabaseball.com/TeamRank/TeamRank.aspx?searchDate=2014-04-15")
	soup = BeautifulSoup(data)
	soup = BeautifulSoup(soup.prettify(formatter=None))
	scores = soup.find_all("table", {"class":"tData"})
	teams = {}
	for tr in scores[0].find_all("tr"):
		tds = tr.find_all("td")
		if len(tds) > 1:
			teams[unicode(tds[1].contents[0].strip()).encode("utf-8")] = int(tds[0].contents[0])
	return teams

def InsertTeams(teams):
	sorted_teams = sorted(teams.iteritems(), key=operator.itemgetter(1))
	for sorted_team in sorted_teams:
		cur.execute("SELECT COUNT(1) FROM team WHERE name=%s", sorted_team[0])
		if not cur.fetchone()[0]:
			print "InsertTeam. sorted_team : ", sorted_team
			cur.execute("INSERT INTO team (team_id,name) VALUES(%s, %s)", (sorted_team[1], sorted_team[0]))
	db.commit()

def InsertPlayer(pitcherUrls, batterUrls):
	for pitcherUrl in pitcherUrls:
		print "InsertPlayer. pitcherUrl : ", pitcherUrl
		(player, playerInfo, pitcherInfo) = PitcherInfo(pitcherUrl)
		cur.execute("SELECT COUNT(1) FROM player WHERE player_id=%s", (player[0]))
		if not cur.fetchone()[0]:
			print "InsertPlayer. player: ", player
			cur.execute("INSERT INTO player (player_id,name,birth,height,weight) VALUES(%s, %s, %s, %s, %s)", player)
		cur.execute("SELECT COUNT(1) FROM playerinfo WHERE player_id=%s and team_id=%s and no=%s and pos=%s and sal=%s and dep=%s and year=%s and career=%s", playerInfo)
		if not cur.fetchone()[0]:
			print "InsertPlayer. playerInfo : ", playerInfo
			cur.execute("INSERT INTO playerinfo (player_id,team_id,no,pos,sal,dep,year,career) VALUES(%s, %s, %s, %s, %s, %s, %s, %s)", playerInfo)
		if len(pitcherInfo)>0:
			cur.execute("SELECT COUNT(1) FROM pitcher WHERE player_id=%s and g=%s", (pitcherInfo[0], pitcherInfo[3]))
			if not cur.fetchone()[0]:
				print "InsertPlayer. pitcherInfo : ", pitcherInfo
				cur.execute("INSERT INTO pitcher (player_id,team_id,era,g,sho,cg,w,l,sv,hld,wpct,tbf,np,ip,ah,a2b,a3b,ahr,asac,asf,abb,aibb,ahbp,k,wp,bk,ar,aer,bs,whip,aavg,qs) VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)", pitcherInfo)
	for batterUrl in batterUrls:
		print "InsertPlayer. batterUrl : ", batterUrl
		(player, playerInfo, batterInfo) = BatterInfo(batterUrl)
		cur.execute("SELECT COUNT(1) FROM player WHERE player_id=%s", (player[0]))
		if not cur.fetchone()[0]:
			print "InsertPlayer. player : ", player
			cur.execute("INSERT INTO player (player_id,name,birth,height,weight) VALUES(%s, %s, %s, %s, %s)", player)
		cur.execute("SELECT COUNT(1) FROM playerinfo WHERE player_id=%s and team_id=%s and no=%s and pos=%s and sal=%s and dep=%s and year=%s and career=%s", playerInfo)
		if not cur.fetchone()[0]:
			print "InsertPlayer. playerInfo : ", playerInfo
			cur.execute("INSERT INTO playerinfo (player_id,team_id,no,pos,sal,dep,year,career) VALUES(%s, %s, %s, %s, %s, %s, %s, %s)", playerInfo)
		if len(batterInfo)>0:
			cur.execute("SELECT COUNT(1) FROM batter WHERE player_id=%s and g=%s", (batterInfo[0], batterInfo[3]))
			if not cur.fetchone()[0]:
				print "InsertPlayer. batterInfo : ", batterInfo
				cur.execute("INSERT INTO batter (player_id,team_id,avg,g,pa,ab,r,hit,2b,3b,hr,tb,pbi,sb,cs,sac,sf,bb,ibb,hbp,so,gdp,slg,obp,err,sr,bbk,slgr,mh,ops,savg,pavg) VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)", batterInfo)
	db.commit()

def InsertDailyPlayer(pitcherUrls, batterUrls):
	for pitcherUrl in pitcherUrls:
		print "InsertDailyPlayer. pitcherUrl : ", pitcherUrl
		dailyRecords = DailyPitcherInfo(pitcherUrl)
		for dailyRecord in dailyRecords:
			cur.execute("SELECT COUNT(1) FROM daily_pitcher WHERE player_id=%s and date=%s", (dailyRecord[0], dailyRecord[1]))
			if not cur.fetchone()[0]:
				print "InsertDailyPlayer. dailyRecord : ", dailyRecord
				cur.execute("INSERT INTO daily_pitcher VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)", dailyRecord)
	for batterUrl in batterUrls:
		print "InsertDailyPlayer. batterUrl : ", batterUrl
		dailyRecords = DailyBatterInfo(batterUrl)
		for dailyRecord in dailyRecords:
			cur.execute("SELECT COUNT(1) FROM daily_batter WHERE player_id=%s and date=%s", (dailyRecord[0], dailyRecord[1]))
			if not cur.fetchone()[0]:
				print "InsertDailyPlayer. dailyRecord : ", dailyRecord
				cur.execute("INSERT INTO daily_batter VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)", dailyRecord)
	db.commit()

oneDay = datetime.timedelta(days = 1)
kboUrl = "http://www.koreabaseball.com"
kboGameListUrl = "http://www.koreabaseball.com/GameCast/GameList.aspx?searchDate="
kboPitcherSearchUrls = ["http://www.koreabaseball.com/Record/PlayerSearch.aspx?position=%ED%88%AC"]
kboBatterSearchUrls = ["http://www.koreabaseball.com/Record/PlayerSearch.aspx?position=%ED%8F%AC"
	, "http://www.koreabaseball.com/Record/PlayerSearch.aspx?position=%EB%82%B4"
	, "http://www.koreabaseball.com/Record/PlayerSearch.aspx?position=%EC%99%B8"]
teams = Teams()
db = MySQLdb.connect(db="dbproject", user="root", passwd="asdf1234", use_unicode=True, charset="utf8")
cur = db.cursor()

if __name__ == "__main__":
	InsertTeams(teams)
	(pitcherUrls, batterUrls) = PlayerUrls()
	InsertPlayer(pitcherUrls, batterUrls)
	InsertDailyPlayer(pitcherUrls, batterUrls)
