#!/usr/bin/env python
from dates import Yesterday

def CreateClassifiers(date = Yesterday().isoformat()):
	from pandas import read_csv
	from sklearn import neighbors, svm, tree
	from sklearn.linear_model import SGDClassifier
	from sklearn.ensemble import GradientBoostingClassifier
	from sklearn.naive_bayes import GaussianNB
	from cPickle import dump
	import sys
	from os.path import dirname, exists
	from os import mkdir
	match_results_dir = dirname(sys.argv[0]) + "/match_results/"
	classifiers_dir = dirname(sys.argv[0]) + "/classifiers/"
	if not exists(classifiers_dir):
		mkdir(classifiers_dir, 0775)
	filename = match_results_dir + date + ".tab"
	data = read_csv(filename, sep='\t')
	X = data[data.columns[:-1]]
	y = data['y']
	n_neighbors = 15
	kNNClf = neighbors.KNeighborsClassifier(n_neighbors, weights='distance')
	kNNClf.fit(X, y)
	with open(classifiers_dir + 'kNN_' + date, 'wb') as fid:
		dump(kNNClf, fid)
	svmClf = svm.SVC()
	svmClf.fit(X, y)
	with open(classifiers_dir + 'svm_' + date, 'wb') as fid:
		dump(svmClf, fid)
	sgdClf = SGDClassifier(loss="hinge", penalty="l2")
	sgdClf.fit(X, y)
	with open(classifiers_dir + 'sgd_' + date, 'wb') as fid:
		dump(sgdClf, fid)
	treeClf = tree.DecisionTreeClassifier()
	treeClf.fit(X, y)
	with open(classifiers_dir + 'tree_' + date, 'wb') as fid:
		dump(treeClf, fid)
	esbClf = GradientBoostingClassifier(n_estimators=100, learning_rate=1.0, max_depth=1, random_state=0)
	esbClf.fit(X, y)
	with open(classifiers_dir + 'esb_' + date, 'wb') as fid:
		dump(esbClf, fid)
	gnbClf = GaussianNB()
	gnbClf.fit(X, y)
	with open(classifiers_dir + 'gnb_' + date, 'wb') as fid:
		dump(gnbClf, fid)

if __name__=="__main__":
	import sys
	if len(sys.argv) > 1:
		date = sys.argv[1]
		CreateClassifiers(date)
	else:
		CreateClassifiers()
