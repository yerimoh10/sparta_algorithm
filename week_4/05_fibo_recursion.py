input = 20

# fibo(N) = fibo(n-1) + fibo(n-2)
def fibo_recursion(n):
    # 1 + 1 = 2
    # 1 + 2 = 3
    # 2 + 3 = 5
    # 3 + 5 = 8
    if n == 1 or n == 2:    # 탈출조건
        return 1
    return fibo_recursion(n - 1) + fibo_recursion(n - 2)


print(fibo_recursion(input))  # 6765