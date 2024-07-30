# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def rightSideView(root):
    """
    Write your code here
    :type root: TreeNode
    :rtype: TreeNode
    """
    from collections import deque
    if not root:
        return []
    ans = []
    q = deque([root])
    while q:
        right = None
        length = len(q)
        for i in range(length):
            node = q.popleft()
            if node:
                right = node
                q.append(node.left)
                q.append(node.right)
        if right:
            ans.append(right.val)
    return ans