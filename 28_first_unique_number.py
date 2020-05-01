class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None

class FirstUnique(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.head = None
        self.tail = None
        self.key_map = {}
        self.in_obj = set()
        for val in nums:
            self.add(val)

    def showFirstUnique(self):
        """
        :rtype: int
        """
        if self.head == None:
            return -1
        else:
            return self.head.val

    def add(self, value):
        """
        :type value: int
        :rtype: None
        """
        if value in self.key_map:
            # Remove node
            node = self.key_map[value]
            if self.head != node:
                node.prev.next = node.next
            else:
                self.head = node.next
            
            if self.tail != node:
                node.next.prev = node.prev
            else:
                self.tail = node.prev
            del self.key_map[value]
            return
        
        if value in self.in_obj:
            return
        
        self.in_obj.add(value)
        node = Node(value)
        self.key_map[value] = node
        
        if self.head == None:
            self.head = node
            self.tail = node
            return
        
        self.tail.next = node
        node.prev = self.tail
        self.tail = node

