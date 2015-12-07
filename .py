def is_prime(number):
	for i in range(2,number):
		if number % i == 0:
			return False
		else:
			return True
	
import random
p = random.randint(5000,10000)
while is_prime(p) == False:
	p = random.randint(5000,10000)

q = random.randint(5000,10000)
while is_prime(q) == False:
	q = random.randint(5000,10000)

n = p * q

totient = (p - 1) * (q - 1)

import math
e = random.randint(1,totient)
while is_prime(e) == False:
	e = random.randint(1,totient)

d = 1.0 / (e % totient)
