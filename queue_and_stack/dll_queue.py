import sys
sys.path.append('../doubly_linked_list')
from doubly_linked_list import DoublyLinkedList


class Queue:
    def __init__(self):
        self.size = 0
        # Why is our DLL a good choice to store our elements? Serialize data coming in from multiple sources/ can be travesed in both forward and backward direction/ more efficient
        self.storage = []


    """add(an item of data awaiting processing) to a queue of such items"""
    def enqueue(self, value):
        # value.insert(0, value)
        self.storage.insert(0, value)
        self.size += 1 #size of the queue increases

    """remove(and item of data awaiting processing) from a queue of such items"""
    def dequeue(self):
        #return self.value.pop()
        if self.size == 0:
            return 
        else:
            self.size -= 1
            return self.storage.pop()

    def len(self):
        #return len(value)/returning the number of items in the queue
        return self.size

"""
Solution from Lecture:

    def __init__(self):
        self.size = 0
        self.storage = DoublyLinkedList()
        
    def push(self, value):
        #pushing to stack
        self.size += 1
           self.storage.add_to_head(value)
        
    def pop(self):
        if self.size > 0:
            self.size -= 1
            return self.storage.remove_from_tail()
            #remove from the opposite in a queue
        else:
            return None

    def len(self):
        return self.size

 """