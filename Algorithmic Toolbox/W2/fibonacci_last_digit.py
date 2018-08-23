# Uses python3
#import sys

def get_fibonacci_last_digit_naive(n):
	ar = []
	ar.append(1)
	ar.append(1)
#	print(ar[0])
#	print(ar[1])
	for i in range (2,n+1): 
		x = (ar[i-1] +ar[i-2]) % 10 
		ar.append(x)
#		print(i)
#		print(ar[i])

	if (n <= 1): 
		return n 
	else: 
		return ar[n-1]

#if __name__ == '__main__':
    #input = sys.stdin.read()
n = int(input())
print(get_fibonacci_last_digit_naive(n))


