class Solution(object):
    def pancakeFlip(self, sublist, k):
        # perform pancake flip on the prefix of list [0:k]
        i = 0
        while i < k / 2:
            sublist[i], sublist[k-i-1] = sublist[k-i-1], sublist[i]
            i += 1
        
        return sublist
        
    def pancakeSort(self, arr):
        """
        :type arr: List[int]
        :rtype: List[int]
        """
        
        ans = []
        
        # get the largest value
        value_to_sort = len(arr)
        while value_to_sort > 0:
            index = arr.index(value_to_sort)
            
            # put this value at the end of the list
            if index != value_to_sort - 1:
                
                # flip the value to the head if its not there already
                if index != 0:
                    ans.append(index+1)
                    self.pancakeFlip(arr, index+1)
                
                # now that its at the head, flip again to put it in the tail
                ans.append(value_to_sort)
                self.pancakeFlip(arr, value_to_sort)
            
            value_to_sort -= 1
        
        return ans
                   
                
        