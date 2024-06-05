from Grid import * 
from Search import *
import time
import os
from copy import deepcopy 

class Pacman:

    def visualize(self, map, P_pos, actions):
        os.system('cls')
        map.print_grid()
        time.sleep(0.5)
        os.system('cls')
        pi, pj = P_pos
        for a in actions:
            if a == 'North':
                pi -= 1
            elif a == 'South':
                pi += 1
            elif a == 'East':
                pj += 1
            elif a == 'West':
                pj -= 1 
            map.update_P_pos(pi, pj)
            map.print_grid()
            time.sleep(0.35)
            os.system('cls')

    def solve(self, filename, searchAlgo):
        map = Grid()
        map.read_from_file(filename)
        grid, P_pos, food_pos = map.get_grid()
        dst = food_pos + map.get_corners()
        s = Search()

        if searchAlgo == 'UCS':
            actions = s.UCS_Search(grid, P_pos, dst)
            self.visualize(deepcopy(map), P_pos, actions)
            return actions
        elif searchAlgo == 'AStar':
            actions = s.AStar_Search(grid, P_pos, dst)
            self.visualize(deepcopy(map), P_pos, actions)
            return actions



p = Pacman()
actions = p.solve('pacman_layouts/smallMaze.lay', 'UCS')
print('Executing UCS')
print('List of actions =', actions)
print('Number of actions =', len(actions))
        
# print('---------------------------------------------------------')

# actions = p.solve('pacman_layouts/smallMaze.lay', 'AStar')
# print('Executing AStar')
# print('List of actions =', actions)
# print('Number of actions =', len(actions))
