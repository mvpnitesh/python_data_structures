arr = [1, 4, 20, 3, 10, 5]
sum = 33
j = 0
n = len(arr)
is_found = False
for i in range(n):
    arr_sum = arr[i]
    j = i+1
    while j <= n:
        if arr_sum == sum:
            print ("Sum found between")
            print("indexes % d and % d"%( i, j-1))     
            is_found = True
            break
        if arr_sum > sum or j == n:
            break
        arr_sum = arr_sum + arr[j]
        j += 1
if not is_found:
    print ("No subarray found")