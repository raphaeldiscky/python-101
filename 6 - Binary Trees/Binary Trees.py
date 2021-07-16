'''
    1) Traversal Algorithm
        a. Pre-order traversal
            - check if the current node is null
            - display the data part of the root (or current node)
            - traverse the left subtree by recursively calling the pre-order method
            - traverse the right subtree by recursively calling the pre-order method
        b. In-order Traversal
            - check if the current node is null
            - traverse the left subtree by recursively calling the pre-order method
            - display the data part of the root (or current node)
            - traverse the right subtree by recursively calling the pre-order method
        c. Post-order Traversal
            - check if the current node is null
            - traverse the left subtree by recursively calling the pre-order method
            - traverse the right subtree by recursively calling the pre-order method
            - display the data part of the root (or current node)
    
    2) Level Order Traversal
        require a queue (last element = front, first element = back)
        - enqueue root node
        - dequeue from the queue and add it to traversal
        - enqueue the children of the node we dequeue
        - dequeue from the queue and add it to traversal, enqueue its children again
        - repeat until queue == 0
'''

from Queue import Queue


class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinaryTree(object):
    def __init__(self, root):
        self.root = Node(root)

    def print_tree(self, traversal_type):
        if traversal_type == "preorder":
            return self.preorder_print(tree.root, "")
        elif traversal_type == "inorder":
            return self.inorder_print(tree.root, "")
        elif traversal_type == "postorder":
            return self.postorder_print(tree.root, "")
        elif traversal_type == "levelorder":
            return self.levelorder_print(tree.root)
        else:
            print("Traversal type " + str(traversal_type) + " is not supported.")
            return False

    def preorder_print(self, start, traversal):
        '''root --> left --> right'''
        if start:
            traversal += (str(start.value) + '-')
            traversal = self.preorder_print(start.left, traversal)
            traversal = self.preorder_print(start.right, traversal)
        return traversal

    def inorder_print(self, start, traversal):
        '''left --> root --> right'''
        if start:
            traversal = self.inorder_print(start.left, traversal)
            traversal += (str(start.value) + '-')
            traversal = self.inorder_print(start.right, traversal)
        return traversal

    def postorder_print(self, start, traversal):
        '''left --> root --> right'''
        if start:
            traversal = self.postorder_print(start.left, traversal)
            traversal = self.postorder_print(start.right, traversal)
            traversal += (str(start.value) + '-')
        return traversal

    def levelorder_print(self, start):
        if start is None:
            return

        queue = Queue()
        queue.enqueue(start)

        traversal = ""
        while len(queue) > 0:
            traversal += str(queue.peek()) + "-"
            node = queue.dequeue()

            if node.left:
                queue.enqueue(node.left)
            if node.right:
                queue.enqueue(node.right)
        return traversal

#               1
#           /       \
#          2          3
#         /  \      /   \
#        4    5     6   7


tree = BinaryTree(1)
tree.root.left = Node(2)
tree.root.right = Node(3)
tree.root.left.left = Node(4)
tree.root.left.right = Node(5)

print(tree.print_tree("levelorder"))

# print(tree.print_tree("preorder"))
# print(tree.print_tree("inorder"))
# print(tree.print_tree("postorder"))
