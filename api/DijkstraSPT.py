from GraphT import *
from NodeT import *
import heapq
class DijkstraSPT():

    def __init__(self, graph,source,destination):
        self.graph = graph
        self.source = source
        self.destination = destination

        self.edgeTo = [0 for i in range (graph.vertices())]
        self.distTo = [float("inf") for i in range (graph.vertices())]
        self.distTo[source.getnumber()-1] = 0

        self.pq = []
        #heappush(pq,)
        self.queue = {}
        self.shortestPath = []

    def calculateDistances(self):
        distances = {vertex: float('infinity') for vertex in self.graph.listOfNodes}
        distances[self.source.getnumber() - 1] = 0

        #print(distances[0])
        #print(distances)




        pq = [(0,self.source.getnumber() - 1)]
        while len(pq) > 0:
            current_distance, current_vertex = heapq.heappop(pq)
            if current_distance > distances[current_vertex]:
                continue

            for neighbor


    # def delMin(self):
    #     minKey = min(self.queue.keys(), key=(lambda k: self.queue[k]))
    #     self.queue.pop(minKey)
    #     if(len(self.queue == 0)):
    #         return minKey
    #     else:
    #         minKey = min(self.queue.keys(), key=(lambda k: self.queue[k]))
    #         return minkey 

    # def relax(self, intOfVertexRelaxing):
    #     ##need to see graph class to implement this

    # def applyDijkstra(self):
    #     for i in range(len(self.distTo)):
    #         self.distTo[i] = float('inf')

    #     self.distTo[self.source-1] = 0
    #     self.queue[self.source] = 0
    #     while(len(self.queue) != 0):
    #         relax(delMin(self.queue))



    