'''A height-balanced binary tree is a binary tree in which the depth of the two
subtrees of every node never differs by more than one.'''

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def isBalanced(root):
    balanced = [True]

    def height(root):
        if not root:
            return 0
        
        left_height = height(root.left)
        if balanced[0] is False:
            return 0
        right_height = height(root.right)

        if abs(left_height - right_height) > 1:
            balanced[0] = False
            return 0

        return 1 + max(left_height, right_height)
    
    height(root)
    return balanced[0]


def main():
#    1
#   / \
#  2   3
# / \
#4   5
    node4 = TreeNode(4)
    node5 = TreeNode(5)
    node2 = TreeNode(2, node4, node5)
    node3 = TreeNode(3)
    root = TreeNode(1, node2, node3)
    print(isBalanced(root))

if __name__ == "__main__":
    main()
