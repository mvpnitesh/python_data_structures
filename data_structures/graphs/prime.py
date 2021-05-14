"""
v=[]
n = 9999
prime = [True] * (n + 1)

p = 2
while p * p <= n:

	# If prime[p] is not changed, 
	# then it is a prime 
	if (prime[p] == True):

		# Update all multiples of p
		for i in range(p * p, n + 1, p):
			prime[i] = False
	p += 1

# Forming a vector of prime numbers
for p in range(1000, n + 1):
if (prime[p]): 
	v.append(p)
"""
primes = []
for n in range(1000,10000):
    count = 1
    for i in range(2,n+1):
        if n%i == 0:
            count+=1
            if count >2:
                break
    if count == 2:
        primes.append(n)
print(primes)

n = 9999
prime = [True] * (n + 1)
v=[]
p = 2
while p * p <= n:

    # If prime[p] is not changed,
    # then it is a prime
    if (prime[p] == True):

        # Update all multiples of p
        for i in range(p * p, n + 1, p):
            prime[i] = False
    p += 1
print("-----------------------")
print(prime)
# Forming a vector of prime numbers
for p in range(1000, n + 1):
    if (prime[p]):
        v.append(p)
print("-----------------------")
print(v)