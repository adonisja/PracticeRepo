# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
def minDepth(self, root):
    if not root:
        return 0
    self.min_depth = 9999999999999
    self.dfs(root, 0)

    return self.min_depth
    
def dfs(self, node, cur_depth):
    if not node:
        return
    if not node.left and not node.right:
        self.min_depth = min(self.min_depth, cur_depth + 1)
    
    self.dfs(node.left, cur_depth +1)
    self.dfs(node.right, cur_depth +1)

'''def minDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        elif root.right is None:
            return 1 + self.minDepth(root.left)
        elif root.left is None:
            return 1 + self.minDepth(root.right)
        else:
            return 1 + min(self.minDepth(root.left),self.minDepth(root.right))'''