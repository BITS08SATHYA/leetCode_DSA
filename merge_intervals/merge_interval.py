def merge_window(intervals):

    intervals.sort(key = lambda x:x[0])

    result = [intervals[0]]

    for start, end in intervals[1:]:
        last_end = result[-1][1]
        if start <= last_end:
            # merging
            result[-1][1] = max(end, last_end)
        else:
            # we add the new array element to the result array
            result.append([start, end])
    return result


# input_intervals = [[2,5],[3,6],[9,11],[20,21]]
input_intervals = [[2,5],[3,6],[9,15],[11,12],[16,18]]
print(merge_window(input_intervals))
