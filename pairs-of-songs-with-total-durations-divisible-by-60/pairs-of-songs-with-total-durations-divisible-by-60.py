class Solution:
    def printArr(self, arr):
        for i, num in enumerate(arr):
            if num:
                print(i, num)
                
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        
        count = 0
        arr = [0 for _ in range(61)]
        for x in time:
            modded = x % 60
            if modded == 0:
                count += arr[0]
            else:
                diff = 60 - modded
                count += arr[diff]
            arr[modded] += 1
        
        return count 