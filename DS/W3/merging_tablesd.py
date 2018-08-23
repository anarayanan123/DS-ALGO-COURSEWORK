# python3

import sys, threading
#sys.setrecursionlimit(10**5) # max depth of recursion
#threading.stack_size(2**27)  # new thread will get stack of such size

n, m = map(int, sys.stdin.readline().split())
lines = []
lines.append(0)
lines.extend(list(map(int, sys.stdin.readline().split())))
rank = [1] * (n+1)
parent = []
parent.append(0)
parent.extend(list(range(1, n+1)))
current_max = max(lines)

def getParent(table):
    if table != parent[table]:
        parent[table] = getParent(parent[table])
    return parent[table]

#def getParent(table):
#    while table != parent[table]:
#        table = parent[table]       
#    return parent[table]

def union(destination, source, current_max):
    realDestination, realSource = getParent(destination), getParent(source)
    if realDestination == realSource:
        return max((lines[realDestination]), current_max)
#        return max(lines)
    if rank[realDestination] > rank[realSource]:
        parent[realSource] = realDestination  
        lines[realDestination] = lines[realDestination] + lines[realSource]
        lines[realSource] = 0
        return max(current_max,(lines[realDestination]))
 #       return max(lines)        
    else:
        parent[realDestination] = realSource
        lines[realSource] = lines[realDestination] + lines[realSource]
        lines[realDestination] = 0
        parent[destination] = realSource    
        if rank[realDestination] == rank[realSource]:
            rank[realSource] = rank[realSource]+1
        return max(current_max,(lines[realSource]))
        #return max(lines)

#def main():
for i in range(m):
    destination, source = map(int, sys.stdin.readline().split())
    x = union(destination, source, current_max)
    print(max(current_max,x))
    current_max = x
    
#threading.Thread(target=main).start()

    
