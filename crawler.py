#!/usr/bin/env python

def CrawlEverything():
	from team_crawler import CrawlTeams
	from player_crawler import CrawlPlayers
	from game_crawler import CrawlGames
	from match_result_creator import CreateMatchResult
	from additional_infos_calculator import CalcAdditionalInfos
	from classifier_creator import CreateClassifiers
	CrawlTeams()
	CrawlPlayers()
	CrawlGames()
	CreateMatchResult(False, 0)
	CreateMatchResult(True, 0)
	CalcAdditionalInfos()
	CreateClassifiers()

if __name__ == "__main__":
	CrawlEverything()
