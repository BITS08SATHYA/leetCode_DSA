def eraseOverlapIntervals(intervals):
    intervals.sort()
    count = 0
    last = intervals[0][1]
    for i in range(1, len(intervals)):
        if intervals[i][0] < last:
            #overlap
            count += 1
            last = min(last, intervals[i][1])
        # other element is to be removed
        else:
            # no overlap
            last = intervals[i][1]
    return count


arr = [[1,2],[3,4],[5,6]]
print(eraseOverlapIntervals(arr))