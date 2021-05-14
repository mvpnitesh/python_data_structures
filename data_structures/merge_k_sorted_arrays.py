
"""
a = []
        for i in arr:
            for j in i:
                a.append(j)
        a.sort()
        return a
"""
K = 3
arr = [[1,2,3],[4,5,6],[7,8,9]]
a = []
l = len(arr[0])
for i,j in range(K),range(l):
	import pdb;pdb.set_trace()
	while i < K:
		b = arr[i][j]
		if b < arr[i+1][j]:
			pass
		else:
			b = arr[i+1]
		i+=1
	a.append(b)
print(a)
a.sort()
#return a