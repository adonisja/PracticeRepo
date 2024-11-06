# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def isSymmetric(root):
    def dfs(left, right):
        if not left and not right:
            return True
        if not left or not right:
            return False
        
        return (left.val == right.val and dfs(left.left, right.right)\
        and dfs(left.right, right.left))
    return dfs(root.left, root.right)

def main():
#             1
#          /      \
#        2         2
#      /   \    /      \
#   3       4  4        3
    node7 = TreeNode(3)
    node6 = TreeNode(4)
    node5 = TreeNode(4)
    node4 = TreeNode(3)
    node3 = TreeNode(2, node6, node7)
    node2 = TreeNode(2, node4, node5)
    root = TreeNode(1, node2, node3)
    print(isSymmetric(root))
 
if __name__ == "__main__":
    main()