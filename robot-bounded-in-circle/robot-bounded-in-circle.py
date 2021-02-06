class Solution(object):
    def isRobotBounded(self, instructions):
        """
        :type instructions: str
        :rtype: bool
        """
        # the robot is in a circle iff it changes direction or it goes back to zero
        
        curr = [0, 0]
        directions = ['N', 'E', 'S', 'W']        # clockwise order
        forward_list = [(1,0), (0, 1), (-1, 0), (0, -1)]
        curr_direction_idx = 0 
        
        for char in instructions:
            if char == 'G':
                # move forward
                movement = forward_list[curr_direction_idx]
                curr[0] += movement[0]
                curr[1] += movement[1]
                 
            elif char == 'L':
                # 90* left 
                if curr_direction_idx == 0:
                    curr_direction_idx = 3
                else:
                    curr_direction_idx -= 1 
            elif char == 'R':
                # 90* right
                if curr_direction_idx == 3:
                    curr_direction_idx = 0
                else:
                    curr_direction_idx += 1
        
        return curr == [0, 0] or curr_direction_idx != 0
        
        