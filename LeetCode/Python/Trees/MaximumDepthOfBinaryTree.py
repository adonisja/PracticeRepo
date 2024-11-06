# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right   

    def maxDepth(root) -> int:
        if not root:
            return 0
        return 1 + max(TreeNode.maxDepth(root.left), TreeNode.maxDepth(root.left))


def main():
    root = [3, 9, 20, None, None, 15, 7]
    print(TreeNode.maxDepth(root))

if __name__ == "__main__":
    main()