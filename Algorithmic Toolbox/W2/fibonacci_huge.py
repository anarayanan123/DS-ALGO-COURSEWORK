# Uses python3
import sys

def get_fibonacci_huge_naive(n, m):
    if n <= 1:
        return n

    previous = 0
    current  = 1

    for _ in range(n - 1):
        previous, current = current, previous + current

    return current % m

def get_fibonacci_huge_smart(n, m):
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
        ar.append(current%m)          
        i = i+1
#        print("1:  ",ar[i])
#        print("0:  ",ar[i-1])
        if (ar[i] == 1 and ar[i-1] == 0):    
            done = True
#    print("End Length",len(ar))
    x = len(ar)-2
#    print(ar)
#    print(current)    

       
    remainder = n % x
    if remainder == 0:
        return 0
    previous = 0
    current  = 1
    if remainder == 0:
        return 0
    for _ in range(remainder-1):
        previous, current = current, previous + current
#    print("Current:  ", current)
    return current % m

if __name__ == '__main__':
    input = sys.stdin.read();
    n, m = map(int, input.split())
    print(get_fibonacci_huge_smart(n, m))
