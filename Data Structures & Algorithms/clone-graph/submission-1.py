"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        copies = {}

        def dfs(node):
            if not node:
                return None
            if node in copies:
                return copies[node]
            
            c = Node(node.val)
            copies[node] = c

            for n in node.neighbors:
                c.neighbors.append(dfs(n))
            
            return c
            
        return dfs(node)
        

