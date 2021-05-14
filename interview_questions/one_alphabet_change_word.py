# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.
data = ['cat','cap','mat','map','tap','rat','cab']
source = 'cat'
destination = 'tap'
possible_output = []
data_length=len(data)
#for x in range(0,data_length-1):
current_path=['cat']
import pdb;pdb.set_trace()
for i in range(0,data_length-1):
    if i < data_length:
        first = data[i]
        second = data[i+1]
        first_len = 0
        for j in first:
            if j in second:
                first_len = first_len+1
    if first_len == len(first)-1:
        current_path.append(second)
        #current_path.append(data[i+1])
    if second == destination:
        break
possible_output.append(current_path)
print(possible_output) 
"""
if second == destination:
    least = data_length
    least_set_length = 0
    for x in range(0,len(possible_output)):
        current_set_length = len(possible_output[x])
        if current_set_length < least:
            least_set_length = x
    print (possible_output)
    print (possible_output[least_set_length])
"""