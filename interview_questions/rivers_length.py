rivers = [[1,0,0,1,0],
		  [1,0,1,0,0],
		  [0,0,1,0,1],
		  [1,0,1,0,1],
		  [1,0,1,1,0]]
length_of_rivers = []
x = len(rivers)
y = len(rivers[0])
def find_next(i,j,length):
    print (i,j)
    if rivers[i+1][j] == 1:
        length+=1
        if i+1 < x and j < y:
            find_next(i+1,j,length)
    elif rivers[i][j+1] == 1:
        length+=1
        find_next(i,j+1,length)
    elif rivers[i+1][j+1]==1:
        length+=1
        find_next(i+1,j+1,length)
    else:
        return length
    
for i in range(x-1):
    length = 0
    for j in range(y-1):
        import pdb;pdb.set_trace()
        if rivers[i][j] == 1:
            length+=1
            length = find_next(i,j,length)
        else:
            length_of_rivers.append(length)
            break
print(length_of_rivers)