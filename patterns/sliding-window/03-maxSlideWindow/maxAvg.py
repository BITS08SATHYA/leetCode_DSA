from collections import deque
def maxSlidingWindow(nums, k):
    # write code here
    dq = deque()
    output = []

    for i in range(k):
        while dq and nums[i] >= nums[dq[-1]]:
            dq.pop()
        dq.append(i)
    output.append(nums[dq[0]])

    for i in range(k, len(nums)):
        # decide whether dq[0] is out of the window
        if dq and dq[0] == i - k:
            dq.popleft()
        # insert i into deque
        while dq and nums[i] >= nums[dq[-1]]:
            dq.pop()
        dq.append(i)
        output.append(nums[dq[0]])

    return output

nums = [2, 3, -2, -4, 5, 2, 8, 11]
nums1 = [3, 2, 1, 4, -4, 5, -6, 8, 12]
# k = 3
k = 4
print(maxSlidingWindow(nums1, k))