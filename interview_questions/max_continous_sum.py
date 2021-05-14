a = [-2, -3, 4, -1, -2, 1, 5, -3]
max_so_far = 0
max_ending_here = 0
for i in a:
    max_ending_here = max_ending_here+i
    if max_so_far < max_ending_here:
        max_so_far = max_ending_here
    if max_ending_here < 0:
        max_ending_here = 0
print(max_so_far)
    