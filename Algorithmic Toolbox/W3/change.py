# Uses python3
import sys

def get_change(m):


    ten = 0
    five = 0
    one = 0

    if m % 10 == 0:
        return int(m/10)
    else:
        if m % 10 % 5 == 0:
            return int(m/10) + int(m%10/5)
        else:
            return (m - int(m/10)*10 - int(m%10/5)*5) + int(m/10) + int(m%10/5)
   

if __name__ == '__main__':
    m = int(sys.stdin.read())
    print(get_change(m))
