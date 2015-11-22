#name, grade, sex, (0 (BAD) - 5 (GOOD)) motivation, behavior, participation, positives, negatives, idNum
#import student.py

classList = []
noGroup = []

num = 0
groupSize = 2
numGroups = 0


def studentMaker(name, grade, sex, motivation, behavior, participation, positives, negatives):
	idNum = num
	classList.append({'name': name, 'idNum': idNum, 'grade': grade, 'sex': sex, 'motivation': motivation, 'behavior': behavior, 'participation': participation, 'positives': positives, 'negatives': negatives, 'hasGroup': False})
	
	num++
	

def groupMaker(classSize):
	if(classSize % groupSize == 0):
		numGroups = classSize/groupSize
	else
		if(classSize % groupSize == 1)
			numGroups = classSize/groupSize
		else
			numGroups = (classSize/groupSize) + 1 

def isGoodMatch(id1, id2):
	good = True
	while(good):
		for x in classList[id1]['postives']:
			if (x == id2):
				good = False
		for x in classList[id1]['negatives']:
			if (x == id2):
				good = False
		if classList[id1]['behavior'] < 3 and classList[id2]['behavior'] < 3:
			good = False
		if classList[id1]['motivation'] < 3 and classList[id2]['motivation'] < 3:
			good = False
		if classList[id1]['participation'] < 3 and classList[id2]['participation'] < 3:
			good = False
	return good

def match():
	for x in classList:
		for y in classList:
			count = 0
			if isGoodMatch(x, y) && x[hasGroup] == False && y[hasGroup] == False:
				if groupList[count].length < groupSize:                #doesn't account for indivisible people
					group = []
					group.append(classList[x])
					group.append(classList[y])
					groupList.append(group)
					x[hasGroup] = True
					y[hasGroup] = True
					count ++

	for x in classList:
		if x[hasGroup] == False
		group
			groupList[count].append(classList[x])		
		






