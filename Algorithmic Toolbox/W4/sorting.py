# Uses python3
import sys
import random

def partition3(a, l, r):

    x = a[l]
#    print("x", x)
    i = l 
    lt = l
    gt = r;
    while i <= gt:

#        print("i", i)
#        print("lt", lt)
#        print("gt", gt)
#        print(a)
        if a[i] < x:
            a[i], a[lt] = a[lt], a[i]
            i += 1
            lt += 1            
        elif a[i] > x:
            a[i], a[gt] = a[gt], a[i]
            gt -= 1            
        elif a[i] == x:
            i += 1

    return lt, gt

def partition4(a, l, r):
    x = a[l]
#    print("x", x)    
    j = l;
    for i in range(l + 1, r + 1):
        if a[i] <= x:
            j += 1
            a[i], a[j] = a[j], a[i]
#    print("j", j)
    a[l], a[j] = a[j], a[l]
    
    j1 = j
    for i in range(j-1, -1, -1):
        if a[i] == x:
            j1 -= 1
            a[i], a[j1] = a[j1], a[i]
#    print("j1", j1)
    return j1, j

def partition2(a, l, r):
    x = a[l]
    j = l;
    for i in range(l + 1, r + 1):
        if a[i] <= x:
            j += 1
            a[i], a[j] = a[j], a[i]
    a[l], a[j] = a[j], a[l]
    return j

def randomized_quick_sort(a, l, r):
    if l >= r:
        return
    k = random.randint(l, r)
    a[l], a[k] = a[k], a[l]
    #use partition3
    m = partition2(a, l, r)
    randomized_quick_sort(a, l, m - 1);
    randomized_quick_sort(a, m + 1, r);

def randomized_quick_sort_three(a, l, r):
    if l >= r:
#        print("stop")
        return
    k = random.randint(l, r)
#    print("k", k)
#    print("a[k]", a[k])
#    print("l", l)
#    print("a[l]", a[l])
#    print("r", r)
#    print("a[r]", a[r])
    a[l], a[k] = a[k], a[l]
    
    m1, m2 = partition3(a, l, r) 
#    print("m1, m2", m1,"", m2)
    randomized_quick_sort_three(a, l, m1-1);
    randomized_quick_sort_three(a, m2 + 1, r);


if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
#    for x in range (0,1000):
#        randomized_quick_sort_three(a, 0, n - 1)
#        for x in a:
#            print(x, end=' ')
#        print("")
    randomized_quick_sort_three(a, 0, n - 1)
    for x in a:
        print(x, end=' ')

