import os

class Grid:
    def __init__(self):
        self.grid = [] # grid is 2d array map
        self.food_pos = []
        self.P_pos = (0, 0)

    def print_grid(self):
        for i in range(len(self.grid)):
            for j in range(len(self.grid[i])):
                print(self.grid[i][j], end = '')
            print()
        
    
    def read_from_file(self, filename):
        if os.path.exists(filename):
            with open (filename) as f:
                line = f.readline().strip()
                col = len(line)

                li = []
                for i in range(col):
                    li.append(line[i])
                self.grid.append(li)
                rows = 1

                for line in f:
                    li = []
                    rows += 1
                    l = line.strip()
                    for i in range(col):
                        if (l[i] == 'P'):
                            self.P_pos = (rows - 1, i)
                        elif (l[i] == '.'):
                            self.food_pos.append((rows - 1, i))
                        li.append(l[i])                         
                    self.grid.append(li)

    
    def get_grid(self):
        return self.grid, self.P_pos, self.food_pos

    def get_corners(self):
        rows = len(self.grid)
        col = len(self.grid[0])
        corners = [(1, 1), (1, col - 2), (rows - 2, 1), (rows - 2, col - 2)]
        return corners 
    
    def update_P_pos(self, pi, pj):
        self.grid[pi][pj] = 'P'
        pi_past, pj_past = self.P_pos
        self.grid[pi_past][pj_past] = ' '
        self.P_pos = (pi, pj)


# m = Grid()
# m.read_from_file("pacman_layouts/smallMaze.lay")
# m.print_grid()

# print(m.get_grid())
# print(m.get_corners())
