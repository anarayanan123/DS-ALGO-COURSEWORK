# python3

import sys

class Bracket:
    def __init__(self, bracket_type, position):
        self.bracket_type = bracket_type
        self.position = position

    def Match(self, c):
        if self.bracket_type == '[' and c == ']':
            return True
        if self.bracket_type == '{' and c == '}':
            return True
        if self.bracket_type == '(' and c == ')':
            return True
        return False

class Stack:
    def __init__(self):
        self.key = []
        self.num = 0 
    def Push(self, c):
        self.key.append(c)
        self.num = self.num + 1    
    def Top(self):
        return self.key[self.num-1]
    def Pop(self):
        a = (self.key[self.num-1])
        del self.key[self.num-1]
        self.num = self.num -1
        return a
    def Empty(self):
        if len(self.key) > 0:
            return False
        else:
            return True
        
def check(text):
    d = Stack()
    a = Stack()
    for i, next in enumerate(text):   
        if next == '(' or next == '[' or next == '{':
            a.Push(next)
            d.Push(i+1)
        if next == ')' or next == ']' or next == '}':
            if a.Empty():
                return i+1 
            else:
                top = a.Pop()
                b = Bracket(top, i+1)
                if b.Match(next) != True:
                    return i+1
                d.Pop()
    if a.Empty(): 
        return -1
    else:
        return d.Pop()


if __name__ == "__main__":
    text = sys.stdin.read()
    if check(text) == -1:
        print ("Success")
    else:
        print(check(text))
        


