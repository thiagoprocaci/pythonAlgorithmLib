
import Queue

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

    @staticmethod
    def findAllPaths(graph, originNode, goalNode):
        graph.clearNodeStatus()        
        parentMap = {}        
        pathList = []
        q = Queue.Queue()
        q.put(originNode)
        while not q.empty():
            n = q.get()
            if n.status != 'discovered':                
                n.status = 'discovered'                  
                for nodeKey in graph.getAdjacentNodes(n):
                    child = graph.nodeDict[nodeKey]                                                            
                    q.put(child)                    
                    parentMap[child.id] = n.id                    
                    if child.id == goalNode.id:    
                        q.get()              
                        n.status = None
                        path = []
                        curr = goalNode.id            
                        while (True):                
                            path.append(curr)
                            curr = parentMap.get(curr)
                            if curr == originNode.id:
                                path.append(curr)
                                break
                        path.reverse()
                        pathList.append(path)
                       
        return pathList


