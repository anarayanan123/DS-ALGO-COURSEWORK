# Uses python3
import sys

def get_optimal_value(capacity, weights, values):
    value = 0
    for i in range(0,n):
#        print("Round:  ",i)      
        if capacity == 0:
            return value
        if len(weights) == 0:
            return value
        best_item = 0
        item = 0 
        for i in range(0,len(weights)):
            itemper = values[i]/weights[i]
            if itemper > best_item:
                best_item = itemper
                item = i
        i = item 
#        print(i)
#        print(values)
#        print(weights)
        if weights[i] < capacity:
            value = value + values[i]            
            capacity = capacity - weights[i]
            del(weights[i])
            del(values[i])
#            print(value)
#            print("1")
        elif weights[i] == capacity:
            value = value + values[i]            
            capacity = capacity - weights[i]
            del(weights[i])
            del(values[i])
#            print(value)
#            print("2")
        else:
            x = capacity / weights[i]               
            value = value + values[i]*x            
            capacity = capacity - weights[i]*x
            weights[i] = weights[i]-weights[i]*x
            del(weights[i])
            del(values[i])            
    return value


if __name__ == "__main__":
    data = list(map(int, sys.stdin.read().split()))
    n, capacity = data[0:2]
    values = data[2:(2 * n + 2):2]
    weights = data[3:(2 * n + 2):2]
#    print(weights)
#    print(values)
    opt_value = get_optimal_value(capacity, weights, values)
    print("{:.4f}".format(opt_value))
#    print(weights)
#    print(values)
