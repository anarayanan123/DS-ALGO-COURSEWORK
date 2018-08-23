#!/usr/bin/python3

import sys, threading

sys.setrecursionlimit(10**7) # max depth of recursion
threading.stack_size(2**27)  # new thread will get stack of such size

result = []
left = []
right = []

def IsBinarySearchTree1(tree, i, nodes, x):
  print("t",i)
  if nodes == 0 or nodes == 1:
    return True
  if i == -1:
    print('i = -1')
    return 0
  if tree[i][1] == -1 and tree[i][2] == -1:
    result.append(tree[i][0])
    left.append(tree[i][1])
    right.append(tree[i][2])
    print(result)
    if len (result) >= 2 and result[-1] < result[-2]:
      return False
    if len (result) >= 2 and result[-1] == result[-2]:
      print(111)
      #print((left[-1]))
      #print((left[-1]))
      if (tree[(left[-1])][0] < result[-1] or (left[-1]) == -1) and (result[-1] >= tree[(right[-1])][0] or (right[-1]) == -1):
        print('we are true')
        return 0
      else:
        return False
    return 0

  if IsBinarySearchTree1(tree, tree[i][1], nodes, x) is False:
    return False
  result.append(tree[i][0])
  left.append(tree[i][1])
  right.append(tree[i][2])
  print(result)
  if len (result) >= 2 and result[-1] < result[-2]:
    return False
  if len (result) >= 2 and result[-1] == result[-2]:
      print(112)
      if (tree[(left[-1])][0] < result[-1] or (left[-1]) == -1) and (result[-1] >= tree[(right[-1])][0] or (right[-1]) == -1):
        print('we are true')
        return 0
      else:
        return False
      
  if IsBinarySearchTree1(tree, tree[i][2], nodes, x) is False:
    return False
    
  return True


def main():
  nodes = int(sys.stdin.readline().strip())
  tree = []
  chidren = []
  for i in range(nodes):
    tree.append(list(map(int, sys.stdin.readline().strip().split())))
  x = IsBinarySearchTree1(tree, 0, nodes, 0)
  #print("c",x)
  if x == True:
    print("CORRECT")

  else:
    print("INCORRECT")
threading.Thread(target=main).start()
