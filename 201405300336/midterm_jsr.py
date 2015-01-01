import sys
import datetime
import urllib
from bs4 import BeautifulSoup
import MySQLdb
import operator

def Dates():
	dates = []
	startDate = datetime.date(2014, 3, 29)
	endDate = datetime.date.today()
	while startDate != endDate:
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

def PlayerUrls():
	pitcherUrls = []
	batterUrls = []
	for url in kboPitcherSearchUrls:
		data = urllib.urlopen(url)
		soup = BeautifulSoup(data)
		playerLists = soup.find_all("ul", {"class" : "playerList"})
		for playerList in playerLists:
			for a in playerList.find_all("a"):
				pitcherUrls.append(kboUrl + a['href'])
	for url in kboBatterSearchUrls:
		data = urllib.urlopen(url)
		soup = BeautifulSoup(data)
		playerLists = soup.find_all("ul", {"class" : "playerList"})
		for playerList in playerLists:
			for a in playerList.find_all("a"):
				batterUrls.append(kboUrl + a['href'])
	return (pitcherUrls, batterUrls)

def PlayerCode(playerUrl):
	return playerUrl.split('=')[1]

def PitcherInfo(playerUrl):
	data = urllib.urlopen(playerUrl)
	soup = BeautifulSoup(data)
	playerBox = soup.find_all('div', {'class':'playerBox'})
	lis = playerBox[0].find_all('li')
	scores = soup.find_all('table', {'class':'tData'})
	tds = scores[0].find_all('tr')[1].find_all('td')
	tds2 = scores[1].find_all('tr')[1].find_all('td')
	if len(tds) > 1 and len(tds2) > 1:
		return (lis[0].contents[1].strip()
		, '-'.join([i[:-1] for i in lis[2].contents[1].strip().split()])
		, int(lis[4].contents[1].split('/')[0].strip()[:-2])
		, int(lis[4].contents[1].split('/')[1].strip()[:-2])
		, playerUrl
		, teams[playerBox[0].h4.contents[2].strip().split()[0]]
		, int(lis[1].contents[1].strip()[3:])
		, lis[3].contents[1].strip()
		, int(lis[7].contents[1].strip()[:-2])
		, int(lis[6].contents[1].strip()[:-2])
		, lis[9].contents[1].strip()
		, lis[5].contents[1].strip()
    	, teams[tds[0].contents[0].strip()]
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
    	, float('.'.join([i.split('/')[0] for i in tds[12].contents[0].strip().split()]))
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
	else:
		return (lis[0].contents[1].strip()
		, '-'.join([i[:-1] for i in lis[2].contents[1].strip().split()])
		, int(lis[4].contents[1].split('/')[0].strip()[:-2])
		, int(lis[4].contents[1].split('/')[1].strip()[:-2])
		, playerUrl
		, teams[playerBox[0].h4.contents[2].strip().split()[0]]
		, int(lis[1].contents[1].strip()[3:])
		, lis[3].contents[1].strip()
		, int(lis[7].contents[1].strip()[:-2])
		, int(lis[6].contents[1].strip()[:-2])
		, lis[9].contents[1].strip()
		, lis[5].contents[1].strip())

def DailyPitcherInfo(playerUrl):
	data = urllib.urlopen('http://www.koreabaseball.com/Record/PitcherDetail2.aspx?pcode=' + PlayerCode(playerUrl))
	soup = BeautifulSoup(data)
	scores = soup.find_all('table', {'class':'tData'})
	ret = []
	for score in scores:
		trs = score.find_all('tr')
		for tr in trs:
			tds = tr.find_all('td')
			if len(tds) > 1:
				ret.append(('2014-' + '-'.join(tds[0].contents[0].strip().split('.'))
				, teams[tds[1].contents[0].strip()]
				, tds[2].contents[0].strip()
				, float(tds[3].contents[0].strip())
				, tds[4].contents[0].strip()
				, int(tds[5].contents[0].strip())
				, float('.'.join([i.split('/')[0] for i in tds[6].contents[0].strip().split()]))
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
	playerBox = soup.find_all('div', {'class':'playerBox'})
	lis = playerBox[0].find_all('li')
	scores = soup.find_all('table', {'class':'tData'})
	tds = scores[0].find_all('tr')[1].find_all('td')
	tds2 = scores[1].find_all('tr')[1].find_all('td')
	if len(tds) > 1 and len(tds2) > 1:
		return (lis[0].contents[1].strip()
		, '-'.join([i[:-1] for i in lis[2].contents[1].strip().split()])
		, int(lis[4].contents[1].split('/')[0].strip()[:-2])
		, int(lis[4].contents[1].split('/')[1].strip()[:-2])
		, playerUrl
		, teams[playerBox[0].h4.contents[2].strip().split()[0]]
		, int(lis[1].contents[1].strip()[3:])
		, lis[3].contents[1].strip()
		, int(lis[7].contents[1].strip()[:-2])
		, int(lis[6].contents[1].strip()[:-2])
		, lis[9].contents[1].strip()
		, lis[5].contents[1].strip()
    	, teams[tds[0].contents[0].strip()]
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
    	, float(tds2[8].contents[0].strip()[:-1])
    	, float(tds2[9].contents[0].strip())
    	, float(tds2[10].contents[0].strip())
    	, int(tds2[11].contents[0].strip())
    	, float(tds2[12].contents[0].strip())
    	, float(tds2[13].contents[0].strip())
		, 0.0 if '-' in tds2[14].contents[0].strip() else float(tds2[14].contents[0].strip())) 
	else:
		return (lis[0].contents[1].strip()
		, '-'.join([i[:-1] for i in lis[2].contents[1].strip().split()])
		, int(lis[4].contents[1].split('/')[0].strip()[:-2])
		, int(lis[4].contents[1].split('/')[1].strip()[:-2])
		, playerUrl
		, teams[playerBox[0].h4.contents[2].strip().split()[0]]
		, int(lis[1].contents[1].strip()[3:])
		, lis[3].contents[1].strip()
		, int(lis[7].contents[1].strip()[:-2])
		, int(lis[6].contents[1].strip()[:-2])
		, lis[9].contents[1].strip()
		, lis[5].contents[1].strip())

def DailyBatterInfo(playerUrl):
	data = urllib.urlopen('http://www.koreabaseball.com/Record/HitterDetail2.aspx?pcode=' + PlayerCode(playerUrl))
	soup = BeautifulSoup(data)
	scores = soup.find_all('table', {'class':'tData'})
	ret = []
	for score in scores:
		trs = score.find_all('tr')
		for tr in trs:
			tds = tr.find_all('td')
			if len(tds) > 1:
				ret.append(('2014-' + '-'.join(tds[0].contents[0].strip().split('.'))
				, teams[tds[1].contents[0].strip()]
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
	data = urllib.urlopen('http://www.koreabaseball.com/TeamRank/TeamRank.aspx?searchDate=2014-04-15')
	soup = BeautifulSoup(data)
	soup = BeautifulSoup(soup.prettify(formatter=None))
	scores = soup.find_all('table', {'class':'tData'})
	teams = {}
	for tr in scores[0].find_all('tr'):
		tds = tr.find_all('td')
		if len(tds) > 1:
			teams[tds[1].contents[0]] = int(tds[0].contents[0])
	return teams

def InsertTeams(teams):
	sorted_teams = sorted(teams.iteritems(), key=operator.itemgetter(1))
	sorted_team_names = [i[0] for i in sorted_teams]
	for team_name in sorted_team_names:
		cur.execute("INSERT INTO team(name) VALUES (%s)", unicode(team_name))
		print unicode(team_name)
		print type(unicode(team_name))

oneDay = datetime.timedelta(days = 1)
kboUrl = "http://www.koreabaseball.com"
kboGameListUrl = "http://www.koreabaseball.com/GameCast/GameList.aspx?searchDate="
kboPitcherSearchUrls = ['http://www.koreabaseball.com/Record/PlayerSearch.aspx?position=%ED%88%AC']
kboBatterSearchUrls = ['http://www.koreabaseball.com/Record/PlayerSearch.aspx?position=%ED%8F%AC'
, 'http://www.koreabaseball.com/Record/PlayerSearch.aspx?position=%EB%82%B4'
, 'http://www.koreabaseball.com/Record/PlayerSearch.aspx?position=%EC%99%B8']
teams = Teams()
db = MySQLdb.connect(db='dbproject', user='root', passwd='asdf1234', use_unicode=True, charset='utf8')
cur = db.cursor()

if __name__ == "__main__":
	'''
	dates = Dates()
	for date in dates:
		boxScoreUrls = BoxScoreUrls(str(date))
		print boxScoreUrls
	(pitcherUrls, batterUrls) = PlayerUrls()
	print PitcherInfo(pitcherUrls[0])[5]
	print DailyPitcherInfo(pitcherUrls[0])
	print BatterInfo(batterUrls[0])[5]
	print DailyBatterInfo(batterUrls[0])
	'''
	print teams
	InsertTeams(teams)
