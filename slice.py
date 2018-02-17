class slice:
    def __init__(self, coord, grid):
        self.solust = coord
        self.sagalt = coord
        self.mushroomCount = 0 
        self.tomatoCount = 0

        if grid[self.solust[0]][self.solust[1]] == 'T':
            self.tomatoCount = 1 
        else :# grid[self.solust[0]][self.solust[1]] == 'M'
            self.mushroomCount = 1

        self.grid = grid
        
    def move(self, direction:str):
        pass
        # TODO

    # TODO WARNING
    def checkMinDist(self, direction:str):
        w = self.sagalt[1] - self.solust[1]
        h = self.sagalt[0] - self.solust[0]

        if direction == 'U':
            cell = (self.solust[0]-1, self.solust[1])  # inclusive

            dist = 0
            flag = False
            while isCellValid(cell):

                for _ in range(w):
                    if grid.isTaken(cell):
                        flag = True
                        break
                    cell = (cell[0], cell[1]+1)

                if flag:
                    break
                
                dist += 1
                
                cell = (cell[0]-1, cell[1])

        elif direction == 'D':
            cell = (self.sagalt[0]+1, self.solust[1])  # inclusive

            dist = 0
            flag = False
            while isCellValid(cell):

                for _ in range(w):
                    if grid.isTaken(cell):
                        flag = True
                        break
                    cell = (cell[0], cell[1]+1)

                if flag:
                    break
                
                dist += 1
                
                cell = (cell[0]+1, cell[1])

        elif direction == 'R':
            cell = (self.solust[0], self.sagalt[1]+1)  # inclusive

            dist = 0
            flag = False
            while isCellValid(cell):

                for _ in range(h):
                    if grid.isTaken(cell):
                        flag = True
                        break
                    cell = (cell[0]+1, cell[1])

                if flag:
                    break
                
                dist += 1
                
                cell = (cell[0], cell[1]+1)

        else :#if direction == 'L'
            cell = (self.solust[0], self.solust[1]-1)  # inclusive

            dist = 0
            flag = False
            while isCellValid(cell):

                for _ in range(h):
                    if grid.isTaken(cell):
                        flag = True
                        break
                    cell = (cell[0]+1, cell[1])

                if flag:
                    break
                
                dist += 1
                
                cell = (cell[0], cell[1]-1)

        return dist

    def isCellValid(self, cell):
        return cell[0] >= 0 and cell[1] >= 0 and cell[0] < grid.r and cell[1] < grid.c

    def checkAllDistances(self):
        # TODO
        pass

    def getLegalMoves(self):
        # U ? D ? R ? L ? TODO
        # return (0, 0, 0, 0)
        pass

    def getMoveDirection(self, legalMovesTuple):
        # return 'D' TODO
        pass


