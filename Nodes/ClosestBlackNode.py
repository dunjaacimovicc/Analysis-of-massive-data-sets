import sys
import numpy as np 
from collections import defaultdict
# from sortedcontainers import SortedSet 
  
# sorted_set = SortedSet([1, 1, 2, 3, 4]) 
  
# # initializing a sorted set using default constructor 
# sorted_set = SortedSet() 
  
# # inserting values one by one 
# for i in range(5, 0, -1): 
#     sorted_set.add(i) 

def findNearestBlackNode(visited, openedNodes, dist, nodeColors, adjacencyMatrix, deadEnds):
    
    if (dist > 10 or len(openedNodes) == 0):
        return (-1, -1)

    # next = SortedSet()
    next = set()
    visited.union(openedNodes)
    for node in openedNodes:
        if(nodeColors[node] == 1):
            return (node, dist)
        next = next.union([node for node in adjacencyMatrix[node] if (node not in visited and node not in deadEnds)])
    return findNearestBlackNode(visited, sorted(next), dist+1, nodeColors, adjacencyMatrix, deadEnds)

def main():
    # input = open("RB.in", "r")
    input = sys.stdin

    (n, e) = map(int, input.readline().split())
    # print(n, e)
    nodeColors = []; # 0 is white, 1 is black
    adjacencyMatrix = defaultdict(lambda: [])
    deadEnds = []

    for i in range(n):
        t = int(input.readline())
        nodeColors.append(t)
    
    for i in range(e):
        (s, d) = map(int, input.readline().split())
        adjacencyMatrix[s].append(d)
        adjacencyMatrix[d].append(s)

    for i in range(n):
        (node, dist) = findNearestBlackNode(set(), {i}, 0, nodeColors, adjacencyMatrix, deadEnds)
        if node == -1:
            deadEnds.append(node)
        print(node, dist)


if __name__ == "__main__":
    main()
