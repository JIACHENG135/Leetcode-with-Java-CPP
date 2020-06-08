# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getLonelyNodes(self, root: TreeNode) -> List[int]:
        res = []
        q = deque([root])
        while q:
            cur = q.popleft()
            if cur.left and not cur.right:
                res.append(cur.left.val)
            if cur.right and not cur.left:
                res.append(cur.right.val)
            if cur.left:
                q.append(cur.left)
            if cur.right:
                q.append(cur.right)
        return res