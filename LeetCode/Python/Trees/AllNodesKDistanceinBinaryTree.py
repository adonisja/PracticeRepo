import collections
def __init__(self, val=0, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right
         
# Your function distanceK is called as such:
# root = TreeNode()
# rightNode = TreeNode()
# root.right = rightNode
# distanceK(root, rightNode, 1)

"""def distanceK(root, target, k):
    if not k:
        return target.val
    graph = collections.defaultdict(list) #creates a dict where the default value is an empty list[]

    queue = collections.deque([root])
    while queue:
        node = queue.popleft()
        if node.left: 
            #add the left node from the current node to adjacency graph
               graph[node].append(node.left)
            # add the bi-directional equivalent so we can see that
            #  the parent from the child
               graph[node.left].append(node)
            # add the child to the queue
               queue.append(node.left)

            # do the same to the right side
        if node.right:
            graph[node].append(node.right)
            graph[node.right].append(node)
            queue.append(node.right)
    res =[]
    visited = set([target])
    queue = collections.deque([(target, 0)])
    while queue:
        node, distance = queue.popleft()
        if distance == k:
            res.append(node.val)
        else:
            for edge in graph[node]:
                if edge not in visited:
                    visited.add(edge)
                    queue.append((edge, distance + 1))

    return res"""
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def distanceK(root, target, K):
    def findPath(node, target, path):
        if not node:
            return False
        if node.val == target.val:
            path.append(node)
            return True
        if findPath(node.left, target, path) or findPath(node.right, target, path):
            path.append(node)
            return True
        return False

    def findDownwards(node, K, path, res):
        if not node or node in path or K < 0:
            return
        if K == 0:
            res.append(node.val)
            return
        findDownwards(node.left, K-1, path, res)
        findDownwards(node.right, K-1, path, res)

    path = []
    findPath(root, target, path)
    res = []
    for i, node in enumerate(reversed(path)):
        if i == K:
            res.append(node.val)
        elif i < K:
            if i == 0:
                findDownwards(node, K-1, path, res)
            else:
                if node.left == path[-(i+1)]:
                    findDownwards(node.right, K-i-1, path, res)
                else:
                    findDownwards(node.left, K-i-1, path, res)
    return res


def main():
    pass


if __name__ == '__main__':
    main()