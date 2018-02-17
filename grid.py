from math import ceil

class grid:
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

	self.slices = []

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
	

