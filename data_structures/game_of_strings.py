s = "fxnsmkasmlerxxoxhfwviluzttqqotdwrsqfcsxrddicaxahewemjyleudukxzgqrzvvrtmvwvxzuxiyvnngna"
import pdb;pdb.set_trace()
k = 21
a = list(s)
char = {}
for i in a:
	if i in char.keys():
		char[i]=char[i]+1
	else:
		char[i] = 1
import pdb;pdb.set_trace()
c = len(s)
b = a[c-k::]
for i in b:
	char[i] = char[i]-1
import pdb;pdb.set_trace()
sum = 0
for i in char:
	sum = sum+char[i]*char[i]
print(sum)