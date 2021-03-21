class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        ans = []
        
        for asteroid in asteroids:
            while ans and asteroid < 0 < ans[-1]:
                
                # if there is a collition and the new one is bigger
                if abs(ans[-1]) < abs(asteroid):
                    ans.pop()
                    continue
                elif abs(ans[-1]) == abs(asteroid):
                    ans.pop()
                break
            else:
                ans.append(asteroid)
    
        return ans