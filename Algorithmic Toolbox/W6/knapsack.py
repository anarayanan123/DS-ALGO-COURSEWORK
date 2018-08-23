# Uses python3
import sys

def optimal_weight(W, w):
    # write your code here
    result = 0
    for x in w:
        if result + x <= W:
            result = result + x
    return result

def optimal_weight(W, w):

    n = len(w)+1
    W = W+1
    items = w


    d = [[0 for x in range(n)] for y in range(W)]


##    count = 0 
##    #first word
##    for j in range(n):
##        d[j][0] = count
##    count = 0
##    #second word
##    for i in range(W):
##        d[0][i] = count


    for i in range(1, n):
        for weight in range(1, W):
            d[weight][i] = d[weight][i-1]
            if items[i-1] <= weight:
                val = d[weight-items[i-1]][i-1] + items[i-1]
                if d[weight][i] < val:
                    d[weight][i] = val


    return d[W-1][n-1]

if __name__ == '__main__':
    input = sys.stdin.read()
    W, n, *w = list(map(int, input.split()))
    print(optimal_weight(W, w))
##    print(optimal_weight1(W, w))
