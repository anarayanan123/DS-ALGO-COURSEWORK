# Uses python3
import numpy

def edit_distance(first, second):


    second_n = len(second)+1    
    first_m = len(first)+1
    
    d = [[0 for x in range(second_n)] for y in range(first_m)]

    count = 0 
    #first word
    for j in range(first_m):
        d[j][0] = count
        count = count +1
    count = 0
    #second word
    for i in range(second_n):
        d[0][i] = count
        count = count +1

    for j in range(1, second_n):
        for i in range (1, first_m):

            insertion = d[i][j-1]+1
            deletion = d[i-1][j]+1
            match = d[i-1][j-1]
            mismatch = d[i-1][j-1]+1
        
            if first[i-1] == second[j-1]:
                d[i][j] = min(insertion, deletion, match)
            else:
                d[i][j] = min(insertion, deletion, mismatch)
            
    return d[first_m-1][second_n-1] 

if __name__ == "__main__":
    print(edit_distance(input(), input()))
