class Array(object):
	a = []
	def __init__(self, array):
		self.a = array
		
	def find_max_frequency(self):
		dict = {}
		for i in self.a:
			if i in dict.keys():
				dict[i] = dict[i]+1
			else:
				dict[i] = 1
		max = 0
		max_element = None
		for j in dict.keys():
			if dict[j] > max:
				max = j
				max_element = j
		return max_element

arr = Array([1,2,3,4,3,5])
max_frequency_element = arr.find_max_frequency()
print(" Element which has maximum frequency is ", max_frequency_element)
arr = [1,2,3,4,3,5]
max_frequency_element = None
max_frequency = 0	
for i in arr:
    print(i)
    if arr.count(i) > max_frequency:
        max_frequency = arr.count(i)
        max_frequency_element = i
print(max_frequency_element,max_frequency)