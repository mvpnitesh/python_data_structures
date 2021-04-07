#Sum of digits in a number and till the sum is less than 10
#number 147=1+4+7=12=1+2=3
number = 143
def sum_nitesh(number):
    sum_number = 0
    while(number> 10):
        sum_number = number%10 + sum_number
        number = number //10
    sum_number = sum_number + number
    return sum_number
a = sum_nitesh(number)
while(a > 10):
    a = sum_nitesh(a)
print(a)