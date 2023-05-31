class MyHashSet(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.keyRange = 769
        self.bucketArray = [Bucket() for i in range(self.keyRange)]

    def _hash(self, key):
        return key % self.keyRange

    def add(self, key):
        """
        :type key: int
        :rtype: None
        """
        bucketIndex = self._hash(key)
        self.bucketArray[bucketIndex].insert(key)

    def remove(self, key):
        """
        :type key: int
        :rtype: None
        """
        bucketIndex = self._hash(key)
        self.bucketArray[bucketIndex].delete(key)

    def contains(self, key):
        """
        Returns true if this set contains the specified element
        :type key: int
        :rtype: bool
        """
        bucketIndex = self._hash(key)
        return self.bucketArray[bucketIndex].exists(key)

    
class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


class Bucket:
    def __init__(self):
        self.head = Node(0)
    
    
    def insert(self, new_value):
        if not self.exists(new_value):
            new_node = Node(new_value, self.head.next)
            self.head.next = new_node
    
    def delete(self, val):
        prev, curr = self.head, self.head.next
        
        while curr:
            if curr.val == val:
                prev.next = curr.next
                return
            prev = curr
            curr = curr.next


    def exists(self, val):
        curr = self.head.next
        
        while curr:
            if curr.val == val:
                return True
            curr = curr.next

        return False
        

# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)