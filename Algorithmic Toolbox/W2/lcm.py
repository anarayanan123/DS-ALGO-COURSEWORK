# Uses python3
import sys

def gcd_naive(a, b):
        if a < b:
                x = a
                a = b
                b = x
        if a == 0:
                return b
        elif b == 0:
                return a
        else:
                a = a%b          
                return gcd_naive(a, b) 

def lcm_naive(a, b):
    for l in range(1, a*b + 1):
        if l % a == 0 and l % b == 0:
            return l
    c = (gcd_naive(a, b))
     #    v = a/(gcd_naive(a, b))*b 
    return c

if __name__ == '__main__':
    input = sys.stdin.read()
    a, b = map(int, input.split())

    print(a//(gcd_naive(a, b))*b)
#    print(a)
#    print(b)
#    print(lcm_naive(a, b))
