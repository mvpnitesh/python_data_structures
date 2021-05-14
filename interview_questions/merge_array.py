
ar1 = [1,3 ,5,7]
ar2 = [0,2,6,8,9]

m = len(ar1)
n = len(ar2)

a = ar1 + ar2
a.sort()
print(a)
b= [None] * (m + n)
i = 0
j =0
k = 0 
while i < m and j < n:
    if ar1[i] < ar2[j]:
        b[k] = ar1[i]
        i+=1
    else:
        b[k] = ar2[j]
        j+=1
    k=k+1
while i<m: 
    b[k] = ar1[i]
    i+=1
    k+=1
while j<n:
    b[k] = ar2[j]
    j+=1
    k+=1
#b = b+ ar1[i:]+ar2[j:]
print(b)

"""
if len(ar2)>len(ar1):
    ar1 ,ar2 = ar2,ar1
import pdb;pdb.set_trace()
a = []
for i in ar1:
    for j in ar2:
        print(ar1[i],ar2[j])
        if ar1[i] > ar2[j]:
            a.append(ar2[j])
            a.append(ar1[i])
            break
        else:
            a.append(ar1[i])
            a.append(ar2[j])
            break

print(a)

for i in range(n-1, -1, -1):
 
    # Find the smallest element
    # greater than ar2[i]. Move all
    # elements one position ahead
    # till the smallest greater
    # element is not found
    last = ar1[m-1]
    j=m-2
    while(j >= 0 and ar1[j] > ar2[i]):
        ar1[j+1] = ar1[j]
        j-=1

    # If there was a greater element
    if (j != m-2 or last > ar2[i]):
     
        ar1[j+1] = ar2[i]
        ar2[i] = last
        
print(ar1,ar2)

for k in range(len(a)):
    if  a[i] > b[k]:
        pass
    else:
        b[k::] = b[k-1::]
        b[k-1] = a[i]
"""