#Uses python3

import sys

def max_dot_product(a, b):
    #write your code here


    res = 0
    maxprod = []
    for i in range(len(a)):
        maxa = max(a)
        maxb = max(b)
        
        a.remove(maxa)
        b.remove(maxb)
        
        maxprod.append(maxa*maxb)
    return sum(maxprod)

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    a = data[1:(n + 1)]
    b = data[(n + 1):]
    print(max_dot_product(a, b))
    
