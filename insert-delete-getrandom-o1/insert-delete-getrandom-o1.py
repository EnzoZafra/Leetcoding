from random import choice

class RandomizedSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.dict = {}
        self.list = []

    def insert(self, val: int) -> bool:
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        """
        if val in self.dict:
            return False
        
        self.dict[val] = len(self.list)
        self.list.append(val)
        
        return True
        

    def remove(self, val: int) -> bool:
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        """
        index = self.dict.get(val, None)
        if index is None:
            return False
        
        last_element = self.list[-1]
        last_element_index = self.dict[last_element]
        
        # swap
        self.dict[last_element] = index
        del self.dict[val]
        
        self.list[index] = last_element
        self.list.pop()
        
        return True
        

    def getRandom(self) -> int:
        """
        Get a random element from the set.
        """
        return choice(self.list)
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()