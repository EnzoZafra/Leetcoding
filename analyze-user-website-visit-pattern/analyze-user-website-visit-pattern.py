class Solution:
    def mostVisitedPattern(self, username: List[str], timestamp: List[int], website: List[str]) -> List[str]:
        tuples = []
        for i in range(len(username)):
            tuples.append((timestamp[i], website[i], username[i]))
        
        tuples.sort()
        
        nameToSitesMap = collections.defaultdict(list)
        for item in tuples:
            nameToSitesMap[item[2]].append(item[1])
        
        print(nameToSitesMap)
        
        counter = collections.defaultdict(int)
        for u, routes in nameToSitesMap.items():
            for triple in set(itertools.combinations(routes, 3)):
                counter[triple]+=1
       
        toSort = []  
        for tup, count in counter.items():
            toSort.append((count, list(tup)))
        
        toSort.sort(key=lambda x: (-x[0], x[1]))
        print(toSort)
        
        return toSort[0][1]
            
            
