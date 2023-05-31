class MyHashSet(object):
    def __init__(self):
        self.key = 769
        self.buckets = [Bucket() for _ in range(self.key)]


    def hash(self, key):
        return key % self.key


    def add(self, key):
        bucketIndex = self.hash(key)
        self.buckets[bucketIndex].insert(key)


    def remove(self, key):
        bucketIndex = self.hash(key)
        self.buckets[bucketIndex].delete(key)


    def contains(self, key):
        bucketIndex = self.hash(key)
        return self.buckets[bucketIndex].exists(key)


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