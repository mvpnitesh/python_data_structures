A = [ -50, -41, -40, -19, 5, 21, 28 ]
B = [ -50, -21, -10 ,3]
"""
A=[0,23]
B=[]
""" 
array = []

for i in A:
	array.append(i)
for j in B:
	array.append(j)
"""
for i,j in A,B:
    if i>j:
        array.append(j)
        array.append(i)
    else:
        array.append(i)
        array.append(j)
"""
print(array)
array.sort()
length_array = len(array)
if length_array % 2 == 1:
    print(array[length_array//2])
else:
    x = length_array//2
    print((array[x]+array[x-1])/2)


"""

PORT=$(openstack baremetal port list | grep -i '94:40:C9:D6:11:77' | awk '{print $2}')
VIF_PORT_ID=$(openstack port list | grep '94:40:C9:D6:11:77' | awk '{print $2}')

openstack baremetal node vif attach --port-uuid $PORT $NODE $VIF_PORT_ID


https://www.vikramanand.com/jobsmasterclass

 WWN: 207000C0FF3C501B

"""