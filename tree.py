class TreeNode(object):
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def printData(self):
        print self.data,

class BinaryTree(object):
    def __init__(self):
        self.root = None

    def getRoot(self):
        return self.root

    def inOrderTraversal(self, root):
        if root is None:
            return

        self.inOrderTraversal(root.left)

        root.printData()

        self.inOrderTraversal(root.right)

    def preOrderTraversal(self, root):
        if root is None:
            return

        root.printData()

        if root.left is not None:
            self.preOrderTraversal(root.left)

        if root.right is not None:
            self.preOrderTraversal(root.right)

    def postOrderTraversal(self, root):
        if root is None:
            return

        if root.left is not None:
            self.postOrderTraversal(root.left)

        if root.right is not None:
            self.postOrderTraversal(root.right)

        root.printData()

    def levelOrderTraversal(selfself, root):
        if root is None:
            return

        queue = [root]
        while len(queue):
            node = queue.pop(0)
            node.printData()

            if node.left is not None:
                queue.append(node.left)

            if node.right is not None:
                queue.append(node.right)
        
    def printTree(self, root, level=0):
        if root is None:
            return

        print '\t' * level, root.data

        level = level + 1
        if root.left is not None:
            self.printTree(root.left, level)

        if root.right is not None:
            self.printTree(root.right, level)

    def add(self, data):
        node = TreeNode(data)

        if self.root is None:
            self.root = node
        else:
            current = self.root
            while True:
                if data < current.data:
                    if current.left is None:
                        current.left = node
                        break

                    current = current.left
                else:
                    if current.right is None:
                        current.right = node
                        break
                    current = current.right

    def findRecursive(self, root, data):
        if root is None:
            return False

        if root.data == data:
            return True

        if data < root.data:
            return self.findRecursive(root.left, data)
        else:
            return self.findRecursive(root.right, data)

        return False

    def serialize(self):
        pass

    def deserialize(self, string):
        pass


if __name__ == '__main__':
    t = BinaryTree()
    t.root = TreeNode('Les')
    t.root.left = TreeNode('Cathy')
    t.root.right = TreeNode('Sam')
    t.root.left.left = TreeNode('Alex')
    t.root.left.right = TreeNode('Frank')
    t.root.right.left = TreeNode('Nancy')
    t.root.right.right = TreeNode('Violet')
    t.root.right.right.left = TreeNode('Tony')
    t.root.right.right.right = TreeNode('Wendy')

    print 'In Order traversal: ',
    t.inOrderTraversal(t.getRoot())

    print
    print 'Pre Order traversal: ',
    t.preOrderTraversal(t.getRoot())

    print
    print 'Post Order traversal: ',
    t.postOrderTraversal(t.getRoot())

    print
    print 'Level Order traversal: ',
    t.levelOrderTraversal(t.getRoot())

    print
    print 'Tree structure: ',
    t.printTree(t.getRoot())

    print
    print 'Adding "Zed" :'
    t.add('Zed')
    t.printTree(t.getRoot())

    print
    print 'Finding Frank :', t.findRecursive(t.getRoot(), 'Frank')
    print 'Finding Newton :', t.findRecursive(t.getRoot(), 'Newton')