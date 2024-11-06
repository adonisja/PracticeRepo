class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def isValidBST(root) -> bool:
       
    def valid(node, left, right):
        if not node:
            return True
        if not(node.val < right and node.val > left):  
        # Perform a check to see if the current value is less than the
        # value of the left child but greater than the value of the right child c
            return False
        return valid(node.left, left, node.val) and \
        valid(node.right, node.val, right)
    return valid(root,float("-inf"), float("inf"))