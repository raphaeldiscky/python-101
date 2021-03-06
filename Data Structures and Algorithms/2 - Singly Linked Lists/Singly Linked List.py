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
            - pointer sum will point to the smaller value of data of the nodes that p and q are pointing to.
            - Once sum points to the smaller value of the data of nodes that p and q point to,
              p or q will move on to the next node in their respective linked list.
            - If sum and p point to the same node, p moves forward; otherwise q moves forward.
            - The final merged linked list will be made from the nodes that sum keeps pointing to.

    8) Remove Duplicates
        a. Algorithm:
            - loop through the linked list once and keep track of all the data held at each of the nodes.
            - use hash table or dictionary to keep track of the data elements that we encounter.
              ex, if we encounter 6, we will add that to the dictionary or hash table and move along.
              Now if we meet another 6 and we check for it in our dictionary or hash table,
              then we???ll know that we already have a 6 and the current node is a duplicate.

    9) Nth-to-Last Noe
        a. Solution 1:
            - calculate the length of the linked list
            - count down from the total length until n is reached
        b. Solution 2:
            - use two pointers p and q
            - p will point to the head node
            - q will point n nodes beyond head node
            - next,  we???ll move these pointers along with the linked list one node at a time.
              When q will reach None, we???ll check where p is pointing, as that is the nod

    10) Count Occurences
        a. Iterative Implementation
        b. Recursive Implementation

    11) Rotate
        shifting or rotating that follows the pivot node to the front of the linked list
        a. Algorithm
            - use two pointer p and q
            - p points to the pivot node while q points to the end of the linked list.
              Then, instead of making it point to None, we make it point to the head of linked list.
              After this step, we achieve a circular linked list.
            - update the head of linked list, which will be the next element after the pivot node,
              as the pivot node has to be the last node.
            - set p.next to None which breaks up the circular linked list and make p the last element

    12) Is Palindrome
        a. Using a string
        b. Using a stack
        c. Using two pointers
            - pointer p will initially point to the head of the list and pointer q to the last node of the list.
            - we'll check the data elements at each of these nodes that are being pointed to by p and q,
              and see if they are equal to each other.
            - if they are, we'll progress p by one, and we'll move q by one in reverse until we get a point where p and q meet
              or can't move any further without crossing

    13) Move Tail to Head
        - use two pointers where one will keep track of the last node of the linkedlist,
          and the other will point to the second-to-last node of the linked list.

    14) Sum Two Linked Lists
        llist1: 3->6->5, llist2: 2->4->8, sum: 613

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
        sum = None

        if not p:
            return q
        if not q:
            return p

        if p and q:
            if p.data <= q.data:
                sum = p
                p = sum.next
            else:
                sum = q
                q = sum.next
            new_head = sum
        while p and q:
            if p.data <= q.data:
                sum.next = p
                sum = p
                p = sum.next
            else:
                sum.next = q
                sum = q
                q = sum.next
        if not p:
            sum.next = q
        if not q:
            sum.next = p

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

    def print_nth_from_last(self, n, method):
        if method == 1:
            # method 1
            total_len = self.len_iterative()
            cur = self.head
            while cur:
                if total_len == n:
                    return cur.data
                total_len -= 1
                cur = cur.next
            if cur is None:
                return

        elif method == 2:
            # method 2
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

    def count_occurences_iterative(self, data):
        count = 0
        cur = self.head
        while cur:
            if cur.data == data:
                count += 1
            cur = cur.next
        return count

    def count_occurences_recursive(self, node, data):
        if not node:
            return 0
        if node.data == data:
            return 1 + self.count_occurences_recursive(node.next, data)
        else:
            return self.count_occurences_recursive(node.next, data)

    def rotate(self, k):
        if self.head and self.head.next:
            p = self.head
            q = self.head
            prev = None
            count = 0

            while p and count < k:
                prev = p
                p = p.next
                q = q.next
                count += 1
            p = prev
            while q:
                prev = q
                q = q.next
            q = prev  # q points to last element in linked list

            q.next = self.head
            self.head = p.next
            p.next = None

    def is_palindrome_1(self):
        # using a string
        sum = ""
        p = self.head
        while p:
            sum += p.data
            p = p.next
        return sum == sum[::-1]  # reverse a string

    def is_palindrome_2(self):
        # using a stack
        p = self.head
        sum = []
        while p:
            sum.append(p.data)
            p = p.next
        p = self.head
        while p:
            data = sum.pop()
            if p.data != data:
                return False
            p = p.next
        return True

    def is_palindrome_3(self):
        # using two pointers
        if self.head:
            p = self.head
            q = self.head
            prev = []

            i = 0
            while q:  # move q to end of linked list
                prev.append(q)
                q = q.next
                i += 1
            q = prev[i-1]

            count = 1

            while count <= i//2 + 1:
                # comparing last element in the prev list, with first element in p
                if prev[-count].data != p.data:
                    return False
                p = p.next
                count += 1
            return True
        else:
            return True

    def is_palindrome(self, method):
        if method == 1:
            return self.is_palindrome_1()
        elif method == 2:
            return self.is_palindrome_2()
        elif method == 3:
            return self.is_palindrome_3()

    def move_tail_to_head(self):
        if self.head and self.head.next:
            last = self.head
            second_to_last = None
            while last.next:
                second_to_last = last
                last = last.next
            # make circular linked list where the last node points to the first element of the linked list
            last.next = self.head
            second_to_last.next = None  # make linear linked list
            self.head = last

    def sum_two_lists(self, llist):
        p = self.head
        q = llist.head

        sum_llist = LinkedList()  # data values of sum_llist will represent the final sum

        carry = 0
        while p or q:
            if not p:
                i = 0
            else:
                i = p.data  # i = current digit picked from the first linked list
            if not q:
                j = 0
            else:
                j = q.data  # j = current digit picked from the second linked list
            sum = i + j + carry
            if sum >= 10:
                print("sum >= 10", sum)
                carry = 1
                remainder = sum % 10
                sum_llist.append(remainder)
            else:

                carry = 0
                sum_llist.append(sum)
            if p:
                p = p.next
            if q:
                q = q.next
        return sum_llist


llist1 = LinkedList()
llist1.append(5)
llist1.append(6)
llist1.append(3)

llist2 = LinkedList()
llist2.append(8)
llist2.append(4)
llist2.append(2)

print(365 + 248)
llist1.sum_two_lists(llist2)

# llist = LinkedList()
# llist.append("A")
# llist.append("B")
# llist.append("C")
# llist.append("D")

# llist.print_list()
# llist.move_tail_to_head()
# print("\n")
# llist.print_list()

# llist = LinkedList()
# llist.append("R")
# llist.append("A")
# llist.append("C")
# llist.append("E")
# llist.append("C")
# llist.append("A")
# llist.append("R")
# print(llist.is_palindrome(3))

# llist = LinkedList()
# llist.append(1)
# llist.append(2)
# llist.append(3)
# llist.append(4)
# llist.append(5)
# llist.append(6)
# llist.rotate(4)
# llist.print_list()

# llist_2 = LinkedList()
# llist_2.append(1)
# llist_2.append(2)
# llist_2.append(1)
# llist_2.append(3)
# llist_2.append(1)
# llist_2.append(4)
# llist_2.append(1)
# print(llist_2.count_occurences_iterative(1))
# print(llist_2.count_occurences_recursive(llist_2.head, 1))

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
