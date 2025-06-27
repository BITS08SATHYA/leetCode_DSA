def twoCitySchedCost(costs):
    costs.sort(key = lambda x:x[0] - x[1])
    cost = 0
    n = len(costs)
    for i in range(n//2):
        cost += costs[i][0]

    for i in range(n//2,n):
        cost += costs[i][1]

    return cost


costs = [[20,700],[400,50],[900,600],[200,150]]
print(twoCitySchedCost(costs))