'''
    @author: Rezab Ud Dawla
'''

import heapq

nodeInitializer = {0: 'S', 1: 'A', 2: 'B', 3: 'C', 4: 'D'}
adjacencyList = {0: {1: 1, 2: 4}, 1: {2: 2, 3: 5, 4: 12}, 2: {3: 2}, 3: {4: 3}, 4: {}}
heuristics = {0: 7, 1: 6, 2: 2, 3: 1, 4: 0}
priorityQueue = []
goalNode = 4
pathTrack = []

class node:
    def __init__(self, nodeNo, prevNode, g_n, f_n):
        self.nodeNo = nodeNo
        self.prevNode = prevNode
        self.g_n = g_n
        self.f_n = f_n

    def __lt__(self, new):
        return self.f_n < new.f_n

startNode = node(list(nodeInitializer.keys())[0], None, 0, heuristics[0])
heapq.heappush(priorityQueue, startNode)

while priorityQueue:
    curQueue = heapq.heappop(priorityQueue)
    if curQueue.nodeNo == goalNode:
        print("Optimal Path Cost: ", end=' ')
        print(curQueue.f_n)
        pathTrack.append(curQueue.nodeNo)
        while curQueue.prevNode != None:
            pathTrack.append(curQueue.prevNode.nodeNo)
            curQueue = curQueue.prevNode
        print("Optimal Path: ", end=' ')
        for x in reversed(range(len(pathTrack))):
            if x == 0:
                print(nodeInitializer[pathTrack[x]])
            else:
                print(nodeInitializer[pathTrack[x]], '->', end=' ')
        break
    for i in range(len(adjacencyList[curQueue.nodeNo])):
        nNodeNumber = list(adjacencyList[curQueue.nodeNo].keys())[i]
        nGn = curQueue.g_n + list(adjacencyList[curQueue.nodeNo].values())[i]
        nFn = nGn + heuristics[nNodeNumber]
        newNode = node(nNodeNumber, curQueue, nGn, nFn)
        heapq.heappush(priorityQueue, newNode)