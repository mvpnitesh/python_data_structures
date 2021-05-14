a={1:1,2:5,3:8,4:9,5:10,6:17,7:17,8:20}
max = 0
key = 0
for i in a.keys():
    print(i)
    if 8-i>0:
        if a[i] + a[8-i] > max:
            max = a[i] +a[8-i]
            key = i
print(a[key],a[8-key],max)

