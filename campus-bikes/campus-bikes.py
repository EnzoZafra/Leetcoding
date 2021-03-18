class Solution:
    def manhattan(self, p1, p2):
        return abs(p1[0] - p2[0]) + abs(p1[1]-p2[1])
        
    def assignBikes(self, workers: List[List[int]], bikes: List[List[int]]) -> List[int]:
        
        distances = []
        for i, worker in enumerate(workers):
            for j, bike in enumerate(bikes):
                manhattan_distance = self.manhattan(worker, bike)
                distances.append((manhattan_distance, i, j))
        
        distances.sort(reverse=True)
        seen = set()
        
        out = [-1 for i in range(len(workers))]
        gotbike = 0
        
        while gotbike < len(workers):
            tuple = distances.pop()
            distance = tuple[0]
            worker = tuple[1]
            bike = tuple[2]
            
            if bike not in seen and out[worker] == -1:
                out[worker] = bike
                seen.add(bike)
                gotbike += 1
        
        return out

                