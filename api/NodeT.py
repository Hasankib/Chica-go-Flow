class NodeT():
    #
    def __init__(self, number,name,neighbours,weight):
        self.name = name
        self.number = number
        self.neighbours = neighbours
        self.weight = weight

    def setname(self, somename):
        self.name = somename
    def getname(self):
        return self.name

    def setnumber(self, somenumber):
        self.name = somenumber
    def getnumber(self):
        return self.number

    def setneighbours(self, someneighbour):
        self.neighbours.append(someneighbour)
    def getneighbours(self):
        return self.neighbours

    def setweight(self, someweight):
        self.weight = someweight
    def getweight(self):
        return self.weight
