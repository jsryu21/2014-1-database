import numpy as np
import pandas as pd
from sklearn import neighbors, svm, tree
from sklearn.linear_model import SGDClassifier
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.naive_bayes import GaussianNB
import cPickle
import sys

n_neighbors = 15

def save_clf(f):
	d = pd.read_csv(f, sep='\t')
	X = d[d.columns[:-1]]
	y = d['y']
	kNNClf = neighbors.KNeighborsClassifier(n_neighbors, weights='distance')
	kNNClf.fit(X, y)
	with open('clf/kNN_' + f, 'wb') as fid:
		cPickle.dump(kNNClf, fid)
	svmClf = svm.SVC()
	svmClf.fit(X, y)
	with open('clf/svm_' + f, 'wb') as fid:
		cPickle.dump(svmClf, fid)
	sgdClf = SGDClassifier(loss="hinge", penalty="l2")
	sgdClf.fit(X, y)
	with open('clf/sgd_' + f, 'wb') as fid:
		cPickle.dump(sgdClf, fid)
	treeClf = tree.DecisionTreeClassifier()
	treeClf.fit(X, y)
	with open('clf/tree_' + f, 'wb') as fid:
		cPickle.dump(treeClf, fid)
	esbClf = GradientBoostingClassifier(n_estimators=100, learning_rate=1.0, max_depth=1, random_state=0)
	esbClf.fit(X, y)
	with open('clf/esb_' + f, 'wb') as fid:
		cPickle.dump(esbClf, fid)
	gnbClf = GaussianNB()
	gnbClf.fit(X, y)
	with open('clf/gnb_' + f, 'wb') as fid:
		cPickle.dump(gnbClf, fid)

if __name__=="__main__":
	if len(sys.argv) == 1:
		f = 'result_2014_05_21_17_39_15.tab'
	else:
		f = sys.argv[1]
	save_clf(f)
