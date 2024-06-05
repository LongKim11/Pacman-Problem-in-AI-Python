class Node:

    def __init__(self, grid, p_pos, action = None, parent = None):
        self.grid = grid
        self.pi, self.pj = p_pos
        self.action = action 
        self.parent = parent

    def get_p_dst(self, action):
        pi_dst, pj_dst = self.pi, self.pj
        if action == 'N':
            pi_dst -= 1
        elif action == 'S':
            pi_dst += 1
        elif action == 'E':
            pj_dst += 1 
        elif action == 'W':
            pj_dst -= 1
        return pi_dst, pj_dst
    
    def get_succ_by(self, action):
        pi_dst, pj_dst = self.get_p_dst(action)
        if self.grid[pi_dst][pj_dst] == '%':
            return None
        p_new_pos = (pi_dst, pj_dst)
        return Node(self.grid, p_new_pos, action, self)
    
    def get_successors(self):
        result = []
        for action in ['N', 'S', 'E', 'W']:
            succ = self.get_succ_by(action)
            if succ != None:
                result.append(succ)
        return result

    def get_parent(self):
        return self.parent 

    def get_action(self):
        return self.action
    
    def get_p_pos(self):
        return (self.pi, self.pj)

