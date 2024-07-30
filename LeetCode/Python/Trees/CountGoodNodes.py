class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = self.right = None


def goodNodes(root):
    """
    Write your code here
    :type root: TreeNode
    :rtype: TreeNode
    """
    def dfs(node, maxVal):
        if not node:
            return 0
        ans = 1 if node.val >= maxVal else 0
        maxVal = max(maxVal, node.val)
        ans += dfs(node.left, maxVal)
        ans += dfs(node.right, maxVal)
        return ans
    
    return dfs(root, root.val)