# Uses python3
import sys

def get_change(m):

    mincoins = []
    mincoins.append(0)
    denom = [1,3,4]
    for m in range (1,m+1):
        mincoins.append(m)
#        print("COINS:", mincoins)
#        print("M:", m)
        for i in denom:
#            print("I:", i)
            if m >= i:
                numcoins = mincoins[m-i]+1
#                print("numcoins:", numcoins)
                if numcoins < mincoins[m]:
                    mincoins[m] = numcoins
#        print(mincoins)
    return mincoins[m]


if __name__ == '__main__':
    m = int(sys.stdin.read())
    print(get_change(m))
