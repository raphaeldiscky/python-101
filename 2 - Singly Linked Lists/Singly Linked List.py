'''
    1) Insert Elements
        a. append = insert an element at the end of the linked list
        b. prepend = insert an element at the beginning of the linked list
        c. insert_after_node = insert an element after a given node

    2) Deletion by Value
        a. Node to be deleted is head.
            - update head to the next node of the previous head
            - delete the previous head node
        b. Node to be deleted is not head.
            - we want to delete Node B
            - previous node of Node B will point to the next node of Node B
            - delete the Node B

    3) Deletion by Index
        a. Node to be deleted is at index 0
        b. Node to be deleted is not at index 0
    
    4) Calculate the Length
        a. Iterative implementation
        b. Recursive Implementation

    5) Swap Two Nodes
        a. Node 1 and Node 2 are not head nodes
        b. Either Node 1 or Node 2 is a head nodes
    
    6) Reverse a Linked List
        a. Iterative implementation
        b. Recursive Implementation
    
    7) Merge Two Sorted Linked Lists
        a. Assumption:
            - Each of the sorted linked lists will contain at least one element.
            - Create a third linked list which is also sorted.
            - The two linked lists given will no longer be available in their original form, 
              and only one linked list which includes both their nodes will remain.
        b. Algorithm:
            - two pointer (p and q) which will each initially point to the head node of each linked list.
            - pointer s will point to the smaller value of data of the nodes that p and q are pointing to.
            - Once s points to the smaller value of the data of nodes that p and q point to, 
              p or q will move on to the next node in their respective linked list.
            - If s and p point to the same node, p moves forward; otherwise q moves forward.
            - The final merged linked list will be made from the nodes that s keeps pointing to.
    
    8) Remove Duplicates
        a. Algorithm:
            - loop through the linked list once and keep track of all the data held at each of the nodes.
            - use hash table or dictionary to keep track of the data elements that we encounter.
              ex, if we encounter 6, we will add that to the dictionary or hash table and move along.
              Now if we meet another 6 and we check for it in our dictionary or hash table, 
              then we’ll know that we already have a 6 and the current node is a duplicate.

    9) Nth-to-Last Noe
        a. Solution 1:
            - calculate the length of the linked list
            - count down from the total length until n is reached
        b. Solution 2:
            - use two pointers p and q
            - p will point to the head node
            - q will point n nodes beyond head node
            - next,  we’ll move these pointers along with the linked list one node at a time. 
              When q will reach None, we’ll check where p is pointing, as that is the nod
'''


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def print_list(self):
        cur_node = self.head
        while cur_node:
            print(cur_node.data)
            cur_node = cur_node.next

    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

    def prepend(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_after_node(self, prev_node, data):
        if not prev_node:
            print("Previous node does not exist")
            return
        new_node = Node(data)
        new_node.next = prev_node.next
        prev_node.next = new_node

    def delete_node(self, key):
        cur_node = self.head
        # if delete head node
        if cur_node and cur_node.data == key:
            self.head = cur_node.next
            cur_node = None
            return

        # if delete non head node
        prev = None
        while cur_node and cur_node.data != key:
            prev = cur_node
            cur_node = cur_node.next
        if cur_node is None:
            return
        prev.next = cur_node.next
        cur_node = None

    def delete_not_at_index(self, index):
        if self.head:
            cur_node = self.head
            if index == 0:
                self.head = cur_node.next
                cur_node = None
                return

        prev = None
        count = 0
        while cur_node and count != index:
            prev = cur_node
            cur_node = cur_node.next
            count += 1
        if cur_node is None:
            return
        prev.next = cur_node.next
        cur_node = None

    def len_iterative(self):
        count = 0
        cur_node = self.head
        while cur_node:
            count += 1
            cur_node = cur_node.next
        return count

    def len_recursive(self, node):
        if node is None:
            return 0
        return 1 + self.len_recursive(node.next)

    def swap_nodes(self, key_1, key_2):
        if key_1 == key_2:
            return

        prev_1 = None
        curr_1 = self.head
        while curr_1 and curr_1.data != key_1:
            prev_1 = curr_1
            curr_1 = curr_1.next

        prev_2 = None
        curr_2 = self.head
        while curr_2 and curr_2.data != key_2:
            prev_2 = curr_2
            curr_2 = curr_2.next

        if not curr_1 or not curr_2:
            return

        if prev_1:
            prev_1.next = curr_2  # if curr_1 is not head, swap
        else:
            self.head = curr_2  # if curr_1 is head, swap
        if prev_2:
            prev_2.next = curr_1
        else:
            self.head = curr_1

        curr_1.next, curr_2.next = curr_2.next, curr_1.next

    def reverse_iterative(self):
        prev = None
        cur = self.head
        while cur:
            nxt = cur.next
            cur.next = prev  # flip arrow
            prev = cur
            cur = nxt
        self.head = prev  # prev is last node, then set head = prev

    def reverse_recursive(self):
        def _reverse_recursive(cur, prev):
            if not cur:
                return prev

            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = nxt
            return _reverse_recursive(cur, prev)

        self.head = _reverse_recursive(cur=self.head, prev=None)

    def merge_sorted(self, llist):
        p = self.head
        q = llist.head
        s = None

        if not p:
            return q
        if not q:
            return p

        if p and q:
            if p.data <= q.data:
                s = p
                p = s.next
            else:
                s = q
                q = s.next
            new_head = s
        while p and q:
            if p.data <= q.data:
                s.next = p
                s = p
                p = s.next
            else:
                s.next = q
                s = q
                q = s.next
        if not p:
            s.next = q
        if not q:
            s.next = p

        self.head = new_head
        return self.head

    def remove_duplicates(self):
        cur = self.head
        prev = None
        dup_values = {}  # dictionary

        while cur:
            if cur.data in dup_values:
                # remove node
                prev.next = cur.next
                cur = None
            else:
                # have not encountered element before
                dup_values[cur.data] = 1  # assign 1 as value
                prev = cur
            cur = prev.next  # to traverse the linked list

    def print_nth_from_last1(self, n):
        total_len = self.len_iterative()

        cur = self.head
        while cur:
            if total_len == n:
                print(cur.data)
                return cur.data
            total_len -= 1
            cur = cur.next
        if cur is None:
            return

    def print_nth_from_last2(self, n):
        p = self.head
        q = self.head

        if n > 0:
            count = 0
            while q:
                count += 1
                if(count >= n):
                    break
                q = q.next

            if not q:
                print(str(n) + " is greater than the number of nodes in lists.")
                return

            while p and q.next:
                p = p.next
                q = q.next
            return p.data
        else:
            return None


# llist.insert_after_node(llist.head.next, "Z")
# llist.insert_after_node(llist.head, "ZZ")

# llist.delete_node("B")
# llist.delete_node("D")
# llist.delete_not_at_index(2)

# print(llist.len_iterative())
# print(llist.len_recursive(llist.head))


# llist.swap_nodes("B", "C")
# print("Swapping nodes B and C that are not head nodes")
# llist.print_list()
# llist.swap_nodes("A", "B")
# print("Swapping nodes A and B where key_1 is head node")
# llist.print_list()
# llist.swap_nodes("D", "B")
# print("Swapping nodes D and B where key_2 is head node")
# llist.print_list()
# llist.swap_nodes("C", "C")
# print("Swapping nodes C and C where both keys are same")

# llist.reverse_iterative()
# llist.reverse_recursive()

# llist_1 = LinkedList()
# llist_2 = LinkedList()
# llist_1.append(1)
# llist_1.append(5)
# llist_1.append(7)
# llist_1.append(9)
# llist_1.append(10)
# llist_2.append(2)
# llist_2.append(3)
# llist_2.append(4)
# llist_2.append(6)
# llist_2.append(8)
# llist_1.merge_sorted(llist_2)
# llist_1.print_list()

# llist = LinkedList()
# llist.append(1)
# llist.append(6)
# llist.append(1)
# llist.append(4)
# llist.append(2)
# llist.append(2)
# llist.append(4)
# print("Original Linked List")
# llist.print_list()
# print("Linked List After Removing Duplicates")
# llist.remove_duplicates()
# llist.print_list()
