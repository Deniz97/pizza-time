

class slicem:
    
    def __init__(self, coord, grid):
        self.solust = coord
        self.sagalt = coord
        self.mushroomCount = 0 
        self.tomatoCount = 0
        self.legalMoveCount = -1
        self.legalMoves = ()

        if grid.board[self.solust[0]][self.solust[1]] == 'T':
            self.tomatoCount = 1 
        else :# grid[self.solust[0]][self.solust[1]] == 'M'
            self.mushroomCount = 1

        self.grid = grid
        
    def move(self, direction:str):
        
        #not used
        oldCounts = self.grid.getMDcount(self.solust,self.sagalt)
        #not used

        if direction=="U":
            self.solust = (self.solust[0]-1, self.solust[1])
        elif direction=="D":
            self.sagalt = (self.sagalt[0]+1, self.sagalt[1])
        elif direction=="R":
            self.sagalt = (self.sagalt[0], self.sagalt[1]+1)
        elif direction=="L":
            self.solust = (self.solust[0], self.solust[1]-1)

        #returns (mantar_number, domates_number)
        newCounts = self.grid.getMDcount(self.solust,self.sagalt)
        self.mushroomCount = newCounts[0]
        self.tomatoCount = newCounts[1]


        self.grid.markTaken(self.solust,self.sagalt)
        


    def checkMinDist(self, direction:str):
        #print("min distance for: ",self.solust," ",self.sagalt," ",direction)
        w = self.sagalt[1] - self.solust[1] +1
        h = self.sagalt[0] - self.solust[0] +1

        if direction == 'U':
            cell = (self.solust[0]-1, self.solust[1])  # inclusive
            dist = 0
            flag = False
            
            while self.isCellValid(cell):
                
                orgcell = cell
                for _ in range(w):
                    if self.grid.isTaken(cell):
                        flag = True
                        break
                    
                    cell = (cell[0], cell[1]+1)
                    

                if flag:
                    break
                cell = orgcell
                dist += 1
                cell = (cell[0]-1, cell[1])

        elif direction == 'D':
            cell = (self.sagalt[0]+1, self.solust[1])  # inclusive

            dist = 0
            flag = False
            while self.isCellValid(cell):

                orgcell = cell

                for _ in range(w):
                    if self.grid.isTaken(cell):
                        flag = True
                        break
                    cell = (cell[0], cell[1]+1)

                if flag:
                    break
                cell=orgcell
                dist += 1
                cell = (cell[0]+1, cell[1])

        elif direction == 'R':
            cell = (self.solust[0], self.sagalt[1]+1)  # inclusive

            dist = 0
            flag = False
            while self.isCellValid(cell):
                orgcell = cell
                for _ in range(h):
                    if self.grid.isTaken(cell):
                        flag = True
                        break
                    cell = (cell[0]+1, cell[1])

                if flag:
                    break
                cell=orgcell
                dist += 1
                cell = (cell[0], cell[1]+1)



        else :#if direction == 'L'
            cell = (self.solust[0], self.solust[1]-1)  # inclusive

            dist = 0
            flag = False
            while self.isCellValid(cell):
                orgcell = cell

                for _ in range(h):
                    if self.grid.isTaken(cell):
                        flag = True
                        break
                    cell = (cell[0]+1, cell[1])
                
                if flag:
                    break
                cell=orgcell

                dist += 1
                cell = (cell[0], cell[1]-1)

        return dist

    def isCellValid(self, cell):
        return cell[0] >= 0 and cell[1] >= 0 and cell[0] < self.grid.r and cell[1] < self.grid.c

    def checkAllDistances(self):
        # TODO
        pass

    def getCenterAsFloat(self):
        return ((self.solust[0]+self.sagalt[0]) / 2  , (self.solust[1]+self.sagalt[1]) / 2 )


    def setLegalMoves(self):
        # U ? D ? R ? L ? TODO
        # return (0, 0, 0, 0)
        directions = ("U","D","R","L")
        retval = [0,0,0,0]
        for i in range(4):
            if ( self.checkMinDist(directions[i]) > 0 ):
                retval[i] = 1

        retval = tuple(retval)
        self.legalMoves = retval
        return retval


        

    def getMoveDirection(self, legalMoveTuple):
        # return 'D' TODO
        #right now i implement a very basic rule
        #this parts needs to get more complicated
        directions = ("U","D","R","L")
        maxDistance=0
        maxDistanceDir = "U" #lel random

        for i in range(4):
            if ( legalMoveTuple[i] == 1 ):
                currDistance = self.checkMinDist(directions[i])
                if(currDistance>maxDistance):
                    maxDistanceDir = directions[i]

        return maxDistanceDir


    def setLegalMoveCount(self):
        legalMoveTuple = self.setLegalMoves()
        self.legalMoveCount = len( [ x for x in legalMoveTuple if x==1] )
        return self.legalMoveCount

