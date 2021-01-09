from EdgeT import *
from NodeT import *
class GraphT():
	def __init__(self, listOfNodes):
		self.numOfVertices = len(listOfNodes)
		self.adjacencyList = [[] for i in range(self.numOfVertices)]
		self.numOfEdges = 0
		self.listOfNodes = listOfNodes
	def vertices(self):
		return self.numOfVertices
	def edges(self):
		return self.numOfEdges
	def addEdge(self, edge):
		first = edge.firstNode()
		second = edge.secondNode(first)
		#print("first", first)
		#print("second", second)
		self.adjacencyList[first.getnumber() - 1].append(edge)
		self.adjacencyList[second.getnumber() - 1].append(edge)
		self.numOfEdges = self.numOfEdges + 1
	def adjList(self, node):
		return self.adjacencyList[node.getnumber() - 1]
	def printAll(self):
		edges = []
		for i in self.listOfNodes:
			for j in self.adjacencyList[i.getnumber() - 1]:
				#print(type(j))
				#print("this is j",j)
				if(j.secondNode(i).getnumber() > i.getnumber()):
					edges.append(j)
		return edges

	def toString(self):
		for i in self.printAll():
			x = i.firstNode()
			y = i.secondNode(x)
			print(x.getnumber(), "->", y.getnumber(), " Weight is ", i.getWeight())
			#print("The weight is ", i.getWeight())
		return 0
		

	def buildGraph(self):
		#list of edges
		for i in range(self.numOfVertices):
			for j in range(self.numOfVertices):
				if j == i:
					continue
				for k in range(len(self.listOfNodes[j].getneighbours())):
					#print("Value of 'i' is ", i)
					#print("Value of 'j' is ", j)
					#print("Value of 'k' is ", k)
					#print("Value of 'self.listOfNodes[i].getnumber()' is ", self.listOfNodes[i].getnumber())
					#print("Value of 'self.listOfNodes[j].getneighbours()[k]' is ", self.listOfNodes[j].getneighbours()[k])
					#print()
					if(self.listOfNodes[i].getnumber() == self.listOfNodes[j].getneighbours()[k]):
						edge = EdgeT(self.listOfNodes[i], self.listOfNodes[j], self.listOfNodes[i].getweight() + self.listOfNodes[j].getweight())
						self.addEdge(edge)
