def recursion(N,arr):


    def findCost(i,j):
        # base case
        if i == j:
            return 0

        # recursive case
        cost = float('inf')
        for k in range(i,j):
            curr_cost = findCost(i,k) + findCost(k+1,j) + arr[i-j]*arr[k]*arr[j]
            cost = min(cost,curr_cost)
        return cost

    return findCost(1, N-1)


arr1 = [2,10,5,4]
print(recursion(4, arr1))