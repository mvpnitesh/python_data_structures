
def fib(n):
    arr = [0]*n
    if n>=0:
        arr[0] = 0
    if n>=1:
        arr[1] = 1
    for i in range(2, n):
        arr[i] = arr[i-2]+arr[i-1]
        a = arr[i-1]
        b = arr[i]
    for i in range(n-1,-1,-1):
        print(arr[i], end="  ")
fib(9)