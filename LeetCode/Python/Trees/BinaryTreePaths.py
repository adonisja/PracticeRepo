# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def binaryTreePaths(root):
    if not root:
        return []
    
    def traverseNode(node, pathTillCurNode):
        # Add current node's val to the path
        new_path = pathTillCurNode + [(str(node.val))]
        # if its a leaf node then join the path and add to "paths" 
        if not(node.left or node.right):
            paths.append("->".join(new_path))
            return
        # Otherwise continue traversing
        if node.left:
            traverseNode(node.left, new_path)
        if node.right:
            traverseNode(node.right, new_path)

    paths = []
    traverseNode(root, []) 
    return paths


def main():
    # Construct the binary tree
    #       1
    #      / \
    #     2   3
    #      \
    #       5
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.right = TreeNode(5)

    # Find all root-to-leaf paths
    paths = binaryTreePaths(root)

    # Print the paths
    print(paths)
    binaryTreePaths(root)

if __name__ == "__main__":
    main()