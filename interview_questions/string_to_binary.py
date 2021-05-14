x="1??0?101"
res = []
def genBin(s):
    if '?' in s:
        s1 = s.replace('?','0',1) #only replace once
        s2 = s.replace('?','1',1) #only replace once
        genBin(s1)
        genBin(s2)
    else: res.append(s)
  
# Driver code
genBin("1??0?101")
print(res)
