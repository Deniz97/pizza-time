rom math import ceil

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
        return board[coord[0]][coord[1]][1]

    def reduceTNumber(self, count):
        self.domatesCount -= count

    def reduceMNumber(self, count):
        self.mantarCount -= count
	
    def increaseMNumber(self,count):
		self.mantarCount += count

	def increaseTNumber(self,count):
		self.domatesCount += count
	
	def placeNewSlice(self, coord) :
        # TODO

		self.slices.append(slice((coord[0],coord[1]),self.board))

    def getNewSlicePositionByDistance(self):
	# TODO

		x,y = [0.0,0.0]
		for rect  in self.slices:
			x += rect.sagalt[0]  
	 		y += rect.sagalt[1]  
		
		x /= float(len(self.slices))
		y /= float( len(self.slices))
		for rect in self.board:
			

    def placeNSlice(self,sliceCount):
        for i in range(sliceCount):
            self.placeNewSlice(getNewSlicePosition())

	@staticmethod
	def distance(rect1,rect2):

		assert(rect1.sagalt == rect1.solust and rect2.sagalt == rect2.solust,"distance methodunda girilen rect1 ve rect2 tek nokta değil.")
		return (rect1.sagalt[0]-rect2.sagalt[0])**2 + (rect1.sagalt[0]-rect2.sagalt[0])**2





	def getUntakenMCount(self):
		return self.mantarCount

	def getUntakenTCount(self):
		return self.domatesCount








