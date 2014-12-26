# -*- coding: utf-8 -*-


class GraphSupport:
    #useful class for basic graph constructions

    @staticmethod
    def buildGraph(text):
        #metodo util para testes
        # pattern AB2;BC3
        textArray = text.split(';')
        nodeDict = {}
        edgeDict = {}
        for t in textArray:
            source = Node(t[0])
            dest = Node(t[1])
            edge = Edge(source, dest, int(t[2]))
            nodeDict[source.id] = source
            nodeDict[dest.id] = dest
            edgeDict[edge.id] = edge
        return Graph(nodeDict, edgeDict)

class Graph:
    nodeDict, edgeDict = None, None

    def __init__(self, nodeDict, edgeDict):
        self.edgeDict = edgeDict
        self.nodeDict = nodeDict

    def __str__(self):
        return "Graph: #nodes: " + str(len(self.nodeDict)) + " #edges: " + str(len(self.edgeDict))

    def getAdjacentNodes(self, node):        
        adjacentNodes = {}
        for key in self.edgeDict:
            edge = self.edgeDict[key]
            if edge.source.id == node.id:
                adjacentNodes[edge.dest.id] = edge.dest        
        return adjacentNodes

    def clearNodeStatus(self):
        for key in self.nodeDict:
            self.nodeDict[key].status = None    

    def getEdge(self, source, dest):
        idEdge = Edge.genId(source, dest)
        return self.edgeDict.get(idEdge)

    def getPathCost(self, path):
        if len(path) > 0:
            i = 0
            sumCost = 0
            while ((i + 1) < len(path)):
                idEdge = Edge.genId(Node(path[i]), Node(path[i + 1]))
                edge = self.edgeDict.get(idEdge)
                sumCost = sumCost + edge.weight
                i = i + 1
            return sumCost
        return None




class Node:
    label, id, status = None, None, None

    def __init__(self, id, label = None, status = None):
        self.label = label
        self.id = id
        self.status = status

    def __str__(self):
        return "Node id: " + str(self.id)

class Edge:
    source, dest, id, weight = None, None, None, None

    def __init__(self, source, dest, weight = 0):
        self.source = source
        self.dest = dest
        self.id = Edge.genId(source, dest)
        self.weight = weight

    @staticmethod
    def genId(sourceNode, destNode):
       return str(sourceNode.id) + "_" + str(destNode.id)

    def __str__(self):
        return "Edge id: " + str(self.id)


class DepthFirstSearch:

    def __init__(self):
        pass

    # busca em profundidade
    # retorna lista com o caminho
    # o grafo nao pode ter ciclos
    @staticmethod
    def findPath(graph, originNode, goalNode):
        graph.clearNodeStatus()
        parentMap = {}        
        found = False
        s = [] #stack 
        s.append(originNode)
        while len(s) > 0:
            n = s.pop()
            if n.status != 'discovered':                
                n.status = 'discovered'                
                for nodeKey in graph.getAdjacentNodes(n):
                    child = graph.nodeDict[nodeKey]                                                            
                    s.append(child)                    
                    parentMap[child.id] = n.id                    
                    if child.id == goalNode.id:
                        found = True                        
                        break             
            if found:                                        
                break            
            
        if found:            
            path = []
            curr = goalNode.id            
            while (True):                
                path.append(curr)
                curr = parentMap.get(curr)
                if curr == originNode.id:
                    path.append(curr)
                    break
            path.reverse()
            return path
        return None    


class BreadthFirstSearch:

    def __init__(self):
        pass

    @staticmethod
    def findAllPathWithNoGoal(graph, originNode, searchMaxLevel = 1):
        if (originNode is None) or (originNode.id is None):
            return []
        visitedList = []
        visitedList.append(originNode.id)
        nodeReturnList = []        
        BreadthFirstSearch.__findAllPathWithNoGoal(graph, visitedList, nodeReturnList, searchMaxLevel, 0)        
        return nodeReturnList

    @staticmethod
    def __findAllPathWithNoGoal(graph, visitedList, nodeReturnList, searchMaxLevel, currentLevel):
        if (searchMaxLevel == currentLevel):
            l = []
            for idNode in visitedList:
                l.append(idNode)
            nodeReturnList.append(l) 
            return

        nodeDict = graph.getAdjacentNodes(graph.nodeDict[visitedList[-1]])

        for nodeKey in nodeDict:            
            visitedList.append(nodeKey)
            currentLevel = currentLevel + 1
            BreadthFirstSearch.__findAllPathWithNoGoal(graph, visitedList, nodeReturnList, searchMaxLevel, currentLevel)
            currentLevel = currentLevel - 1
            visitedList.pop()



    # returns all path between two nodes
    # accept cycles in graph,however, paths returned admits no cicle
    # origin node must be different from goal node
    @staticmethod
    def findAllPath(graph, originNode, goalNode, searchMaxLevel = None):
        if (goalNode is None) or (goalNode.id is None) or (originNode is None) or (originNode.id is None) or (goalNode.id == originNode.id):
            return []
        if searchMaxLevel <= 0:
            searchMaxLevel = None
        visitedList = []
        visitedList.append(originNode.id)
        nodeReturnList = []        
        BreadthFirstSearch.__findAllPath(graph, goalNode, visitedList, nodeReturnList, searchMaxLevel, 0)  
        
        return nodeReturnList
        

    @staticmethod
    def __findAllPath(graph, goalNode, visitedList, nodeReturnList, searchMaxLevel, currentLevel):        
        if (searchMaxLevel is not None)  and (searchMaxLevel <= currentLevel):
            return         
        nodeDict = graph.getAdjacentNodes(graph.nodeDict[visitedList[-1]])
        for nodeKey in nodeDict:
            if nodeKey in visitedList:
                continue
            if nodeKey == goalNode.id:
                visitedList.append(nodeKey)
                l = []
                for idNode in visitedList:
                    l.append(idNode)
                nodeReturnList.append(l)                
                visitedList.pop()
                break

        for nodeKey in nodeDict:
            if (nodeKey in visitedList) or (nodeKey == goalNode.id):
                continue
            visitedList.append(nodeKey)
            currentLevel = currentLevel + 1
            BreadthFirstSearch.__findAllPath(graph, goalNode, visitedList, nodeReturnList, searchMaxLevel, currentLevel)
            currentLevel = currentLevel - 1
            visitedList.pop()
