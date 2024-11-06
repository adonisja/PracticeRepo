def sumOfLeftLeaves(self, root):
    self.sum = 0
    def sumOfLeftLeaves(root, isLeft):
        if isLeft and not (root.left and root.right):
            self.sum += root.val
            return
        if root.left:
            sumOfLeftLeaves(root.left, True)
        if root.right:
            sumOfLeftLeaves(root.right, False)
        
    if not root:
        return 0
    sumOfLeftLeaves(root, False)
    return self.sum

def main():
    pass

if __name__ == "__main__":
    main()