import sys
sys.setrecursionlimit(10000)

class Solution:
    def match(self, h, node):
        if not h:
            return True
        elif not node or node.val != h.val:
            return False

        return self.match(h.next, node.left) or self.match(h.next, node.right)

    def isSubPath(self, head, root) -> bool:
        if not root:
            return False
        elif self.match(head, root):
            return True

        return self.isSubPath(head, root.left) or self.isSubPath(head, root.right)