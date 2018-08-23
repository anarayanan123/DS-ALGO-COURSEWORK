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

if __name__ == "__main__":
    input = sys.stdin.read()
    a, b = map(int, input.split())
    print(gcd_naive(a, b))
