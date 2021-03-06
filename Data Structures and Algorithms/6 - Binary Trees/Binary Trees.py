''' 
    Binary Tree = tree data structure in which each node has at most two children, 
    which are referred to as the left child and the right child.
    1) Traversal Algorithm (DFS), time = O(n)
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

    2) Level-Order Traversal (BFS), time = O(n)
        require a queue (last element = front, first element = back)
        - enqueue root node
        - dequeue from the queue and add it to traversal
        - enqueue the children from left child to right child of the node we dequeue
        - dequeue from the queue and add it to traversal, enqueue its children again
        - repeat until queue empty

    3) Reverse Level-Order Traversal
        using queue with a slight tweak (enqueue the right child, then the left child) and using stack
        - enqueue root node
        - dequeue from the queue and push to stack
        - enqueue the children (right then left)
        - repeat until queue empty
        - pop the stack
    
    4) Calculating the Height of a Binary Tree
        recursive approach
    
    5) Calculating the Size of a Tree
        size of three = total number of nodes in a tree
        a. Iterative Approach
            - push to stack and increment size by 1
            - pop top of stack and push their children on to the stack, for every push increment size by 1
            - repeat until stack empty
        b. Recursive Approach

'''

from Queue import Queue
from Stack import Stack


class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinaryTree(object):
    def __init__(self, root):
        self.root = Node(root)

    def print_tree(self, traversal_type):
        # recursive traversal
        if traversal_type == "preorder":
            return self.preorder_print(tree.root, "")
        elif traversal_type == "inorder":
            return self.inorder_print(tree.root, "")
        elif traversal_type == "postorder":
            return self.postorder_print(tree.root, "")

        # iterative traversal
        elif traversal_type == "levelorder":
            return self.levelorder_print(tree.root)
        elif traversal_type == "reverse_levelorder":
            return self.reverse_levelorder_print(tree.root)
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

    def reverse_levelorder_print(self, start):
        if start is None:
            return

        queue = Queue()
        stack = Stack()
        queue.enqueue(start)

        traversal = ""
        while len(queue) > 0:
            node = queue.dequeue()
            stack.push(node)

            if node.right:
                queue.enqueue(node.right)
            if node.left:
                queue.enqueue(node.left)

        while len(stack) > 0:
            node = stack.pop()
            traversal += str(node.value) + "-"

        return traversal

    def height(self, node):
        if node is None:
            return -1  # will return 0 because 1 + -1 is 0

        left_height = self.height(node.left)
        right_height = self.height(node.right)

        return 1 + max(left_height, right_height)

    def size_iterative(self):
        if self.root is None:
            return 0

        stack = Stack()
        stack.push(self.root)
        size = 1
        while stack:
            node = stack.pop()
            if node.left:
                size += 1
                stack.push(node.left)
            if node.right:
                size += 1
                stack.push(node.right)
        return size

    def size_recursive(self, node):
        if node is None:
            return 0
        return 1 + self.size_recursive(node.left) + self.size_recursive(node.right)


#     1
#    / \
#   2  3
#  / \
# 4  5
#
tree = BinaryTree(1)
tree.root.left = Node(2)
tree.root.right = Node(3)
tree.root.left.left = Node(4)
tree.root.left.right = Node(5)

print(tree.size_iterative())
print(tree.size_recursive(tree.root))
