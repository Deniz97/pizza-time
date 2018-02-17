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

    def checkAllDistances(self)
        # TODO

