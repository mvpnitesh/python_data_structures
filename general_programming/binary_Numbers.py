bin_num = ['1']
N = int(input('Enter the value of N till which you need binary number'))
"""
for i in range(2,N+1):
	binary_number = '1'
	while i >1:
		reminder = i%2
		if reminder == 0:
			binary_number = binary_number + '0'
		else:
			binary_number = binary_number + '1'
		i = i//2
	bin_num.append(binary_number) 
print(bin_num)
"""
for i in range(1,N+1):
	print(bin(i).replace('0b',''))