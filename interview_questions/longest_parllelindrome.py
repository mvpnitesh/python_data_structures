string = "forgeeksskeegfor"
length = len(string)
if length%2 == 0:
    middle = int(length/2)-1
    middle_next = middle+1
else:
    middle = int(length//2)
    middle_next = middle
print(middle)

while middle > 0:
    if string[middle] == string[middle_next]:
        middle = middle - 1
        middle_next = middle_next+1
    else:
        break
print(string[middle+1:middle_next])
print("-------------------------")
def strBruteForce(str,pattern):
    if not pattern: return 0
    for i in range(len(str)-len(pattern)+1):
        stri = i
        patterni = 0
        while stri < len(str) and patterni < len(pattern) and str[stri] == pattern[patterni]:
            stri+=1
            patterni+=1
        if patterni == len(pattern): return i
    return -1

print(strBruteForce("xxxxxyzabcdabcdefabc","abc"))


string = "xxxxxyzabcdabcdefabc"
print(string.rfind("abc"))

