'''def warn(*args, **kwargs):
    pass
import warnings
warnings.warn = warn'''

import numpy as np
from sklearn.tree import DecisionTreeClassifier
from IPython.display import Image  

'''File I/O'''
def formatData(path):
	file = open(path)
	data = file.read()
	file.close()
	lines = [line.strip() for line in data.splitlines()]
	vals = [val.split(",") for val in lines]

	attributes = [[0]*10 for x in range(len(vals))]
	classifier = [0]*len(vals)
	'''Convert Data To Integers'''
	for i in range(len(vals)):
		for j in range(len(vals[0])):
			if j < 10:
				attributes[i][j] = float(vals[i][j])
			else:
				classifier[i] = int(vals[i][j])
	return[classifier, attributes]

data = formatData("poker-hand-training-true.data.txt")


attributes = np.array(data[1])
print(attributes)
classifier = np.array(data[0])
classifier = classifier.reshape(len(classifier),1)


clf = DecisionTreeClassifier()
clf = clf.fit(attributes, classifier)

testData = formatData("poker-hand-testing.data.txt")

print(clf.predict([1,1,1,13,2,4,2,3,1,12]))
print(clf.predict([4,1,4,13,4,12,4,11,4,10]))


clf.predict_proba(testData)

