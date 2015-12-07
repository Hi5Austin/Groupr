import matcher

classSize = 4


matcher.studentMaker('A', 90, 'male', 5, 4, 4, [2], [4])
matcher.studentMaker('B', 90, 'female', 5, 4, 4, [1], [])
matcher.studentMaker('C', 65, 'male', 3, 2, 1, [4], [])
matcher.studentMaker('D', 65, 'female', 3, 2, 1, [3], [1])

#A and C
#B and D
matcher.groupMaker(classSize)

matcher.match()
matcher.printMatch()
