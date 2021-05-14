arr = [0, -1, 2, -3, 1]
arr = [1, -2, 1, 0, 5]
len_arr = len(arr)
len_arr = len_arr-2
triplets = []
print(len_arr)
for i in range(len_arr):
    new_arr = arr.copy()
    a = arr[i]
    b = arr[i+1]
    new_arr.remove(a)
    new_arr.remove(b)
    for next_number in new_arr:
        if (a + b + next_number) == 0:
            print ("New triplets are ", a,b,next_number)
            
            """ 
            import pdb;pdb.set_trace()

            for t in triplets:
                if a in triplets[i] and b in triplets[i] and j in triplets[i]:
                    pass
                else:
                    triplets.append([a,b,j])"""

print (triplets)