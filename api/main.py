from NodeT import *
#from GraphT import *
#from BFS import *

class main:
    def __init__(self, nodeList):
        self.nodeList = nodeList
        #self.graph = graph
        #self.shortestPath = shortestPath
    
    def setNodeList (self, filename,filename2,filename3):
        file1 = open(filename,"r") 
        dictionary = eval(file1.read())
        file1.close()

        file2 = open(filename2,"r")
        names = (file2.read()).split(",")
        file2.close()

        file3 = open(filename3,"r")
        tmplist = (file3.read().split(" "))
        file3.close()
        neighbours = []
        for i in tmplist:
            tmplist2 = i.split(",")
            for i in tmplist2:
                tmplist2[tmplist2.index(i)] = int(i)
            neighbours.append(tmplist2)

        for i in range (1,78):
            tempnode = NodeT(i,names[i-1],neighbours[i-1],dictionary[i])
            self.nodeList.append(tempnode)
        

main = main([])
main.setNodeList("dataset1.txt","dataset2.txt","dataset3.txt")
print((main.nodeList)[0].number)
print((main.nodeList)[0].name)
print((main.nodeList)[0].neighbours)
print((main.nodeList)[0].weight)

print((main.nodeList)[76].number)
print((main.nodeList)[76].name)
print((main.nodeList)[76].neighbours)
print((main.nodeList)[76].weight)

#queue = {0:100,1:50,2:20}
#minKey = min(queue.keys(), key=(lambda k: queue[k]))
#queue.pop(minKey)
#print(queue)
#print(minKey)