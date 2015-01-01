#!/usr/bin/env python
# -*- coding:utf-8 -*-
from dates import Yesterday

def LoadClassifiers(date):
	from cPickle import load
	import sys
	from os.path import dirname, exists
	from os import mkdir, walk
	from datetime import datetime
	classifiers_dir = dirname(sys.argv[0]) + "/classifiers/"
	kNN = []
	svm = []
	sgd = []
	tree = []
	esb = []
	gnb = []
	for base, dirs, names in walk(classifiers_dir):
		for name in names:
			if name.startswith("kNN"):
				kNN.append(name.split("_")[1])
			elif name.startswith("svm"):
				svm.append(name.split("_")[1])
			elif name.startswith("sgd"):
				sgd.append(name.split("_")[1])
			elif name.startswith("tree"):
				tree.append(name.split("_")[1])
			elif name.startswith("esb"):
				esb.append(name.split("_")[1])
			elif name.startswith("gnb"):
				gnb.append(name.split("_")[1])
	kNN = sorted(kNN)
	svm = sorted(svm)
	sgd = sorted(sgd)
	tree = sorted(tree)
	esb = sorted(esb)
	gnb = sorted(gnb)
	classifiers = []
	rate = []
	if date in kNN:
		with open(classifiers_dir + 'kNN_' + date, 'rb') as fid:
			classifiers.append(load(fid))
			rate.append(0.7406)
	elif len(kNN) > 0:
		with open(classifiers_dir + 'kNN_' + kNN[-1], 'rb') as fid:
			classifiers.append(load(fid))
			rate.append(0.7406)
	if date in svm:
		with open(classifiers_dir + 'svm_' + date, 'rb') as fid:
			classifiers.append(load(fid))
			rate.append(0.2766)
	elif len(svm) > 0:
		with open(classifiers_dir + 'svm_' + svm[-1], 'rb') as fid:
			classifiers.append(load(fid))
			rate.append(0.2766)
	if date in sgd:
		with open(classifiers_dir + 'sgd_' + date, 'rb') as fid:
			classifiers.append(load(fid))
			rate.append(0.2939)
	elif len(sgd) > 0:
		with open(classifiers_dir + 'sgd_' + sgd[-1], 'rb') as fid:
			classifiers.append(load(fid))
			rate.append(0.2939)
	if date in tree:
		with open(classifiers_dir + 'tree_' + date, 'rb') as fid:
			classifiers.append(load(fid))
			rate.append(0.5391)
	elif len(tree) > 0:
		with open(classifiers_dir + 'tree_' + tree[-1], 'rb') as fid:
			classifiers.append(load(fid))
			rate.append(0.5391)
	if date in esb:
		with open(classifiers_dir + 'esb_' + date, 'rb') as fid:
			classifiers.append(load(fid))
			rate.append(0.5667)
	elif len(esb) > 0:
		with open(classifiers_dir + 'esb_' + esb[-1], 'rb') as fid:
			classifiers.append(load(fid))
			rate.append(0.5667)
	if date in gnb:
		with open(classifiers_dir + 'gnb_' + date, 'rb') as fid:
			classifiers.append(load(fid))
			rate.append(0.2641)
	elif len(gnb) > 0:
		with open(classifiers_dir + 'gnb_' + gnb[-1], 'rb') as fid:
			classifiers.append(load(fid))
			rate.append(0.2641)
	sum_of_rate = sum(rate)
	rate = [round(r * 100 / sum_of_rate, 1) for r in rate]
	return rate, classifiers

def PredictMatch(batter_player_id, pitcher_player_id, date = Yesterday().isoformat()):
	from match_result_creator import MatchDetails
	from MySQLdb import connect
	from os import linesep
	rate, classifiers = LoadClassifiers(date)
	db = connect(db="dbproject", user="root", passwd="asdf1234", use_unicode=True, charset="utf8")
	matchDetails = MatchDetails(date, batter_player_id, pitcher_player_id, db)
	prediction_map = {1:"번트", 2:"희생번트", 3:"희생플라이", 4:"희생실책", 5:"희생선택"
	, 6:"플라이", 7:"안타", 8:"2루타", 9:"3루타", 10:"홈런", 11:"땅볼", 12:"병살"
	, 13:"직선타", 14:"파울아웃", 15:"실책", 16:"삼진", 17:"야수선택", 18:"사사구"}
	predictions = {}
	for i in xrange(len(classifiers)):
		prediction = classifiers[i].predict(matchDetails)
		label = prediction_map[prediction[0]]
		predictions.setdefault(label, 0)
		predictions[label] += rate[i]
	for i in predictions:
		print i + "\t" + str(predictions[i]) + "%"

if __name__=="__main__":
	import sys
	batter_player_id = sys.argv[1]
	pitcher_player_id = sys.argv[2]
	if len(sys.argv) >= 4:
		date = sys.argv[3]
		PredictMatch(batter_player_id, pitcher_player_id, date)
	else:
		PredictMatch(batter_player_id, pitcher_player_id)
