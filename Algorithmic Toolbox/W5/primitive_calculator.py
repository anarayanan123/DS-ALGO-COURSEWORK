# Uses python3
import sys

def optimal_sequence(n):
    sequence = []
    while n >= 1:
        sequence.append(n)
        if n % 3 == 0:
            n = n // 3
        elif n % 2 == 0:
            n = n // 2
        else:
            n = n - 1
    return reversed(sequence)



def optimal_sequence1(n):
    sequence = []
    dp_table = []
    dp_table.append(0)
    dp_table.append(0)
    for m in range(2,n+1):
   
        dp_table.append(m)
#        print(dp_table[m])
        if m%3 ==0:
            three = dp_table[m//3]+1
        else:
            three = dp_table[m]
        if m%2 == 0:
            two = dp_table[m//2]+1
        else:
            two = dp_table[m]  
        one =  dp_table[m-1]+1
        dp_table[m] = (min(one, three, two))
#    print(dp_table)
    value = dp_table[n]
    return value


input = sys.stdin.read()
n = int(input)
#sequence = list(optimal_sequence(n))
#print(len(sequence) - 1)
#for x in sequence:
#    print(x, end=' ')
print(optimal_sequence1(n))
