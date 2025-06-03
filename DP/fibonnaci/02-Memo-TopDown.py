def fibonacci_2(n, ht={0:0, 1:1}):
    if n in ht:
        return ht[n]
    else:
        ht[n] = fibonacci_2(n-1,ht) + fibonacci_2(n-2, ht)
        return ht[n]

print(fibonacci_2(6))



def fib_memo(n, ht={0:0, 1:1}):
    if n in ht:
        return ht[n]
    return fib_memo(n-1, ht) + fib_memo(n-2, ht)