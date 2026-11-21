# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        ret = []
        if not root:
            return ret

        search = deque()
        search.append(root)
        while search:
            ret.append(search[-1].val)
            levellen = len(search)
            for _ in range(levellen):
                curr = search.popleft()
                if curr.left:
                    search.append(curr.left)
                if curr.right:
                    search.append(curr.right)
        return ret