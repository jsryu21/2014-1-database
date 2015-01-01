# -*- coding:utf-8 -*-
import numpy as np
import pandas as pd
from sklearn import neighbors
import cPickle
import sys
import MySQLdb

label = {1:"번트", 2:"희생번트", 3:"희생플라이", 4:"희생실책", 5:"희생선택"
		, 6:"플라이", 7:"안타", 8:"2루타", 9:"3루타", 10:"홈런", 11:"땅볼", 12:"병살"
		, 13:"직선타", 14:"파울아웃", 15:"실책", 16:"삼진", 17:"야수선택", 18:"사사구"}
rate = [0.7406, 0.2766, 0.2939, 0.5391, 0.5667, 0.2641]
db = MySQLdb.connect(db="dbproject", user="root", passwd="asdf1234", use_unicode=True, charset="utf8")
cur = db.cursor()

def loadClf(f):
	with open('clf/kNN_' + f, 'rb') as fid:
		kNNClf = cPickle.load(fid)
	with open('clf/svm_' + f, 'rb') as fid:
		svmClf = cPickle.load(fid)
	with open('clf/sgd_' + f, 'rb') as fid:
		sgdClf = cPickle.load(fid)
	with open('clf/tree_' + f, 'rb') as fid:
		treeClf = cPickle.load(fid)
	with open('clf/esb_' + f, 'rb') as fid:
		esbClf = cPickle.load(fid)
	with open('clf/gnb_' + f, 'rb') as fid:
		gnbClf = cPickle.load(fid)
	return (kNNClf, svmClf, sgdClf, treeClf, esbClf, gnbClf)

def predict(clfs, l):
	return (clfs[0].predict(l)
			, clfs[1].predict(l)
			, clfs[2].predict(l)
			, clfs[3].predict(l)
			, clfs[4].predict(l)
			, clfs[5].predict(l))

def foo(batter_player_id, pitcher_player_id, f):
	cur.execute("SELECT ab, r, hit, pbi, sb, cs, bb, hbp, so, gdp FROM daily_batter WHERE player_id=%s", batter_player_id)
	accum_daily_batter = [0.0] * 10
	j = 0
	for r in cur.fetchall():
		j += 1
		for i in xrange(10):
			accum_daily_batter[i] += r[i]
	if j == 0:
		return
	for i in xrange(10):
		accum_daily_batter[i] /= j
	cur.execute("SELECT tbf, ip, ah, ahr, abb, ahbp, k, ar, aer FROM daily_pitcher WHERE player_id=%s", pitcher_player_id)
	accum_daily_pitcher = [0.0] * 9
	j = 0
	for r in cur.fetchall():
		j += 1
		for i in xrange(9):
			accum_daily_pitcher[i] += r[i]
	if j == 0:
		return
	for i in xrange(9):
		accum_daily_pitcher[i] /= j
	clfs = loadClf(f)
	result = predict(clfs, accum_daily_batter + accum_daily_pitcher)
	evaluatedResult = {}
	rate_sum = sum(rate)
	for i in xrange(6):
		if label[result[i][0]] in evaluatedResult:
			evaluatedResult[label[result[i][0]]] += rate[i]
		else:
			evaluatedResult.setdefault(label[result[i][0]], rate[i])
	for r in evaluatedResult:
		evaluatedResult[r] /= rate_sum
	return evaluatedResult

if __name__=="__main__":
	batter_player_id = sys.argv[1]
	pitcher_player_id = sys.argv[2]
	if len(sys.argv) == 3:
		f = 'result_2014_05_21_17_39_15.tab'
	else:
		f = sys.argv[3]
	convertedResult = foo(batter_player_id, pitcher_player_id, f)
	for r in convertedResult:
		print r + '\t' + str(round(convertedResult[r] * 100, 1)) + '%'
