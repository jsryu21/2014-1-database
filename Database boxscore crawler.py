# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <codecell>

import sys
import datetime
import urllib
from bs4 import BeautifulSoup

oneDay = datetime.timedelta(days = 1)
kboUrl = "http://www.koreabaseball.com"
kboGameListUrl = "http://www.koreabaseball.com/GameCast/GameList.aspx?searchDate="
kboPitcherSearchUrls = ['http://www.koreabaseball.com/Record/PlayerSearch.aspx?position=%ED%88%AC']
kboBatterSearchUrls = ['http://www.koreabaseball.com/Record/PlayerSearch.aspx?position=%ED%8F%AC'
, 'http://www.koreabaseball.com/Record/PlayerSearch.aspx?position=%EB%82%B4'
, 'http://www.koreabaseball.com/Record/PlayerSearch.aspx?position=%EC%99%B8']

def Dates(dates):
    del dates[:]
    startDate = datetime.date(2014, 3, 29)
    endDate = datetime.date.today()
    while startDate != endDate:
        dates.append(startDate)
        startDate += oneDay

def BoxScoreUrls(boxScoreUrls, date = ''):
    del boxScoreUrls[:]
    if not date:
        d = datetime.date.today()
        d -= oneDay
    else:
        d = datetime.datetime.strptime(date, '%Y-%m-%d')
    data = urllib.urlopen(kboGameListUrl + str(d))
    soup = BeautifulSoup(data)
    btns = soup.findAll("div", {"class" : "btnSms"})
    for btn in btns:
        link = btn.find_all('a')[1]['href']
        boxScoreUrls.append(kboUrl + link)

def PlayerUrls(pitcherUrls, batterUrls):
    del pitcherUrls[:]
    del batterUrls[:]
    for url in kboPitcherSearchUrls:
        data = urllib.urlopen(url)
        soup = BeautifulSoup(data)
        playerLists = soup.findAll("ul", {"class" : "playerList"})
        for playerList in playerLists:
            for a in playerList.findAll("a"):
                pitcherUrls.append(kboUrl + a['href'])
    for url in kboBatterSearchUrls:
        data = urllib.urlopen(url)
        soup = BeautifulSoup(data)
        playerLists = soup.findAll("ul", {"class" : "playerList"})
        for playerList in playerLists:
            for a in playerList.findAll("a"):
                batterUrls.append(kboUrl + a['href'])

# <codecell>

pitcherUrls = []
batterUrls = []
PlayerUrls(pitcherUrls, batterUrls)

# <codecell>

data = urllib.urlopen('http://www.koreabaseball.com/Record/PitcherDetail1.aspx?pcode=79229')
soup = BeautifulSoup(data)
img = soup.findAll('span', {'class':'photo'})[0].img
print kboUrl + img['src']
playerBox = soup.findAll('div', {'class':'playerBox'})
ls = playerBox[0].findAll('li')
print ls[0].contents[1].strip()
print ls[2].contents[1].strip()
print ls[4].contents[1].split('/')[0].strip()[:-2]
print ls[4].contents[1].split('/')[1].strip()[:-2]
print playerBox[0].h4.contents[2].strip()
print ls[1].contents[1].strip()[3:]
print ls[3].contents[1].strip()
print ls[7].contents[1].strip()[:-2]
print ls[6].contents[1].strip()[:-2]
print ls[9].contents[1].strip()
print ls[5].contents[1].strip()

# <codecell>

score = soup.findAll('table', {'class':'tData'})
tds = score[0].find_all('tr')[1].find_all('td')
tds2 = score[1].find_all('tr')[1].find_all('td')
if len(tds) > 1 and len(tds2) > 1:
    print tds[0].contents[0].strip()
    print tds[1].contents[0].strip()
    print tds[2].contents[0].strip()
    print tds[3].contents[0].strip()
    print tds[4].contents[0].strip()
    print tds[5].contents[0].strip()
    print tds[6].contents[0].strip()
    print tds[7].contents[0].strip()
    print tds[8].contents[0].strip()
    print tds[9].contents[0].strip()
    print tds[10].contents[0].strip()
    print tds[11].contents[0].strip()
    print tds[12].contents[0].strip()
    print tds[13].contents[0].strip()
    print tds[14].contents[0].strip()
    print tds[15].contents[0].strip()
    print tds[16].contents[0].strip()
    print tds2[0].contents[0].strip()
    print tds2[1].contents[0].strip()
    print tds2[2].contents[0].strip()
    print tds2[3].contents[0].strip()
    print tds2[4].contents[0].strip()
    print tds2[5].contents[0].strip()
    print tds2[6].contents[0].strip()
    print tds2[7].contents[0].strip()
    print tds2[8].contents[0].strip()
    print tds2[9].contents[0].strip()
    print tds2[10].contents[0].strip()
    print tds2[11].contents[0].strip()
    print tds2[12].contents[0].strip()
    print tds2[13].contents[0].strip()

# <codecell>

data = urllib.urlopen('http://www.koreabaseball.com/Record/PitcherDetail2.aspx?pcode=79229')
soup = BeautifulSoup(data)
scores = soup.findAll('table', {'class':'tData'})
for score in scores:
    trs = score.find_all('tr')
    for tr in trs:
        tds = tr.find_all('td')
        if len(tds) > 1:
            print tds[0].contents[0].strip()
            print tds[1].contents[0].strip()
            print tds[2].contents[0].strip()
            print tds[3].contents[0].strip()
            print tds[4].contents[0].strip()
            print tds[5].contents[0].strip()
            print tds[6].contents[0].strip()
            print tds[7].contents[0].strip()
            print tds[8].contents[0].strip()
            print tds[9].contents[0].strip()
            print tds[10].contents[0].strip()
            print tds[11].contents[0].strip()
            print tds[12].contents[0].strip()
            print tds[13].contents[0].strip()
            print tds[14].contents[0].strip()

# <codecell>

data = urllib.urlopen('http://www.koreabaseball.com/Record/HitterDetail1.aspx?pcode=74540')
soup = BeautifulSoup(data)
img = soup.findAll('span', {'class':'photo'})[0].img
print kboUrl + img['src']
playerBox = soup.findAll('div', {'class':'playerBox'})
ls = playerBox[0].findAll('li')
print ls[0].contents[1].strip()
print ls[2].contents[1].strip()
print ls[4].contents[1].split('/')[0].strip()
print ls[4].contents[1].split('/')[1].strip()
print playerBox[0].h4.contents[2].strip()
print ls[1].contents[1].strip()
print ls[3].contents[1].strip()
print ls[7].contents[1].strip()
print ls[6].contents[1].strip()
print ls[9].contents[1].strip()
print ls[5].contents[1].strip()

# <codecell>

data = urllib.urlopen('http://www.koreabaseball.com/Record/HitterDetail1.aspx?pcode=74540')
soup = BeautifulSoup(data)
score = soup.findAll('table', {'class':'tData'})
tds = score[0].find_all('tr')[1].find_all('td')
tds2 = score[1].find_all('tr')[1].find_all('td')
if len(tds) > 1 and len(tds2) > 1:
    print tds[0].contents[0].strip()
    print tds[1].contents[0].strip()
    print tds[2].contents[0].strip()
    print tds[3].contents[0].strip()
    print tds[4].contents[0].strip()
    print tds[5].contents[0].strip()
    print tds[6].contents[0].strip()
    print tds[7].contents[0].strip()
    print tds[8].contents[0].strip()
    print tds[9].contents[0].strip()
    print tds[10].contents[0].strip()
    print tds[11].contents[0].strip()
    print tds[12].contents[0].strip()
    print tds[13].contents[0].strip()
    print tds[14].contents[0].strip()
    print tds[15].contents[0].strip()
    print tds2[0].contents[0].strip()
    print tds2[1].contents[0].strip()
    print tds2[2].contents[0].strip()
    print tds2[3].contents[0].strip()
    print tds2[4].contents[0].strip()
    print tds2[5].contents[0].strip()
    print tds2[6].contents[0].strip()
    print tds2[7].contents[0].strip()
    print tds2[8].contents[0].strip()
    print tds2[9].contents[0].strip()
    print tds2[10].contents[0].strip()
    print tds2[11].contents[0].strip()
    print tds2[12].contents[0].strip()
    print tds2[13].contents[0].strip()
    print tds2[14].contents[0].strip()

# <codecell>

data = urllib.urlopen('http://www.koreabaseball.com/Record/HitterDetail2.aspx?pcode=74540')
soup = BeautifulSoup(data)
scores = soup.findAll('table', {'class':'tData'})
for score in scores:
    trs = score.find_all('tr')
    for tr in trs:
        tds = tr.find_all('td')
        if len(tds) > 1:
            print tds[0].contents[0].strip()
            print tds[1].contents[0].strip()
            print tds[2].contents[0].strip()
            print tds[3].contents[0].strip()
            print tds[4].contents[0].strip()
            print tds[5].contents[0].strip()
            print tds[6].contents[0].strip()
            print tds[7].contents[0].strip()
            print tds[8].contents[0].strip()
            print tds[9].contents[0].strip()
            print tds[10].contents[0].strip()
            print tds[11].contents[0].strip()
            print tds[12].contents[0].strip()
            print tds[13].contents[0].strip()
            print tds[14].contents[0].strip()
            print tds[15].contents[0].strip()

# <codecell>

data = urllib.urlopen('http://www.koreabaseball.com/TeamRank/TeamRank.aspx')
soup = BeautifulSoup(data)
scores = soup.findAll('table', {'class':'tData'})
teams = []
for tr in scores[0].find_all('tr'):
    tds = tr.find_all('td')
    if len(tds) > 1:
        teams.append(tds[1].contents[0])
print teams

# <codecell>


# <codecell>


# <codecell>


# <codecell>


# <codecell>


# <codecell>


# <codecell>


