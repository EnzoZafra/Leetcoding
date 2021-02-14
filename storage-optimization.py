# https://leetcode.com/discuss/interview-question/1021429/Amazon-OA-or-storage-optimization

def get_max_dist(bars):
    maxCut = 0
    count = 0
    for has_bar in bars:
        # if there is a bar, see if the size of the hole is bigger than the max
        if has_bar:
            maxCut = max(maxCut, count)
            count = 1
        else:
            count += 1

    # do another max because we might encounter a case where the last bar is cut and we never max
    maxCut = max(maxCut, count)

    return maxCut


def storage_optimization(n, m, h, v):
    horizontal_bars = [True for _ in range(n+1)]
    vertical_bars = [True for _ in range(m+1)]

    for horizontal_cut in h:
        horizontal_bars[horizontal_cut] = False

    for vertical_cut in v:
        vertical_bars[vertical_cut] = False

    maxHorizontalCut = get_max_dist(horizontal_bars)
    maxVerticalCut = get_max_dist(vertical_bars)

    return maxVerticalCut * maxHorizontalCut * 1



result = storage_optimization(6, 6, [4], [2])
print(result)

result = storage_optimization(3, 3, [2], [2])
print(result)

result = storage_optimization(2, 2, [1], [2])
print(result)

result = storage_optimization(3, 2, [1,2,3], [1,2])
print(result)
