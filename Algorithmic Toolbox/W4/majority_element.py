# Uses python3
import sys

def get_majority_element(a, left, right):
    
    if left == right:
#        print("STOP")
        return -1
    if left + 1 == right:
#        print("STOP")
        return a[left]
           
    mid = int((right-left)/2)+left
#    print("Left", left)
#    print("Mid", mid-1)
#    print("Right", right)
    y = get_majority_element(a, left, mid-1)

    z = get_majority_element(a, mid, right)
    
    if (y == -1 and z == -1):
#        print("111111111")
#        print(y," ", z)
#        print(left)
#        print(right)
        return -1
    elif y != -1 and z != -1:
#        print("2222")
#        print(y)
#        print(z)
        county = 0        
        for i in range (left,right):
            if a[i] == y:
                county = county + 1
            if county > (right-left)/2:
#                print("y county", y)
                return y
        countz = 0               
        for i in range (left,right):
            if a[i] == z:
                countz = countz + 1
            if countz > (right-left)/2:
#                print("z county", z)
                return z
        return -1    
    elif y != -1:
 #       print("4444444")
 #       print("y", y)
 #       print("z", z)
 #       print(left)
 #       print(right)
        county = 0
        for i in range (left,right):
            if a[i] == y:
                county = county + 1
            if county > (right-left)/2:
#                print("y county", y)
                return y  
        return -1       
    else:
    #    print("444444433333")
    #    print("y", y)
    #    print("z", z)
        countz = 0        
        for i in range (left,right):
            if a[i] == z:
                countz = countz + 1
            if countz > (right-left)/2:
  #              print("z county", z)
                return z  
        return -1        


def get_naive_majority_element(a, left, n):
    for i in range (0,len(a)):
        current = a[i]
        count = 0
        for j in range (0,len(a)):
            if a[j] == current:
                count = count + 1
            if count > n/2:
                return a[j]
        return -1 
    

if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    if get_majority_element(a, 0, n) != -1:
        print(1)
    else:
        print(0)

    
