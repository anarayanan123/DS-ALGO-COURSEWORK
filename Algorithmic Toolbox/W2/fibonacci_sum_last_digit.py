# Uses python3
import sys

def fibonacci_sum_naive(n):
    if n <= 1:
        return n

    ar = []
    ar.append(0)
    ar.append(1)
    i = 1
#    print("i: ",i)
#    print("Initial Length",len(ar))
#    print(ar[1])
#    print(ar[0])
    done = False
    previous = 0
    current  = 1
    while (not done):
#        print(i)
        previous, current = current, previous + current
#        print(current)    
        ar.append(current%10)          
        i = i+1
#        print("1:  ",ar[i])
#        print("0:  ",ar[i-1])
        if (ar[i] == 1 and ar[i-1] == 0):    
            done = True
#    print("End Length",len(ar))
    ar.pop(-1)
    ar.pop(-1)
    x = len(ar)
#    print(x)
#    print(current)

    y = (n+2) % x
#    print(y)
    d = ar[y] - 1
    if d == -1:
        d = 9 
    return d 
    
    
if __name__ == '__main__':
    input = sys.stdin.read()
    n = int(input)
    print(fibonacci_sum_naive(n))


    
