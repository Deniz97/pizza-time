from math import ceil
from math import sqrt
from slicem import slicem

class grid:
	def __init__(self):
		self.r, self.c, self.a, self.b = input().split()
		# 2D arr of (chr, bool)
		self.board = []
		self.r = int(self.r)
		self.c = int(self.c)
		self.a = int(self.a)
		self.b = int(self.b)
        
		self.mantarCount = self.domatesCount = 0
		for i in range(self.r):
			row = list(map(lambda x: [x, False], list(input()) ))
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

		self.minSliceByB = int(ceil(self.r * self.c / self.b))
		self.maxSliceByA = self.mantarCount // self.a

		self.slices = []
		self.originalMantarCount = self.mantarCount
		self.originalDomatesCount = self.domatesCount
		#print("initing")
		#print(self.board)

	def isTaken(self, coord):
		return self.board[coord[0]][coord[1]][1]

	def setTaken(self, coord):
		self.board[coord[0]][coord[1]][1] = True

	def reduceTNumber(self, count):
		self.domatesCount -= count

	def reduceMNumber(self, count):
		self.mantarCount -= count
	
	def increaseMNumber(self,count):
		self.mantarCount += count

	def increaseTNumber(self,count):
		self.domatesCount += count
	
	def placeNewSlice(self, coord):
		#TODO
		self.slices.append(slicem((coord[0],coord[1]),self))

		if self.board[coord[0]][coord[1]][0] == self.mantar:
			self.reduceMNumber(1)
		else: #self.board[coord[0]][coord][1] == self.domates
			self.reduceTNumber(1)

		self.setTaken(coord)


	def getNewSlicePositionByDistance(self, cell_type):
		"""
		#old code
		x,y = [0.0,0.0]
		for rect  in self.slices:
			x += rect.sagalt[0]
			y += rect.sagalt[1]
		
		if( len(self.slices) != 0):
			x /= float(len(self.slices))
			y /= float( len(self.slices))
		
		for rect in self.board:
		"""

		#first, calculate the agirlikli ortalama of all slices
		ortalar = []
		for s in self.slices:
			ortalar.append( s.getCenterAsFloat() )
		ortX = sum( [ x[0] for x in ortalar ] ) / len(ortalar)
		ortY = sum( [ x[1] for x in ortalar ] ) / len(ortalar)

		#now calculate all distances to free cell_type s and find the max
		coord_with_max_distance = (0,0)
		max_distance = 0
		for i in range( len(self.board) ):
			for j in range( len( self.board[0] ) ):
				
				if self.board[i][j][0] == cell_type and not self.isTaken((i,j)):
					curr_dist = self.floatDistance( (ortX,ortY), (i,j) )
					if( curr_dist >= max_distance):
						coord_with_max_distance = (i,j)

		# return the max
		print("new slice position coord: ",coord_with_max_distance)
		return coord_with_max_distance







	#def placeNSlice(self,sliceCount):
	#	for i in range(sliceCount):
	#		self.placeNewSlice(getNewSlicePositionByDistance())

	@staticmethod
	def distance(rect1,rect2):

		assert (rect1.sagalt == rect1.solust) and (rect2.sagalt == rect2.solust) ,"distance methodunda girilen rect1 ve rect2 tek nokta degil."

		return (rect1.sagalt[0]-rect2.sagalt[0])**2 + (rect1.sagalt[0]-rect2.sagalt[0])**2

	def floatDistance(self,c1,c2):
		return sqrt( (c1[0] - c2[0])**2 + (c1[1]-c2[1])**2 )


	def getUntakenMCount(self):
		return self.mantarCount

	def getUntakenTCount(self):
		return self.domatesCount



	def getCurrentSliceCount(self):
		return len(self.slices)

	def minSliceCount(self):
		return self.minSliceByB


	def maxSliceCount(self):
		return self.maxSliceByA

	def getSliceCountToPlace(self):
		return self.minSliceCount()

	def markTaken(self,solust,sagalt):
		mantar = 0
		domates = 0
		(i,j) = solust

		while i < sagalt[0]:
			while j < sagalt[1]:

				if not self.isTaken((i,j)):
					self.setTaken((i,j))
					if self.board[i][j][0] ==self.mantar:
						mantar+=1
					else: # ==domates
						domates+=1
				

				j+=1
			i+=1

		self.reduceTNumber(domates)
		self.reduceMNumber(mantar)

	def placeFirstSlice(self):
		
		#REMEMBER: We assume domates>mantar at start
		coord = self.getLeftUpperMostCoord(self.mantar)
		self.placeNewSlice(coord)
	
	def getMDcount(self,solust,sagalt): # returns (mantarCount, domatesCount) in rectengale
		mantar = 0
		domates = 0
		(i,j) = solust

		while i < sagalt[0]:
			while j < sagalt[1]:

				if self.board[i][j] == self.mantar:
					mantar+=1
				else: #== self.domates
					domates+=1

				j+=1
			i+=1

		return (mantar,domates)


	def getLeftUpperMostCoord(self, cell_type):
		i=0
		while True:
			for x in range(i+1):
				for y in range(i+1):
				
					if self.board[x][y][0] == cell_type:
						print("new slice position coord: ",(x,y))
						return (x,y)
			i+=1

	def placeNextSlice(self):
		if( self.mantarCount <= self.domatesCount ):
			
			coord = self.getNewSlicePositionByDistance(self.mantar)

		else: #self.mantarCount > self.domatesCount
			coord = self.getNewSlicePositionByDistance(self.domates)

		self.placeNewSlice(coord)

		
	def getOrderedSliceArray(self):

		retval = sorted(self.slices,key=lambda x : x.setLegalMoveCount() )
		return retval

