class Node(object):
    def __init__(self, key, val):
        self.val = val
        self.key = key
        self.next = None
        self.prev = None

class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity = capacity
        self.len = 0
        self.dict = {}
        self.head = Node(-1, -1)
        self.tail = Node(-1, -1)
        self.head.next = self.tail
        self.tail.prev = self.head
        
    def _add_node(self, node):
        # add new nodes after the head
        node.prev = self.head
        node.next = self.head.next
        
        self.head.next.prev = node
        self.head.next = node
    
    def _remove_node(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev
    
    def _move_to_head(self, node):
        # util to move a node to the head, where we keep Most recently used
        self._remove_node(node)
        self._add_node(node)
    
    def _pop_tail(self):
        nodeToBePopped = self.tail.prev
        self._remove_node(nodeToBePopped)
        
        return nodeToBePopped

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        node = self.dict.get(key, None)
        
        if not node:
            return -1
        
        self._move_to_head(node)

        return node.val
        

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        node = self.dict.get(key, None)
        if not node:
            node = Node(key, value)
            self._add_node(node)
            self.dict[key] = node
            if self.len < self.capacity:
                self.len+=1
            else:
                popped = self._pop_tail()
                del self.dict[popped.key]
        else:
            node.val = value
            self._move_to_head(node)
            
            
            
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)