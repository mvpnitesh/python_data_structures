#No of occurances in an array
array = [1,2,3,4,4, 3, 2, 1,4,4,4]
occurance_dict ={}
most_occurance = 0
for i in array:
    if i in occurance_dict.keys():
        occurance_dict[i] = occurance_dict[i] + 1
    else:
        occurance_dict[i] = 1

for i in occurance_dict.keys():
    if occurance_dict[i] > most_occurance:
		most_occurance = occurance_dict[i]
		most_occuranced_number  = i
print (most_occuranced_number)



0.08sec 89.024