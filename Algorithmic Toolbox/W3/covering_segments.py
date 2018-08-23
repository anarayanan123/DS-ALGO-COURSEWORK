# Uses python3
import sys
from collections import namedtuple

Segment = namedtuple('Segment', 'start end')

#def optimal_points(segments):


#    points = []
#    while len(segments) > 0:
#        segments.sort(key=lambda x: x[1])
#        p = segments[0].end
#        for s in segments:
#            if s.start <= p <= s.start:
#                segments.remove(s)
#                
#        points.append(p)          
#
#    return points


def optimal_points(segments):


    points = []
    while len(segments) > 0:
#    for i in range (0,4):
        segments.sort(key=lambda x: x[1])
#        print("Segments",segments)
        p = segments[0].end
#        print(p)
#        print(len(segments))
        points.append(p)
#        print("::::")
#        print("Segments",segments)
        indy  = []
        for s in segments:
#            print("indy",indy)
#            print(len(indy))
#            print("S", s)
#            print("Start", s.start)
#            print("End", s.end)
#            print("P", p)                
            if s.start <= p and p <= s.end:
                indy.append(s)
#        print(indy)
#        print(segments)
        for x in indy:
          segments.remove(x)

    return points


if __name__ == '__main__':
    input = sys.stdin.read()
    n, *data = map(int, input.split())
    segments = list(map(lambda x: Segment(x[0], x[1]), zip(data[::2], data[1::2])))
    points = optimal_points(segments)
    print(len(points))
    for p in points:
        print(p, end=' ')
