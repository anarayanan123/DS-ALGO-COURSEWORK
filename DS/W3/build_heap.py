# python3

def SiftDown(h, i, t):  
  n = len(h)-1
  maxIndex = i
  l = 2*i+1
  if l <= n and h[l] < h[maxIndex]:
    maxIndex = l
  r = 2*i+2
  if r <= n and h[r] < h[maxIndex]:
    maxIndex = r
  if i != maxIndex:
    h[i], h[maxIndex] = h[maxIndex], h[i]
    t.append((i, maxIndex))
    SiftDown(h, maxIndex, t)

class HeapBuilder:
  def __init__(self):
    self._swaps = []
    self._data = []

  def WriteResponse(self):
    print(len(self._swaps))
    for swap in self._swaps:
      print(swap[0], swap[1])

  def GenerateSwaps(self):
    for i in range(len(self._data)):
      for j in range(i + 1, len(self._data)):
        if self._data[i] > self._data[j]:
          self._swaps.append((i, j))
          self._data[i], self._data[j] = self._data[j], self._data[i]

  def ReadData(self):
    n = int(input())
    self._data = [int(s) for s in input().split()]
    assert n == len(self._data)


  def buildheap(self):
    n = len(self._data)
#    print(n)
    for i in range ((n-1)//2, -1, -1):
      SiftDown(self._data, i, self._swaps)       

        


  def Solve(self):
    self.ReadData()
    self.buildheap()
#    self.GenerateSwaps()
    self.WriteResponse()


if __name__ == '__main__':
    heap_builder = HeapBuilder()
    heap_builder.Solve()
