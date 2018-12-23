class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_end(self,val):
        curr = self.head
        to_insert = Node(val)
        if not self.head:
            self.head = to_insert
        while curr.next is not None:
            curr = curr.next 
        curr.next = to_insert

    def insert_at_front(self, val):
        to_insert = Node(val)
        to_insert.next = self.head
        self.head = to_insert

    def get_length(self, val):
        i = 0
        curr = self.head
        while curr:
            i += 1
            curr = curr.next
        return i

    def lookup(self, val):
        curr = self.head
        while curr:
            if curr.val == val:
                return True
        return False

    def pop_front(self):
        if self.head:
            self.head = self.head.next

    def pop_last(self):
        curr = self.head
        if not curr:
            return
        while curr.next.next:
            curr = curr.next
        res = curr.next
        curr.next = None
        return res

    def delete(val):
        if not self.head:
            return

        if self.head.val == val:
            self.head = self.head.next
    
        curr = self.head 
        while curr.next:
            if curr.next.val == val:
                curr.next = curr.next.next
            curr = curr.next:

    def find_center(val):
        if not self.head:
            return None 
        fast = self.head 
        slow = self.head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        return slow 

    def reverse(val):
        next_ptr = None
        prev_ptr = None
        curr_ptr = head
        while curr:
            next_ptr = curr.next 
            curr_ptr.next = prev_ptr
            prev_ptr = curr_ptr
            curr_ptr = next_ptr
        self.head = prev


1 2 3 4 5 


