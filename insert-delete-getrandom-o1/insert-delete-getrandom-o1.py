from random import choice

class RandomizedSet(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.dict = {}
        self.list = []
        

    def insert(self, val):
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        :type val: int
        :rtype: bool
        """
        if val in self.dict:
            return False
        else:
            self.list.append(val)
            index = len(self.list) - 1
            self.dict[val] = index
            
            return True
    
    def _swap_last_element_to_index(self, index):
        temp = self.list[index]
        
        lastindex = -1
        last_item = self.list[lastindex]
        
        self.list[index] = self.list[lastindex]
        self.list[lastindex] = temp
        self.dict[last_item] = index
    
    def _pop_last_item(self):
        val = self.list.pop()
        del self.dict[val]

    def remove(self, val):
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        :type val: int
        :rtype: bool
        """
        if val not in self.dict:
            return False
        else:
            index = self.dict[val]
            self._swap_last_element_to_index(index) 
            self._pop_last_item()
            return True
        

    def getRandom(self):
        """
        Get a random element from the set.
        :rtype: int
        """
        return choice(self.list)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()