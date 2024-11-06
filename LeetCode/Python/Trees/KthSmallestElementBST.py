class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def kthSmallest(root, k):
# Things to note, a BST is always sorted so level order traversal is necessary
    '''    n = 0  #Number of visited nodes, if n == k, then we know we've got the val/node we need
    stack = []  #create a stack to keep track of parent nodes
    curr = root  #pointer

    while curr or stack:
        while curr:
            stack.append(curr) #append the parent to the stack so we can return after visiting the left node
            curr = curr.left   #keep going left

        curr = stack.pop() #return to the parent node
        n += 1              
        if n == k:          #the kth element has been found so return it
            return curr.val
        curr = curr.right   #visit the right node '''
    
    def helper(root):
        if root is None:
            return []
        return helper(root.left) + [root.val] + helper(root.right)
    return helper(root)[k-1]
    

def main():
    pass

if __name__ == '__main__':
    main()