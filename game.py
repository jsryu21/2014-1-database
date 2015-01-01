import sys
import datetime
import urllib
from bs4 import BeautifulSoup
import MySQLdb
import operator
import unicodedata

def Dates():
	dates = []
	startDate = datetime.date(2014, 3, 29)
	endDate = datetime.date.today()
	while startDate < endDate:
		dates.append(startDate)
		startDate += oneDay
	return dates

def BoxScoreUrls(date = ''):
	boxScoreUrls = []
	if not date:
		d = datetime.date.today()
		d -= oneDay
	else:
		d = datetime.datetime.strptime(date, '%Y-%m-%d')
	data = urllib.urlopen(kboGameListUrl + str(d))
	soup = BeautifulSoup(data)
	btns = soup.find_all("div", {"class" : "btnSms"})
	for btn in btns:
		link = btn.find_all('a')[1]['href']
		boxScoreUrls.append(kboUrl + link)
	return boxScoreUrls

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

def GameKey(boxScoreUrl):
	if isinstance(boxScoreUrl, str):
		i = boxScoreUrl.find("?gmkey=")
		if i == -1:
			return ""
		else:
			j = boxScoreUrl[i + 1:].find("&dryear=")
			if j == -1:
				return ""
			else:
				return unicode(boxScoreUrl[i + 7:i + j + 1]).encode("utf-8")
	else:
		return ""

def BoxScore(boxScoreUrl):
	data = urllib.urlopen(boxScoreUrl)
	gameKey = GameKey(boxScoreUrl)
	soup = BeautifulSoup(data)
	awayHitterTable = soup.find_all("table", {"id":"xtable1"})[0]
	homeHitterTable = soup.find_all("table", {"id":"xtable2"})[0]
	awayPitcherTable = soup.find_all("table", {"id":"xtable3"})[0]
	homePitcherTable = soup.find_all("table", {"id":"xtable4"})[0]
	hitterScores = []
	pitcherScores = []
	h4s = soup.find_all("div", {"class":"boxScore"})[0].find_all("h4")
	trs = awayHitterTable.find_all("tbody")[0].find_all("tr")
	for tr in trs:
		ths = tr.find_all("th")
		tds = tr.find_all("td")
		hitterScores.append((
			gameKey	
			, teams[unicode(h4s[0].contents[0].split()[0]).encode("utf-8")]
			, int(ths[0].contents[0].strip())
			, unicode(ths[1].contents[0].strip()).encode("utf-8")
			, unicode(ths[2].contents[0].strip()).encode("utf-8")
			, "" if tds[0].contents[0].strip() == "&nbsp" else unicode(tds[0].contents[0].strip()).encode("utf-8")
			, "" if tds[1].contents[0].strip() == "&nbsp" else unicode(tds[1].contents[0].strip()).encode("utf-8")
			, "" if tds[2].contents[0].strip() == "&nbsp" else unicode(tds[2].contents[0].strip()).encode("utf-8")
			, "" if tds[3].contents[0].strip() == "&nbsp" else unicode(tds[3].contents[0].strip()).encode("utf-8")
			, "" if tds[4].contents[0].strip() == "&nbsp" else unicode(tds[4].contents[0].strip()).encode("utf-8")
			, "" if tds[5].contents[0].strip() == "&nbsp" else unicode(tds[5].contents[0].strip()).encode("utf-8")
			, "" if tds[6].contents[0].strip() == "&nbsp" else unicode(tds[6].contents[0].strip()).encode("utf-8")
			, "" if tds[7].contents[0].strip() == "&nbsp" else unicode(tds[7].contents[0].strip()).encode("utf-8")
			, "" if tds[8].contents[0].strip() == "&nbsp" else unicode(tds[8].contents[0].strip()).encode("utf-8")
			, "" if tds[9].contents[0].strip() == "&nbsp" else unicode(tds[9].contents[0].strip()).encode("utf-8")
			, "" if tds[10].contents[0].strip() == "&nbsp" else unicode(tds[10].contents[0].strip()).encode("utf-8")
			, "" if tds[11].contents[0].strip() == "&nbsp" else unicode(tds[11].contents[0].strip()).encode("utf-8")
			, "" if tds[12].contents[0].strip() == "&nbsp" else unicode(tds[12].contents[0].strip()).encode("utf-8")
			, "" if tds[13].contents[0].strip() == "&nbsp" else unicode(tds[13].contents[0].strip()).encode("utf-8")
			, "" if tds[14].contents[0].strip() == "&nbsp" else unicode(tds[14].contents[0].strip()).encode("utf-8")
			, int(tds[15].contents[0].strip())
			, int(tds[16].contents[0].strip())
			, int(tds[17].contents[0].strip())
			, int(tds[18].contents[0].strip())
			, float(tds[19].contents[0].strip())
		))
	trs = homeHitterTable.find_all("tbody")[0].find_all("tr")
	for tr in trs:
		ths = tr.find_all("th")
		tds = tr.find_all("td")
		hitterScores.append((
			gameKey	
			, teams[unicode(h4s[1].contents[0].split()[0]).encode("utf-8")]
			, int(ths[0].contents[0].strip())
			, unicode(ths[1].contents[0].strip()).encode("utf-8")
			, unicode(ths[2].contents[0].strip()).encode("utf-8")
			, "" if tds[0].contents[0].strip() == "&nbsp" else unicode(tds[0].contents[0].strip()).encode("utf-8")
			, "" if tds[1].contents[0].strip() == "&nbsp" else unicode(tds[1].contents[0].strip()).encode("utf-8")
			, "" if tds[2].contents[0].strip() == "&nbsp" else unicode(tds[2].contents[0].strip()).encode("utf-8")
			, "" if tds[3].contents[0].strip() == "&nbsp" else unicode(tds[3].contents[0].strip()).encode("utf-8")
			, "" if tds[4].contents[0].strip() == "&nbsp" else unicode(tds[4].contents[0].strip()).encode("utf-8")
			, "" if tds[5].contents[0].strip() == "&nbsp" else unicode(tds[5].contents[0].strip()).encode("utf-8")
			, "" if tds[6].contents[0].strip() == "&nbsp" else unicode(tds[6].contents[0].strip()).encode("utf-8")
			, "" if tds[7].contents[0].strip() == "&nbsp" else unicode(tds[7].contents[0].strip()).encode("utf-8")
			, "" if tds[8].contents[0].strip() == "&nbsp" else unicode(tds[8].contents[0].strip()).encode("utf-8")
			, "" if tds[9].contents[0].strip() == "&nbsp" else unicode(tds[9].contents[0].strip()).encode("utf-8")
			, "" if tds[10].contents[0].strip() == "&nbsp" else unicode(tds[10].contents[0].strip()).encode("utf-8")
			, "" if tds[11].contents[0].strip() == "&nbsp" else unicode(tds[11].contents[0].strip()).encode("utf-8")
			, "" if tds[12].contents[0].strip() == "&nbsp" else unicode(tds[12].contents[0].strip()).encode("utf-8")
			, "" if tds[13].contents[0].strip() == "&nbsp" else unicode(tds[13].contents[0].strip()).encode("utf-8")
			, "" if tds[14].contents[0].strip() == "&nbsp" else unicode(tds[14].contents[0].strip()).encode("utf-8")
			, int(tds[15].contents[0].strip())
			, int(tds[16].contents[0].strip())
			, int(tds[17].contents[0].strip())
			, int(tds[18].contents[0].strip())
			, float(tds[19].contents[0].strip())
		))
	trs = awayPitcherTable.find_all("tbody")[0].find_all("tr")
	for tr in trs:
		ths = tr.find_all("th")
		tds = tr.find_all("td")
		pitcherScores.append((
			gameKey
			, teams[unicode(h4s[2].contents[0].split()[0]).encode("utf-8")]
			, unicode(ths[0].contents[0].strip()).encode("utf-8")
			, "" if tds[0].contents[0].strip() == "&nbsp" else unicode(tds[0].contents[0].strip()).encode("utf-8")
			, "" if tds[1].contents[0].strip() == "&nbsp" else unicode(tds[1].contents[0].strip()).encode("utf-8")
			, int(tds[2].contents[0].strip())
			, int(tds[3].contents[0].strip())
			, int(tds[4].contents[0].strip())
			, sum([float(i) if i.isdigit() else unicodedata.numeric(i) for i in tds[5].contents[0].strip().split()])
			, int(tds[6].contents[0].strip())
			, int(tds[7].contents[0].strip())
			, int(tds[8].contents[0].strip())
			, int(tds[9].contents[0].strip())
			, int(tds[10].contents[0].strip())
			, int(tds[11].contents[0].strip())
			, int(tds[12].contents[0].strip())
			, int(tds[13].contents[0].strip())
			, int(tds[14].contents[0].strip())
			, float(tds[15].contents[0].strip())
		))
	trs = homePitcherTable.find_all("tbody")[0].find_all("tr")
	for tr in trs:
		ths = tr.find_all("th")
		tds = tr.find_all("td")
		pitcherScores.append((
			gameKey
			, teams[unicode(h4s[3].contents[0].split()[0]).encode("utf-8")]
			, unicode(ths[0].contents[0].strip()).encode("utf-8")
			, "" if tds[0].contents[0].strip() == "&nbsp" else unicode(tds[0].contents[0].strip()).encode("utf-8")
			, "" if tds[1].contents[0].strip() == "&nbsp" else unicode(tds[1].contents[0].strip()).encode("utf-8")
			, int(tds[2].contents[0].strip())
			, int(tds[3].contents[0].strip())
			, int(tds[4].contents[0].strip())
			, sum([float(i) if i.isdigit() else unicodedata.numeric(i) for i in tds[5].contents[0].strip().split()])
			, int(tds[6].contents[0].strip())
			, int(tds[7].contents[0].strip())
			, int(tds[8].contents[0].strip())
			, int(tds[9].contents[0].strip())
			, int(tds[10].contents[0].strip())
			, int(tds[11].contents[0].strip())
			, int(tds[12].contents[0].strip())
			, int(tds[13].contents[0].strip())
			, int(tds[14].contents[0].strip())
			, float(tds[15].contents[0].strip())
		))
	return (hitterScores, pitcherScores)

def InsertBoxScores():
	for date in dates:
		boxScoreUrls = BoxScoreUrls(str(date))
		for boxScoreUrl in boxScoreUrls:
			print "InsertBoxScores. boxScoreUrl : ", boxScoreUrl
			(hitterScores, pitcherScores) = BoxScore(boxScoreUrl)
			for hitterScore in hitterScores:
				cur.execute("SELECT COUNT(1) FROM boxscore_hitter WHERE gamekey=%s AND team_id=%s AND lineup=%s AND pos=%s AND name=%s AND i1=%s AND i2=%s AND i3=%s AND i4=%s AND i5=%s AND i6=%s AND i7=%s AND i8=%s AND i9=%s AND i10=%s AND i11=%s AND i12=%s AND i13=%s AND i14=%s AND i15=%s AND ab=%s AND hit=%s AND rbi=%s AND r=%s", hitterScore[:-1])
				if not cur.fetchone()[0]:
					print "InsertBoxScores. hitterScore : ", hitterScore
					cur.execute("INSERT INTO boxscore_hitter (gamekey,team_id,lineup,pos,name,i1,i2,i3,i4,i5,i6,i7,i8,i9,i10,i11,i12,i13,i14,i15,ab,hit,rbi,r,avg) VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)", hitterScore)
			for pitcherScore in pitcherScores:
				cur.execute("SELECT COUNT(1) FROM boxscore_pitcher WHERE gamekey=%s AND team_id=%s AND name=%s AND pos=%s AND result=%s AND w=%s AND l=%s AND sv=%s AND tbf=%s AND np=%s AND aab=%s AND ah=%s AND ahr=%s AND bbibbhbp=%s AND k=%s AND ar=%s AND aer=%s", pitcherScore[:8] + pitcherScore[9:-1])
				if not cur.fetchone()[0]:
					print "InsertBoxScores. pitcherScore : ", pitcherScore
					cur.execute("INSERT INTO boxscore_pitcher (gamekey,team_id,name,pos,result,w,l,sv,ip,tbf,np,aab,ah,ahr,bbibbhbp,k,ar,aer,era) VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)", pitcherScore)
	db.commit()

oneDay = datetime.timedelta(days = 1)
kboUrl = "http://www.koreabaseball.com"
kboGameListUrl = "http://www.koreabaseball.com/GameCast/GameList.aspx?searchDate="
teams = Teams()
dates = Dates()
db = MySQLdb.connect(db="dbproject", user="root", passwd="asdf1234", use_unicode=True, charset="utf8")
cur = db.cursor()

if __name__ == "__main__":
	InsertBoxScores()
