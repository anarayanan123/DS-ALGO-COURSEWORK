# python3

import sys, threading
sys.setrecursionlimit(10**6) # max depth of recursion
threading.stack_size(2**27)  # new thread will get stack of such size

class TreeOrders:
  def read(self):
    self.n = int(sys.stdin.readline())
    self.key = [0 for i in range(self.n)]
    self.left = [0 for i in range(self.n)]
    self.right = [0 for i in range(self.n)]
    self.result1 = []
    self.result2 = []
    self.result3 = []
    for i in range(self.n):
      [a, b, c] = map(int, sys.stdin.readline().split())
      self.key[i] = a
      self.left[i] = b
      self.right[i] = c
    #print(self.key)

  def inOrder(self, i):
    # Finish the implementation
    # You may need to add a new recursive method to do that
    #print("Result1", self.result1)
    #print("INDEX", i)
    #print("KEY", self.key[i])
    if i == -1:
      return 0 
    if self.left[i] == -1 and self.right[i] == -1:
      self.result1.append(self.key[i]) 
      return 0
    self.inOrder(self.left[i])
    self.result1.append(self.key[i])
    self.inOrder(self.right[i])
    return self.result1

  def preOrder(self, i):
    #print("Result2", self.result2)
    #print("INDEX", i)
    #print("KEY", self.key[i])
    if i == -1:
      return 0     
    if self.left[i] == -1 and self.right[i] == -1:
      self.result2.append(self.key[i]) 
      return 0
    self.result2.append(self.key[i])
    self.preOrder(self.left[i])
    self.preOrder(self.right[i])  
    return self.result2
                


  def postOrder(self, i):
    # Finish the implementation
    # You may need to add a new recursive method to do that
    #print("Result2", self.result2)
    #print("INDEX", i)
    #print("KEY", self.key[i])
    if i == -1:
      return 0     
    if self.left[i] == -1 and self.right[i] == -1:
      self.result3.append(self.key[i]) 
      return 0
    self.postOrder(self.left[i])
    self.postOrder(self.right[i])  
    self.result3.append(self.key[i])


                
    return self.result3

def main():
	tree = TreeOrders()
	tree.read()
	print(" ".join(str(x) for x in tree.inOrder(0)))
	print(" ".join(str(x) for x in tree.preOrder(0)))
	print(" ".join(str(x) for x in tree.postOrder(0)))

threading.Thread(target=main).start()
