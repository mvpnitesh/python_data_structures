s='leetcode'
l = list(s)
print(l)
unique = False
for char in l:
    count = 0
    #import pdb;pdb.set_trace()
    for i in l:
        if char == i:
            count+=1
    if count == 1:
        print(char)
        print(l.index(char))
        if not unique:
            unique = True
            break
if not unique:
	print(-1)