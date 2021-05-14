dict = {"ale", "apple", "monkey", "plea"}   
str = "abpcplea"
#dict = {"pintu", "geeksfor", "geeksgeeks", " forgeek"} 
#str = "geeksforgeeks"
max = 0
max_word = ''
str_list = list(str)
for i in dict:
    count = 0
    for j in i:
        if j in str_list:
            count+=1
    if count == len(i):
        if count > max:
            max = count
            max_word = i
if max:
    print(max_word)
else:
    print('Dict is not having any words which is a substring of given string')