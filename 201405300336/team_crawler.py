#!/usr/bin/env python
from urllib import urlopen
from bs4 import BeautifulSoup

def Teams():
	data = urlopen("http://www.koreabaseball.com/TeamRank/TeamRank.aspx?searchDate=2014-04-15")
	soup = BeautifulSoup(data)
	soup = BeautifulSoup(soup.prettify(formatter=None))
	scores = soup.find_all("table", {"class":"tData"})
	teams = {}
	for tr in scores[0].find_all("tr"):
		tds = tr.find_all("td")
		if len(tds) > 1:
			teams[unicode(tds[1].contents[0].strip()).encode("utf-8")] = int(tds[0].contents[0])
	return teams

def TeamRanks(date, teams):
	data = urlopen("http://www.koreabaseball.com/TeamRank/TeamRank.aspx?searchDate=" + str(date))
	soup = BeautifulSoup(data)
	soup = BeautifulSoup(soup.prettify(formatter=None))
	scores = soup.find_all("table", {"class":"tData"})
	teamRanks = []
	for tr in scores[0].find_all("tr"):
		tds = tr.find_all("td")
		if len(tds) > 1:
			teamRanks.append((
				teams[unicode(tds[1].contents[0].strip()).encode("utf-8")]
				, 0.0
				, int(tds[2].contents[0].strip())
				, 0
				, 0
				, int(tds[3].contents[0].strip())
				, int(tds[4].contents[0].strip())
				, 0
				, 0
				, float(tds[6].contents[0].strip())
				, 0
				, 0
				, 0.0
				, 0
				, 0
				, 0
				, 0
				, 0
				, 0
				, 0
				, 0
				, 0
				, 0
				, 0
				, 0
				, 0
				, 0
				, 0
				, 0.0
				, 0.0
				, 0
				, 0.0
				, 0
				, 0
				, 0
				, 0
				, 0
				, 0
				, 0
				, 0
				, 0
				, 0
				, 0
				, 0
				, 0
				, 0
				, 0
				, 0
				, 0
				, 0
				, float(tds[10].contents[0].strip())
				, float(tds[9].contents[0].strip())
				, 0
				, 0.0
				, 0.0
				, 0.0
				, 0
				, 0.0
				, 0.0
				, 0.0
				, int(tds[0].contents[0].strip())
				, int(tds[5].contents[0].strip())
				, 0.0 if tds[7].contents[0].strip() == "-" else float(tds[7].contents[0].strip())
				, unicode(tds[8].contents[0].strip()).encode("utf-8")
				))
	return teamRanks

def TeamRecords(teams):
	data = urlopen("http://www.koreabaseball.com/Record/TeamRecord.aspx")
	soup = BeautifulSoup(data)
	pitcher1 = soup.find_all("div", {"id":"pitcher1"})[0].find_all("tr")
	pitcher2 = soup.find_all("div", {"id":"pitcher2"})[0].find_all("tr")
	hitter1 = soup.find_all("div", {"id":"hitter1"})[0].find_all("tr")
	hitter2 = soup.find_all("div", {"id":"hitter2"})[0].find_all("tr")
	teamRecords = []
	for i in xrange(len(pitcher1)):
		pit1Tds = pitcher1[i].find_all("td")
		pit2Tds = pitcher2[i].find_all("td")
		hit1Tds = hitter1[i].find_all("td")
		hit2Tds = hitter2[i].find_all("td")
		if len(pit1Tds) > 1 and teams.__contains__(unicode(pit1Tds[0].contents[0].strip()).encode("utf-8")):
			teamRecords.append((
				teams[unicode(pit1Tds[0].contents[0].strip()).encode("utf-8")]
				, float(pit1Tds[1].contents[0].strip())
				, int(pit1Tds[2].contents[0].strip())
				, int(pit1Tds[3].contents[0].strip())
				, int(pit1Tds[4].contents[0].strip())
				, int(pit1Tds[5].contents[0].strip())
				, int(pit1Tds[6].contents[0].strip())
				, int(pit1Tds[7].contents[0].strip())
				, int(pit1Tds[8].contents[0].strip())
				, float(pit1Tds[9].contents[0].strip())
				, int(pit1Tds[10].contents[0].strip())
				, int(pit1Tds[11].contents[0].strip())
				, float(".".join([i.split("/")[0] for i in pit1Tds[12].contents[0].strip().split()]))
				, int(pit1Tds[13].contents[0].strip())
				, int(pit1Tds[14].contents[0].strip())
				, int(pit1Tds[15].contents[0].strip())
				, int(pit1Tds[16].contents[0].strip())
				, int(pit2Tds[1].contents[0].strip())
				, int(pit2Tds[2].contents[0].strip())
				, int(pit2Tds[3].contents[0].strip())
				, int(pit2Tds[4].contents[0].strip())
				, int(pit2Tds[5].contents[0].strip())
				, int(pit2Tds[6].contents[0].strip())
				, int(pit2Tds[7].contents[0].strip())
				, int(pit2Tds[8].contents[0].strip())
				, int(pit2Tds[9].contents[0].strip())
				, int(pit2Tds[10].contents[0].strip())
				, int(pit2Tds[11].contents[0].strip())
				, float(pit2Tds[12].contents[0].strip())
				, float(pit2Tds[13].contents[0].strip())
				, int(pit2Tds[14].contents[0].strip())
				, float(hit1Tds[1].contents[0].strip())
				, int(hit1Tds[3].contents[0].strip())
				, int(hit1Tds[4].contents[0].strip())
				, int(hit1Tds[5].contents[0].strip())
				, int(hit1Tds[6].contents[0].strip())
				, int(hit1Tds[7].contents[0].strip())
				, int(hit1Tds[8].contents[0].strip())
				, int(hit1Tds[9].contents[0].strip())
				, int(hit1Tds[10].contents[0].strip())
				, int(hit1Tds[11].contents[0].strip())
				, int(hit1Tds[12].contents[0].strip())
				, int(hit1Tds[13].contents[0].strip())
				, int(hit1Tds[14].contents[0].strip())
				, int(hit1Tds[15].contents[0].strip())
				, int(hit2Tds[1].contents[0].strip())
				, int(hit2Tds[2].contents[0].strip())
				, int(hit2Tds[3].contents[0].strip())
				, int(hit2Tds[4].contents[0].strip())
				, int(hit2Tds[5].contents[0].strip())
				, float(hit2Tds[6].contents[0].strip())
				, float(hit2Tds[7].contents[0].strip())
				, int(hit2Tds[8].contents[0].strip())
				, float(hit2Tds[9].contents[0].strip())
				, float(hit2Tds[10].contents[0].strip())
				, float(hit2Tds[11].contents[0].strip())
				, int(hit2Tds[12].contents[0].strip())
				, float(hit2Tds[13].contents[0].strip())
				, float(hit2Tds[14].contents[0].strip())
				, float(hit2Tds[15].contents[0].strip())
				, 0
				, 0
				, 0.0
				, ""
				))
	return teamRecords

def InsertTeams(teams, db):
	from operator import itemgetter
	cur = db.cursor()
	sorted_teams = sorted(teams.iteritems(), key=itemgetter(1))
	for sorted_team in sorted_teams:
		cur.execute("SELECT COUNT(1) FROM team WHERE name=%s", sorted_team[0])
		if not cur.fetchone()[0]:
			print "Inserting team. sorted_team : ", sorted_team
			cur.execute("INSERT INTO team (team_id,name) VALUES(%s, %s)", (sorted_team[1], sorted_team[0]))
	db.commit()

def InsertTeamRanks(dates, teams, db):
	cur = db.cursor()
	for date in dates:
		teamRanks = TeamRanks(date, teams)
		print "Checking date. date : ", date
		for teamRank in teamRanks:
			cur.execute("SELECT COUNT(1) FROM teaminfo WHERE team_id=%s AND t_g=%s", (teamRank[0], teamRank[2]))
			if not cur.fetchone()[0]:
				print "Inserting teaminfo. teamRank : ", teamRank
				cur.execute("INSERT INTO teaminfo (team_id,t_era,t_g,t_sho,t_cg,t_w,t_l,t_sv,t_hld,t_wavg,t_tbf,t_np,t_ip,t_ah,t_a2b,t_a3b,t_ahr,t_asac,t_asf,t_abb,t_aibb,t_ahbp,t_k,t_wp,t_bk,t_ar,t_aer,t_bs,t_whip,t_aavg,t_qs,t_avg,t_pa,t_ab,t_r,t_hit,t_2b,t_3b,t_hr,t_tb,t_rbi,t_sb,t_cs,t_sac,t_sf,t_bb,t_ibb,t_hbp,t_so,t_gdp,t_slg,t_obp,t_err,t_sr,t_kbb,t_slgr,t_mh,t_ops,t_savg,t_pavg,t_rank,t_tie,t_diff,t_seq) VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)", teamRank)
			else:
				print "Updating teaminfo. teamRank : ", teamRank
				cur.execute("UPDATE teaminfo SET t_w=%s, t_l=%s, t_wavg=%s, t_slg=%s, t_obp=%s, t_rank=%s, t_tie=%s, t_diff=%s, t_seq=%s WHERE team_id=%s and t_g=%s", (teamRank[5], teamRank[6], teamRank[9], teamRank[50], teamRank[51], teamRank[60], teamRank[61], teamRank[62], teamRank[63], teamRank[0], teamRank[2]))
	db.commit()

def InsertTeamRecords(teams, db):
	cur = db.cursor()
	teamRecords = TeamRecords(teams)
	for teamRecord in teamRecords:
		cur.execute("SELECT COUNT(1) FROM teaminfo WHERE team_id=%s AND t_g=%s", (teamRecord[0], teamRecord[2]))
		if not cur.fetchone()[0]:
			print "Inserting teaminfo. teamRecord : ", teamRecord
			cur.execute("INSERT INTO teaminfo (team_id,t_era,t_g,t_sho,t_cg,t_w,t_l,t_sv,t_hld,t_wavg,t_tbf,t_np,t_ip,t_ah,t_a2b,t_a3b,t_ahr,t_asac,t_asf,t_abb,t_aibb,t_ahbp,t_k,t_wp,t_bk,t_ar,t_aer,t_bs,t_whip,t_aavg,t_qs,t_avg,t_pa,t_ab,t_r,t_hit,t_2b,t_3b,t_hr,t_tb,t_rbi,t_sb,t_cs,t_sac,t_sf,t_bb,t_ibb,t_hbp,t_so,t_gdp,t_slg,t_obp,t_err,t_sr,t_kbb,t_slgr,t_mh,t_ops,t_savg,t_pavg,t_rank,t_tie,t_diff,t_seq) VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)", teamRecord)
		else:
			print "Updating teaminfo. teamRecord : ", teamRecord
			cur.execute("UPDATE teaminfo SET t_era=%s, t_sho=%s, t_cg=%s, t_w=%s, t_l=%s, t_sv=%s, t_hld=%s, t_wavg=%s, t_tbf=%s, t_np=%s, t_ip=%s, t_ah=%s, t_a2b=%s, t_a3b=%s, t_ahr=%s, t_asac=%s, t_asf=%s, t_abb=%s, t_aibb=%s, t_ahbp=%s, t_k=%s, t_wp=%s, t_bk=%s, t_ar=%s, t_aer=%s, t_bs=%s, t_whip=%s, t_aavg=%s, t_qs=%s, t_avg=%s, t_pa=%s, t_ab=%s, t_r=%s, t_hit=%s, t_2b=%s, t_3b=%s, t_hr=%s, t_tb=%s, t_rbi=%s, t_sb=%s, t_cs=%s, t_sac=%s, t_sf=%s, t_bb=%s, t_ibb=%s, t_hbp=%s, t_so=%s, t_gdp=%s, t_slg=%s, t_obp=%s, t_err=%s, t_sr=%s, t_kbb=%s, t_slgr=%s, t_mh=%s, t_ops=%s, t_savg=%s, t_pavg=%s WHERE team_id=%s and t_g=%s", (teamRecord[1], teamRecord[3], teamRecord[4], teamRecord[5], teamRecord[6], teamRecord[7], teamRecord[8], teamRecord[9], teamRecord[10], teamRecord[11], teamRecord[12], teamRecord[13], teamRecord[14], teamRecord[15], teamRecord[16], teamRecord[17], teamRecord[18], teamRecord[19], teamRecord[20], teamRecord[21], teamRecord[22], teamRecord[23], teamRecord[24], teamRecord[25], teamRecord[26], teamRecord[27], teamRecord[28], teamRecord[29], teamRecord[30], teamRecord[31], teamRecord[32], teamRecord[33], teamRecord[34], teamRecord[35], teamRecord[36], teamRecord[37], teamRecord[38], teamRecord[39], teamRecord[40], teamRecord[41], teamRecord[42], teamRecord[43], teamRecord[44], teamRecord[45], teamRecord[46], teamRecord[47], teamRecord[48], teamRecord[49], teamRecord[50], teamRecord[51], teamRecord[52], teamRecord[53], teamRecord[54], teamRecord[55], teamRecord[56], teamRecord[57], teamRecord[58], teamRecord[59], teamRecord[0], teamRecord[2]))
	db.commit()

def CrawlTeams():
	from MySQLdb import connect
	from dates import Dates
	teams = Teams()
	db = connect(db="dbproject", user="root", passwd="asdf1234", use_unicode=True, charset="utf8")
	InsertTeams(teams, db)
	dates = Dates()
	InsertTeamRanks(dates, teams, db)
	InsertTeamRecords(teams, db)

if __name__ == "__main__":
	CrawlTeams()
