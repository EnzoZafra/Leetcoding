class Solution(object):
    def timeToMins(self, t):
        split = t.split(':')
        hours = int(split[0]) * 60
        mins = int(split[1])

        return hours + mins

    def minsToTime(self, mins):
        hour = mins / 60
        minutes = mins % 60

        return str(hour) + ":" + str(minutes)

    def getAvailability(self, s1, s2, block1, block2):
        a1 = []
        a2 = []

        curr = s1[0]
        for i in range(1, len(s1)):
            s = s1[i]

            if i == 1:
                availStart = max(self.timeToMins(block1[0]), self.timeToMins(s[1]))
                availEnd = self.timeToMins(s[0])
            elif i == len(s1) - 1:
                # if last item in calendar, the avail end is max of ends
                availEnd = max(self.timeToMins(block1[1]), self.timeToMins(s[1]))
                availStart = min(self.timeToMins(block1[1]), self.timeToMins(s[1]))
            else:
                availStart = self.timeToMins(curr[1])
                availEnd = self.timeToMins(s[0])

            a1.append([self.minsToTime(availStart), self.minsToTime(availEnd)])
            curr = s

        print(a1)


    def minAvailableDuration(self, slots1, slots2, duration):
        """
        :type slots1: List[List[int]]
        :type slots2: List[List[int]]
        :type duration: int
        :rtype: List[int]
        """

        slots1.sort(key = lambda x: x[0])
        slots2.sort(key = lambda x: x[0])

        ptr1 = 0
        ptr2 = 0


        while ptr1 < len(slots1) and ptr2 < len(slots2):
            meeting1 = slots1[ptr1]
            meeting2 = slots2[ptr2]

            minEnd = min(meeting1[1], meeting2[1])
            maxStart = max(meeting1[0], meeting2[0])

            if minEnd - maxStart >= duration:
                meetingEnd = maxStart + duration
                return [maxStart, meetingEnd]
            else:
                # increment the counter that ends first
                if meeting1[1] < meeting2[1]:
                    ptr1 += 1
                else:
                    ptr2 += 1

        return None

sol = Solution()

s1 = [['9:00', '10:30'], ['12:00', '13:00'], ['16:00', '18:00']]
b1 = ['9:00', '20:00']
s2 = [['10:00', '11:30'], ['11:30', '14:30'], ['14:30', '15:00'], ['16:00','17:00']]
b2 = ['10:00', '18:30']

sol.getAvailability(s1, s2, b1, b2)
