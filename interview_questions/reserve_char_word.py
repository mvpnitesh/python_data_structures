"""
input_sentence = [H,o,w, ,a,b,o,u,t, ,y,o,u, ,m,y, ,f,r,i,e,n,d]
input_sentence = “How about you my friend”
import pdb;
pdb.set_trace()
length_sentence = len(input_sentence)
starting_char = 0
ending_char = 0
for i in range(length_sentence):
    char = input_sentence[i]
    if char !=' ' and i!=N:
        pass
    else:
        import pdb;
        pdb.set_trace()
        ending_char = i-1
        input_sentence[i-1] = input_sentence[starting_char]
        input_sentence[starting_char] = input_sentence[ending_char]
        starting_char = i+1
print(input_sentence)
"""
with open("input.txt") as f:
    starting_char = 0
    while 1:
        c = f.read(1)
        if not c:
            break
        elif c != ' ':
            starting_char+=1
        else:
            print(starting_char)
            str = f.read(-starting_char)
            starting_char = 0
            print (str)
        #print(c)