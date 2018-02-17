from math import ceil

class slice:
    def __init__(self, solust, sagalt, grid):
	self.solust = solust
	self.sagalt = sagalt
	self.mushroomCount = 0
	self.tomatoCount = 0
	self.grid = grid
	
    def move(self, direction:str):
	# TODO

    def checkMinDist(self, direction:str):
	diff = (0, 0)
        if direction == 'U':
            diff = (0, 1)
        elif direction == 'D':
            diff = (0, -1)
        elif direction == 'R':
            diff = (1, 0)
        else #if direction == 'L':
            diff = (-1, 1)

        # TODO 

        
        # @returns {direction:str,distance:int}

    
    def checkAllDistances(self)
        # TODO

class grid():
	
    def __init__(self):
	self.r, self.c, self.a, self.b = input().split()
        # 2D arr of (chr, bool)
        self.board = []
        
        self.mantarCount = self.domatesCount = 0
        for i in range(self.r):
            row = map(lambda x: (x, False), input().split())
            self.board.append(row)
            for (c, _) in row:
                if c == 'M':
                    self.mantarCount += 1
                else:
                    self.domatesCount += 1

        # TODO WARNING
        if self.mantarCount > self.domatesCount:
            self.mantarCount, self.domatesCount = self.domatesCount, self.mantarCount
            self.mantar  = 'T'
            self.domates = 'M'
    
        else:
            self.mantar  = 'M'
            self.domates = 'T'

        self.minSliceByB = int(ceil(r * c / b))
	self.maxSliceByA = self.mantarCount // a

        """
        self.remainingT = None
	self.remainingM = None
        """

	self.slices = []

    """
    def populateGrid(self):
	pass
    """

    def isTaken(self, coord) -> bool:
        return board[coord[0]][coord[1]]

    def reduceTNumber(self, count):
        self.domatesCount -= count

    def reduceMNumber(self, count):
        self.mantarCount -= count
	
    def placeNewSlice(self, coord) -> slice:
        # TODO

    def getNewSlicePositionByDistance(self):
	# TODO

    def placeNSlice(self,sliceCount):
        for i in range(sliceCount):
            self.placeNewSlice()
	

