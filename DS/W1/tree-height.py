# python3

import sys, threading
sys.setrecursionlimit(10**7) # max depth of recursion
threading.stack_size(2**27)  # new thread will get stack of such size

class TreeHeight:
        def read(self):
                self.n = int(sys.stdin.readline())
                print(self.n)
                self.parent = list(map(int, sys.stdin.readline().split()))
                print(self.parent)

        def compute_height(self):
                # Replace this code with a faster implementation
                maxHeight = 0
                for vertex in range(self.n):
                        height = 0
                        print("VERT", vertex)
                        i = vertex
                        print("i", i)
                        while i != -1:
                                height += 1
                                print("height", height)
                                i = self.parent[i]
                                print("ii", i)
                        maxHeight = max(maxHeight, height);
                return maxHeight;

class Nodes:
    def __init__(self, key, parent):
        self.key = key
        self.children = []
        self.parent = parent 
    def add_child(self, c):
        self.children.append(c)

    def recurseroot(self):
        if not self.children:
                print(self.key)
                return 0
        else:

                print(self.key)
                print("_____")
                for i in self.children:
                        nodes[i].recurseroot()

    def height(self, nodes):
        self.nodes = nodes
        if not self.children and self.parent == -1:
                return 1
        elif not self.children:
                return 1
        else:
                a = []
                for i in self.children:
                        a.append(nodes[i].height(nodes))
                return 1 + max(a)



def main():
        n = int(sys.stdin.readline())
        arr = list(map(int, sys.stdin.readline().split()))
        nodes = []

        for i in range (0,n):
                nodes.append(Nodes(i,arr[i]))
        for i in range(0,n):
                if (nodes[i].parent) == -1:
                        root = (nodes[i].key)
                else:
                        nodes[nodes[i].parent].add_child(nodes[i].key)

        print(nodes[root].height(nodes))
threading.Thread(target=main).start()

