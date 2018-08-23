# Uses python3
def calc_fib(n):
	ar = []
	ar.append(1)
	ar.append(1)
#	print(ar[0])
#	print(ar[1])
	for i in range (2,46): 
		x = ar[i-1]+ar[i-2]
		ar.append(x)
#		print(i)
#		print(ar[i])

	if (n <= 1): 
		return n 
	else: 
		return ar[n-1]

n = int(input())

print(calc_fib(n))
