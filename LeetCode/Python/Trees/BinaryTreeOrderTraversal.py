import ctypes
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def preorderTraversal(root): # 12, 9, 3, 0, 7, 1, 15, 17, 25, 21, 27, 31
    cur, stack = root, []
    res = []
    while cur or stack:
        if cur:
            stack.append(cur.right)
            res.append(cur.val)
            cur = cur.left
        else:
            cur = stack.pop()
    return res

def postOrderTraversal(root): # 0, 3, 1, 7, 9, 25, 17, 31, 27, 21, 15, 12
    if root is None:  # If the tree is empty, we have nothing to do.
        return []

    stack = [root]  # This is our backpack where we keep notes on where to go next.
    result = []  # This is where we'll store the numbers we say "hi" to.
    while stack:  # As long as there are notes in our backpack, we keep exploring.
        cur = stack.pop()  # Take the last note we put in, this tells us where to go next.
        result.insert(0, cur.val)  # Say "hi" to the current number by adding it to our list, but at the beginning.
        
        # Now, decide where to go next. Remember, left first, then right.
        if cur.left:  # If there's a left branch, add a note to visit it.
            stack.append(cur.left)
        if cur.right:  # If there's a right branch, add a note to visit it too.
            stack.append(cur.right)

    return result  # Once we've said "hi" to all the numbers, we're done.


def inOrderTraversal(root):
    if root is None:  # If the forest is empty, there's no adventure.
        return []

    result = []  # This is where we'll keep all the treasure chests we've opened.
    stack = []  # This is our map, helping us remember where to go.
    current = root  # We start our adventure at the entrance of the forest.

    while current or stack:  # As long as there are places to explore or our map has notes.
        while current:  # Keep going left as far as possible.
            stack.append(current)  # Mark the path on our map before going left.
            current = current.left  # Take the left path.

        current = stack.pop()  # We can't go left anymore, so we go back to the last marked path.
        result.append(current.val)  # Open the treasure chest (say "hello" to the number).
        current = current.right  # Now, let's see what's on the right.

    return result  # Adventure is over, and we have all our treasures.
        

def main():
#                      12
#               /                \
#               9                15
#            /    \           /      \
#          3       7         17       21
#        /          \         \       /  
#       0            1         25    27   
#                                       \
#                                        31 
    
    node12 = TreeNode(31)
    node11 = TreeNode(27, None, node12)
    node10 = TreeNode(25)
    node9 = TreeNode(1)
    node8 = TreeNode(0)
    node7 = TreeNode(21, node11)
    node6 = TreeNode(17, None, node10)
    node5 = TreeNode(7, None, node9)
    node4 = TreeNode(3, node8)
    node3 = TreeNode(15, node6, node7)
    node2 = TreeNode(9, node4, node5)
    root = TreeNode(12, node2, node3)
    print(f'PreOrder Traversal: {preorderTraversal(root)}')
    print(f'PostOrder Traversal: {postOrderTraversal(root)}')
    print(f'InOrder Traversal: {inOrderTraversal(root)}')

if __name__ == "__main__":
    main()