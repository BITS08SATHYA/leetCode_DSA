def insert(intervals, newInterval):
    res = []

    for i in range(len(intervals)):
        # newInterval is before the current
        if newInterval[1] < intervals[i][0]:
            res.append(newInterval)
            return res + intervals[i:]
        elif newInterval[0] > intervals[i][1]:
            res.append(intervals[i])
        # merge case
        else:
            # [start1, end1] [start2, end2]
            newInterval[0] = min(newInterval[0], intervals[i][0])
            newInterval[1] = max(newInterval[1], intervals[i][1])

    res.append(newInterval)

    return res


arr = [[1,2],[3,4],[5,6]]
newInterval = [3,7]

print(insert(arr, newInterval))