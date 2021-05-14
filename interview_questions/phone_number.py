dict={'2':['a','b','c'],'3':['d','e','f'],'4':['g','h','i'],'5':['j','k','l'],'6':['m','n','o'],'7':['p','q','r','s'],'8':['t','v','u'],'9':['w','x','y','z']}

given_list = ["foo","bar","baz","foobar","emo","cap","car","cat"]

phone_number = "3662277"

can_have_characters = []
for i in phone_number:
    a = dict[i]
    for j in a:
        if j not in can_have_characters:
            can_have_characters.append(j)

print(can_have_characters)

is_present = []

for word in given_list:
    count = 0
    #import pdb;pdb.set_trace()
    for char in word:
        if char in can_have_characters:
            count+=1
    if count == len(word):
        is_present.append(word)

print(given_list)
print(is_present)