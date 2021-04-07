def DecimalToBinary(num):
     
    #if num >= 1:
    #    DecimalToBinary(num // 2)
    #print(num % 2, end = '')
	import pdb;pdb.set_trace()
	i = num
	binary_number = ''
	while i >1:
		reminder = i%2
		binary_number = binary_number + str(reminder)
		i = i//2
	print (binary_number+'1')
# Driver Code
if __name__ == '__main__':
     
    # decimal value
    dec_val = 15
     
    # Calling function
    DecimalToBinary(dec_val)