from Node import *

class Search:

    def get_path(self, src, dst): 
        path = [dst]
        while path[0] != src:
            path.insert(0, path[0].get_parent())
        return path

    def get_actions(self, src, dst):
        path = self.get_path(src, dst)
        actions = []
        for i in range(1, len(path)):
            action = path[i].get_action()
            if action == 'N':
                actions.append('North')
            elif action == 'S':
                actions.append('South')
            elif action == 'E':
                actions.append('East')
            elif action == 'W':
                actions.append('West')
        return actions
    
    def get_manhattan_dist(self, src, dst):
        return abs(src[0] - dst[0]) + abs(src[1] - dst[1])
    
    def UCS_Search(self, grid, src, dst):
        root = Node(grid, src)

        actions = []
    
        expanded = []
        frontier = [] # frontier is Priority Queue

        frontier.append((root, 0))
        while frontier:
            frontier.sort(key = lambda g: g[1])
            node, g = frontier.pop(0)

            if node.get_p_pos() in dst:
                dst.remove(node.get_p_pos())
                if len(dst) == 0:
                    return self.get_actions(root, node)
                actions = self.get_actions(root, node) + self.UCS_Search(grid, node.get_p_pos(), dst)
                return actions

            if node.get_p_pos() in expanded:
                continue

            expanded.append(node.get_p_pos())
            
            successors = node.get_successors()
            for succ in successors:
                if succ.get_p_pos() not in expanded:
                    g_succ = g + 1
                    frontier.append((succ, g_succ))
        return None

    def AStar_Helper(self, grid, src, dst):

        root = Node(grid, src)

        expanded = []
        frontier = []

        frontier.append((root, 0, 0))
        
        while frontier:
            frontier.sort(key = lambda f: f[2])
            node, g, f = frontier.pop(0)

            if node.get_p_pos() == dst:
                actions = self.get_actions(root, node) 
                return actions
            
            if node.get_p_pos() in expanded:
                continue

            expanded.append(node.get_p_pos())

            successors = node.get_successors()
            for succ in successors:
                if succ.get_p_pos() not in expanded:
                    g_succ = g + 1
                    h_succ = self.get_manhattan_dist(succ.get_p_pos(), dst)
                    frontier.append((succ, g_succ, g_succ + h_succ))
        return None
    
    def AStar_Search(self, grid, src, dst):
        actions = []
        while len(dst) != 0:
            dict = {}
            for goal in dst:
                dict[goal] = len(self.AStar_Helper(grid, src, goal))
            nearest_goal = min(dict, key=dict.get)
            actions += self.AStar_Helper(grid, src, nearest_goal)
            dst.remove(nearest_goal)
            src = nearest_goal
        return actions





