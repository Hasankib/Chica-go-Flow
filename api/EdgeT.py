class EdgeT():
	def __init__(self, NodeA, NodeB, weight):
		self.NodeA = NodeA
		self.NodeB = NodeB
		self.weight = weight
	def getWeight(self):
		return self.weight
	def firstNode(self):
		return self.NodeA
	def secondNode(self,vertex):
		if vertex == self.NodeA:
			return self.NodeB
		elif vertex == self.NodeB:
			return self.NodeA
		#exception handling
		else:
			return 0