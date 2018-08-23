# Uses python3
import sys
import itertools

def partition3(A):
##Then, you may want to build all possible arrays of N=len(A) values taken from a list of possible values.
    for c in itertools.product(range(3), repeat=len(A)):
#        print(c)
        sums = [None] * 3
        for i in range(3):
            sums[i] = sum(A[k] for k in range(len(A)) if c[k] == i)
#            print(sums)
#        print("STO")
        if sums[0] == sums[1] and sums[1] == sums[2]:
#            print("AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA")
            return 1

    return 0




if __name__ == '__main__':
    input = sys.stdin.read()
    n, *A = list(map(int, input.split()))
    print(partition3(A))

