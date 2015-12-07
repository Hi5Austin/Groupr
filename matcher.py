#name, grade, sex, (0 (BAD) - 5 (GOOD)) motivation, behavior, participation, positives, negatives, idNum
#import student.py

classList = []
groupList = []
#noGroup = []

num = 0
groupSize = 2
numGroups = 0


def studentMaker(name, grade, sex, motivation, behavior, participation, positives, negatives):
	global num
	idNum = num
	classList.append({'name': name, 'idNum': idNum, 'grade': grade, 'sex': sex, 'motivation': motivation, 'behavior': behavior, 'participation': participation, 'positives': positives, 'negatives': negatives, 'hasGroup': False})
	
	num = num + 1

	

def groupMaker(classSize):
	if(classSize % groupSize == 0):
		numGroups = classSize/groupSize
	else:
		if(classSize % groupSize == 1):
			numGroups = classSize/groupSize
		else:
			numGroups = (classSize/groupSize) + 1 

def isGoodMatch(id1, id2):
	good = True
	#while(good):
	for x in classList[id1]['positives']:
		if (x == id2):
			good = False
	for x in classList[id1]['negatives']:
		if (x == id2):
			good = False
	if classList[id1]['idNum'] == classList[id2]['idNum']:
		good = False
	if classList[id1]['grade'] < 65 and classList[id2]['grade'] < 65:
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
		print('x')
		print(x)
		for y in classList:
			print('y')
			print(y)
			#count = 0
			if isGoodMatch(x['idNum'], y['idNum']) and (x['hasGroup'] == False and y['hasGroup'] == False):
				#if groupList[].length < groupSize:                #doesn't account for indivisible people
				group = []
				group.append(x)
				group.append(y)
				groupList.append(group)
				x['hasGroup'] = True
				y['hasGroup'] = True
				#count = count + 1
				#print count

#	for x in classList:
#		if x['hasGroup'] == False:
#			groupList[count].append(x)		
		
def printMatch():
	for x in groupList:
		print(x)





