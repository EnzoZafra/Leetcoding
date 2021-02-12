class Node(object):
    
    def __init__(self, key=None, val=None):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None

class LRUCache(object):
    # linked hashmap, keep the least recently used at the tail while the new one at the head

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.map = {}
        self.capacity = capacity
        self.length = 0
        self.head = Node()
        self.tail = Node()
        
        self.head.next = self.tail
        self.tail.prev = self.head
    
    def _move_to_head(self, node):
        self._remove_node(node)
        self._add_node_to_head(node)
        
    def _add_node_to_head(self, node):
        temp = self.head.next
        
        self.head.next = node
        temp.prev = node
        node.next = temp
        node.prev = self.head
        
    
    def _remove_node(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev
    
    def _pop_tail(self):
        to_pop = self.tail.prev
        self._remove_node(to_pop)
        
        del self.map[to_pop.key]
        self.length -= 1

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        node = self.map.get(key, None)
        if node:
            self._move_to_head(node)
            return node.val
        
        return -1
        

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        
        if key in self.map:
            # update the value if its already in there.
            node = self.map[key]
            node.val = value
            self._move_to_head(node)
        else:
            # at max capacity, we need to pop
            if self.length == self.capacity:
                self._pop_tail()
            
            new_node = Node(key, value)
            self.length += 1
            self._add_node_to_head(new_node)
            self.map[key] = new_node


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)