class GraphT():
	#
	def __init__(self, numOfVertices):
		self.numOfVertices = numOfVertices
		self.adjacencyList = [[] for i in range(numOfVertices + 1)]
		self.numOfEdges = 0

	def vertices(self):
		return self.numOfVertices
	def edges(self):
		return self.numOfEdges
	def addEdge(self, nodeA, nodeB):
		self.adjacencyList[nodeA].append(nodeB)
		self.adjacencyList[nodeB].append(nodeA)
		self.numOfEdges = self.numOfEdges + 1
	def adjList(self, node):
		return self.adjacencyList[node]


		

def main():
	print("Hello")
	g = GraphT(4)
	x = g.vertices()
	print(x)
	g.addEdge(3,4)
	g.addEdge(3,2)
	print(g.edges())
	print(g.adjList(3))
main()
