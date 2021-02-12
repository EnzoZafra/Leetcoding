class Solution(object):
    def isRobotBounded(self, instructions):
        """
        :type instructions: str
        :rtype: bool
        """
        curr = [0,0]
        
        # north, east, south, west
        forward_directions = [(1,0), (0,1), (-1,0), (0,-1)]
        curr_direction = 0
        
        for char in instructions:
            if char == 'G':
                movement = forward_directions[curr_direction]
                curr[0] += movement[0]
                curr[1] += movement[1]
            elif char == 'L':
                curr_direction -= 1
                curr_direction = curr_direction % 4
            elif char == 'R':
                curr_direction += 1
                curr_direction = curr_direction % 4
        
        return curr == [0, 0] or curr_direction != 0