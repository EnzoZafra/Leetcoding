# given a list of blocks, containing information whether there is a building (office, school, gym) in that block,
# find the apartment that minimizes the farthest distance you need to walk to each building

# question in https://www.youtube.com/watch?v=rw4s4M3hFfs

blocks = [
    {
        "gym": False,
        "school": True,
        "store": False
    },
    {
        "gym": True,
        "school": False,
        "store": False
    },
    {
        "gym": True,
        "school": True,
        "store": False
    },
    {
        "gym": False,
        "school": True,
        "store": False
    },
    {
        "gym": False,
        "school": True,
        "store": True
    }
]

requirements1 = ["gym", "school", "store"]
requirements2 = ["gym", "school"]
requirements3 = ["gym"]

out1 = 3 # at index 3, the min distance to walk is 1, which is to walk to index 4 for store, stay for school and index 2 for gym


# O(nk) where n = len of blocks and r = len(requirements)
def getApartmentMinDistance(blocks, requirements):
    dist = [[float('inf') for _ in range(len(requirements))] for x in range(len(blocks))]

    # left scan
    for i in range(len(blocks)):  # O(n) where n = len(blocks)
        block = blocks[i]
        for r in range(len(requirements)):   # O(k) where k = len(requirements)
            requirement = requirements[r]
            if block[requirement]:
                dist[i][r] = 0
            else:
                if i-1 >= 0 and dist[i-1] != float('inf'):
                    dist[i][r] = dist[i-1][r] + 1

    minDistance = float('inf')
    minDistanceIndex = -1
    # right scan, take the min of left scan and right scan, also calculate the max
    for i in range(len(blocks) - 1, -1, -1):
        block = blocks[i]
        maxDistInRequirements = -1
        for r in range(len(requirements)):
            requirement = requirements[r]
            if block[requirement]:
                dist[i][r] = 0
            else:
                if i+1 < len(blocks) and dist[i+1] != float('inf'):
                    rightscan = dist[i+1][r] + 1
                    dist[i][r] = min(rightscan, dist[i][r])

            maxDistInRequirements = max(maxDistInRequirements, dist[i][r])

        if minDistance > maxDistInRequirements:
            minDistance = maxDistInRequirements
            minDistanceIndex = i

    print(minDistanceIndex)
    return minDistanceIndex


getApartmentMinDistance(blocks, requirements1)
getApartmentMinDistance(blocks, requirements2)
getApartmentMinDistance(blocks, requirements3)


