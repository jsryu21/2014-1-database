#!/usr/bin/env python
# -*- coding:utf-8 -*-

def GetMatches(boxScoreUrls, db):
	from game_crawler import GameKey, GameDate
	cur = db.cursor()
	matches = []
	for boxScoreUrl in boxScoreUrls:
		print boxScoreUrl
		gameKey = GameKey(boxScoreUrl)
		if gameKey == "":
			continue
		gameDate = GameDate(gameKey)
		cur.execute("SELECT DISTINCT team_id FROM boxscore_hitter WHERE gameKey=%s", (gameKey))
		away_team_id = cur.fetchone()[0]
		home_team_id = cur.fetchone()[0]
		batterLineups = []
		startLineup = 0
		for i in xrange(15):
			cur.execute("SELECT lineup, name, i" + str(i + 1) + ", ab, hit, rbi, r FROM boxscore_hitter WHERE gameKey=%s and team_id=%s", (gameKey, away_team_id))
			iningLineups = [[], [], [], [], [], [], [], [], []]
			for r in cur.fetchall():
				lineup = r[0]
				if r[2] != "":
					results = r[2].split('/')
					for result in results:
						iningLineups[lineup - 1].append((r[1], home_team_id, int(r[3]), int(r[4]), int(r[5]), int(r[6]), result))
			while len(sum(iningLineups, [])) > 0:
				batterLineups.append(iningLineups[startLineup].pop(0))
				startLineup += 1
				startLineup %= 9
		startLineup = 0
		for i in xrange(15):
			cur.execute("SELECT lineup, name, i" + str(i + 1) + ", ab, hit, rbi, r FROM boxscore_hitter WHERE gameKey=%s and team_id=%s", (gameKey, home_team_id))
			iningLineups = [[], [], [], [], [], [], [], [], []]
			for r in cur.fetchall():
				lineup = r[0]
				if r[2] != "":
					results = r[2].split('/')
					for result in results:
						iningLineups[lineup - 1].append((r[1], away_team_id, int(r[3]), int(r[4]), int(r[5]), int(r[6]), result))
			while len(sum(iningLineups, [])) > 0:
				batterLineups.append(iningLineups[startLineup].pop(0))
				startLineup += 1
				startLineup %= 9
		pitcherLineups = []
		cur.execute("SELECT name, tbf, ah, ahr, k, ar, aer FROM boxscore_pitcher WHERE gameKey=%s and team_id=%s", (gameKey, away_team_id))
		for r in cur.fetchall():
			tbf = int(r[1])
			for i in xrange(tbf):
				pitcherLineups.append((r[0], home_team_id, tbf, int(r[2]), int(r[3]), int(r[4]), int(r[5]), int(r[6])))
		cur.execute("SELECT name, tbf, ah, ahr, k, ar, aer FROM boxscore_pitcher WHERE gameKey=%s and team_id=%s", (gameKey, home_team_id))
		for r in cur.fetchall():
			tbf = int(r[1])
			for i in xrange(tbf):
				pitcherLineups.append((r[0], away_team_id, tbf, int(r[2]), int(r[3]), int(r[4]), int(r[5]), int(r[6])))
		for i in xrange(len(batterLineups)):
			cur.execute("SELECT player_id FROM player NATURAL JOIN daily_batter WHERE name=%s AND competitor_team_id=%s AND ab=%s AND hit=%s AND pbi=%s AND r=%s AND date=%s", batterLineups[i][:-1] + (gameDate,))
			batter_player_id = cur.fetchone()[0]
			cur.execute("SELECT player_id FROM player NATURAL JOIN daily_pitcher WHERE name=%s AND competitor_team_id=%s AND tbf=%s AND ah=%s AND ahr=%s AND k=%s AND ar=%s AND aer=%s AND date=%s", pitcherLineups[i] + (gameDate,))
			print pitcherLineups, gameDate, i, pitcherLineups[i]
			pitcher_player_id = cur.fetchone()[0]
			matches.append((gameDate, batter_player_id, pitcher_player_id, batterLineups[i][-1]))
	return matches

def MatchDetails(gameDate, batter_player_id, pitcher_player_id, db):
	cur = db.cursor()
	cur.execute("SELECT ab, r, hit, pbi, sb, cs, bb, hbp, so, gdp FROM daily_batter WHERE player_id=%s AND date <= %s", (batter_player_id, gameDate))
	daily_batter_count = cur.rowcount
	accum_daily_batter = [0.0] * 10
	for r in cur.fetchall():
		for i in xrange(10):
			accum_daily_batter[i] += r[i]
	if daily_batter_count != 0:
		for i in xrange(10):
			accum_daily_batter[i] /= daily_batter_count
	cur.execute("SELECT tbf, ip, ah, ahr, abb, ahbp, k, ar, aer FROM daily_pitcher WHERE player_id=%s AND date <= %s", (pitcher_player_id, gameDate))
	daily_pitcher_count = cur.rowcount
	accum_daily_pitcher = [0.0] * 9
	for r in cur.fetchall():
		for i in xrange(9):
			accum_daily_pitcher[i] += r[i]
	if daily_pitcher_count != 0:
		for i in xrange(9):
			accum_daily_pitcher[i] /= daily_pitcher_count
	return accum_daily_batter + accum_daily_pitcher

def CreateMatchResult(for_orange, label_map_type):
	label_maps = [{"포번":1, "투번":1, "3번":1, "1번":1
	, "1희번":2, "포희번":2, "투희번":2, "3희번":2, "2희번":2
	, "1희비":3, "좌희비":3, "중희비":3
	, "3희실":4, "포희실":4, "1희실":4, "투희실":4
	, "투희선":5, "3희선":5
	, "3비":6, "1비":6, "좌비":6, "유비":6, "우비":6, "중비":6, "2비":6, "투비":6
	, "좌안":7, "좌중안":7, "2안":7, "투1안":7, "1우안":7, "포안":7, "우안":7, "유안":7, "중안":7, "3안":7, "2우안":7, "우중안":7, "투2안":7, "투좌안":7, "투3안":7, "투유안":7, "1안":7, "투안":7, "2중안":7, "포비":7, "유좌안":7, "우희비":7, "유중안":7
	, "1우2":8, "3좌2":8, "중2":8, "우중2":8, "좌중2":8, "우2":8, "좌2":8
	, "중3":9, "우중3":9, "좌3":9, "좌중3":9, "우3":9
	, "좌홈":10, "좌중홈":10, "우홈":10, "중홈":10, "우중홈":10
	, "포땅":11, "투땅":11, "좌땅":11, "3땅":11, "2땅":11, "1땅":11, "우땅":11, "유땅":11, "중땅":11
	, "2유병":12, "2병":12, "포3병":12, "투2병":12, "투유병":12, "3병":12, "3포병":12, "유병":12, "1병":12, "투포병":12, "3유병":12, "유2병":12, "1유병":12, "투병":12, "32병":12
	, "유직":13, "3직":13, "1직":13, "2직":13, "투직":13
	, "포파":14, "투파":14, "2파":14, "1파":14, "좌파":14, "유파":14, "우파":14, "3파":14
	, "투실":15, "1실":15, "2실":15, "우실":15, "3실":15, "좌실":15, "포실":15, "유실":15
	, "삼진":16, "스낫":16
	, "야선":17
	, "고4":18, "4구":18, "사구":18}
	, {"포번":1, "투번":1, "3번":1, "1번":1, "1희번":1, "포희번":1, "투희번":1, "3희번":1, "2희번":1
	, "1희비":2, "좌희비":2, "중희비":2, "3비":2, "1비":2, "좌비":2, "유비":2, "우비":2, "중비":2, "2비":2, "투비":2, "포파":2, "투파":2, "2파":2, "1파":2, "좌파":2, "유파":2, "우파":2, "3파":2
	, "좌안":3, "좌중안":3, "2안":3, "투1안":3, "1우안":3, "포안":3, "우안":3, "유안":3, "중안":3, "3안":3, "2우안":3, "우중안":3, "투2안":3, "투좌안":3, "투3안":3, "투유안":3, "1안":3, "투안":3, "2중안":3, "포비":3, "유좌안":3, "우희비":3, "유중안":3
	, "1우2":4, "3좌2":4, "중2":4, "우중2":4, "좌중2":4, "우2":4, "좌2":4, "중3":4, "우중3":4, "좌3":4, "좌중3":4, "우3":4, "유직":4, "3직":4, "1직":4, "2직":4, "투직":4
	, "좌홈":5, "좌중홈":5, "우홈":5, "중홈":5, "우중홈":5
	, "포땅":6, "투땅":6, "좌땅":6, "3땅":6, "2땅":6, "1땅":6, "우땅":6, "유땅":6, "중땅":6, "2유병":6, "2병":6, "포3병":6, "투2병":6, "투유병":6, "3병":6, "3포병":6, "유병":6, "1병":6, "투포병":6, "3유병":6, "유2병":6, "1유병":6, "투병":6, "32병":6
	, "3희실":7, "포희실":7, "1희실":7, "투희실":7, "투실":7, "1실":7, "2실":7, "우실":7, "3실":7, "좌실":7, "포실":7, "유실":7, "투희선":7, "3희선":7, "야선":7
	, "삼진":8, "스낫":8
	, "고4":9, "4구":9, "사구":9}
	, {"포번":1, "투번":1, "3번":1, "1번":1, "1희번":1, "포희번":1, "투희번":1, "3희번":1, "2희번":1, "포땅":1, "투땅":1, "좌땅":1, "3땅":1, "2땅":1, "1땅":1, "우땅":1, "유땅":1, "중땅":1, "2유병":1, "2병":1, "포3병":1, "투2병":1, "투유병":1, "3병":1, "3포병":1, "유병":1, "1병":1, "투포병":1, "3유병":1, "유2병":1, "1유병":1, "투병":1, "32병":1
	, "1희비":2, "좌희비":2, "중희비":2, "3비":2, "1비":2, "좌비":2, "유비":2, "우비":2, "중비":2, "2비":2, "투비":2, "포파":2, "투파":2, "2파":2, "1파":2, "좌파":2, "유파":2, "우파":2, "3파":2
	, "좌안":3, "좌중안":3, "2안":3, "투1안":3, "1우안":3, "포안":3, "우안":3, "유안":3, "중안":3, "3안":3, "2우안":3, "우중안":3, "투2안":3, "투좌안":3, "투3안":3, "투유안":3, "1안":3, "투안":3, "2중안":3, "포비":3, "유좌안":3, "우희비":3, "유중안":3, "1우2":3, "3좌2":3, "중2":3, "우중2":3, "좌중2":3, "우2":3, "좌2":3, "중3":3, "우중3":3, "좌3":3, "좌중3":3, "우3":3, "유직":3, "3직":3, "1직":3, "2직":3, "투직":3, "좌홈":3, "좌중홈":3, "우홈":3, "중홈":3, "우중홈":3
	, "3희실":4, "포희실":4, "1희실":4, "투희실":4, "투실":4, "1실":4, "2실":4, "우실":4, "3실":4, "좌실":4, "포실":4, "유실":4, "투희선":4, "3희선":4, "야선":4, "고4":4, "4구":4, "사구":4
	, "삼진":5, "스낫":5}]
	from dates import Dates, Yesterday
	from game_crawler import BoxScoreUrls
	from MySQLdb import connect
	from os.path import isfile, dirname, exists
	from os import mkdir
	import sys
	dates = Dates()
	yesterday = Yesterday(dates).isoformat()
	match_results_dir = dirname(sys.argv[0]) + "/match_results/"
	if not exists(match_results_dir):
		mkdir(match_results_dir, 0775)
	if for_orange:
		filename = match_results_dir + yesterday + "_orange.tab"
	else:
		filename = match_results_dir + yesterday + ".tab"
	if not isfile(filename):
		db = connect(db="dbproject", user="root", passwd="asdf1234", use_unicode=True, charset="utf8")
		boxScoreUrls = BoxScoreUrls(dates)
		matches = GetMatches(boxScoreUrls, db)
		f = open(filename, "w")
		f.write("a1	a2	a3	a4	a5	a6	a7	a8	a9	a10	a11	a12	a13	a14	a15	a16	a17	a18	a19	y\n")
		if for_orange:
			f.write("c	c	c	c	c	c	c	c	c	c	c	c	c	c	c	c	c	c	c	d\n")
			f.write("																			class\n")
		for match in matches:
			matchDetails = MatchDetails(match[0], match[1], match[2], db)
			result = match[3].encode("utf-8")
			if result in label_maps[label_map_type]:
				label = label_maps[label_map_type][result]
				f.write("\t".join(map(str, matchDetails)) + "\t" + str(label) + "\n")
		f.close()

if __name__ == "__main__":
	from optparse import OptionParser
	parser = OptionParser()
	parser.add_option("-o", dest="for_orange", default="False", type="string")
	parser.add_option("-l", dest="label_map_type", default="0", type="int")
	(options, args) = parser.parse_args()
	for_orange = options.for_orange == "True"
	label_map_type = options.label_map_type
	CreateMatchResult(for_orange, label_map_type)
