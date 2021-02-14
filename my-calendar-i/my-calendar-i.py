class Node(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
        self.left = None
        self.right = None
        
    def insert(self, node):
        # when we're inserting a meeting, we can only insert if:
        # 1. it starts after this meeting
        # 2. it ends before this meeting
        
        if node.start >= self.end:
            if not self.right:
                self.right = node
                return True
            return self.right.insert(node)
        
        elif node.end <= self.start:
            if not self.left:
                self.left = node
                return True
            return self.left.insert(node)
        else:
            return False

class MyCalendar(object):

    def __init__(self):
        self.root = None

    def book(self, start, end):
        """
        :type start: int
        :type end: int
        :rtype: bool
        """
        node = Node(start, end)
        
        if self.root is None:
            self.root = Node(start, end)
            return True
        else:
            return self.root.insert(node)
        


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)