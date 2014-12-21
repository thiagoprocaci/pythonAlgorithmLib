# -*- coding: utf-8 -*-

from Graph import *
import codecs


def loadMatrix():
    fileName = 'inputs/BoggleSolver.txt'
    fileMatrix = codecs.open(fileName, 'r', 'utf-8')
    text = fileMatrix.read()        
    matrix = []
    for line in text.split('\n'):            
        row = []
        for mychar in line.split(';'):
            if mychar:
                row.append(mychar.strip())
        matrix.append(row)
    return matrix

def findNeighbourList(matrix, i, j):
    neighbourList = []
    addToNeighbourList(neighbourList, i + 1, j, matrix)
    addToNeighbourList(neighbourList, i - 1, j, matrix)
    addToNeighbourList(neighbourList, i , j + 1, matrix)
    addToNeighbourList(neighbourList, i , j - 1, matrix)
    addToNeighbourList(neighbourList, i + 1, j + 1, matrix)
    addToNeighbourList(neighbourList, i + 1, j - 1, matrix)
    addToNeighbourList(neighbourList, i - 1, j + 1, matrix)
    addToNeighbourList(neighbourList, i - 1, j - 1, matrix)
    return neighbourList


def addToNeighbourList(neighbourList, i, j, matrix):
    if i >= 0 and j >= 0 and j < len(matrix[0]) and i < len(matrix[0]):        
        t = (i,j)        
        neighbourList.append(t)  

def transformMatrixToGraph(matrix):
    i = j = 0   
    nodeDict = {}     
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            nodeId = str(i) + "-" + str(j)
            node = Node(nodeId, matrix[i][j])
            nodeDict[nodeId] = node

    edgeDict = {}
    for nodeId in nodeDict:
        nodeIdArray = nodeId.split('-')
        i = int(nodeIdArray[0])
        j = int(nodeIdArray[1])
        neighbourList = findNeighbourList(matrix, i ,j)
        for neighbour in neighbourList:
            t = list(neighbour)
            source = nodeDict[nodeId]
            dest = nodeDict[str(t[0]) + "-" + str(t[1])]
            edge = Edge(source, dest)
            edgeDict[edge.id] = edge

    return Graph(nodeDict, edgeDict)



def main():
    #not optimized solution
    matrix = loadMatrix()
    print matrix
    print '-----------'
    graph = transformMatrixToGraph(matrix)
    originList = []
    destList = []
    for nodeKey in graph.nodeDict:
        node = graph.nodeDict[nodeKey]
        #print node.id, node.label
        if node.label == 'h':
            originList.append(node)
        elif node.label == 't':
            destList.append(node)



    dictPossibleSolution = {}
    count = 0
    for originNode in originList:
        print 'Origin:', originNode.id, originNode.label
        for goalNode in destList:
            print 'Dest:', goalNode.id, goalNode.label
            pathList = BreadthFirstSearch.findAllPath(graph, originNode, goalNode, 3)
            dictPossibleSolution[count] = pathList
            count = count + 1

    print 'Printing solution: finding word "heat"'
    for key in dictPossibleSolution:
        pathList = dictPossibleSolution[key]        
        for path in pathList:            
            printSep = False 
            length = len(path)
            label1 = graph.nodeDict[path[0]].label
            label2 = graph.nodeDict[path[1]].label
            label3 = graph.nodeDict[path[2]].label
            label4 = graph.nodeDict[path[3]].label
            if (length == 4) and (label1 == 'h') and (label2 == 'e') and (label3 == 'a') and label4 == 't':
                printSep = True
                for nodeId in path:
                    node = graph.nodeDict[nodeId]
                    pathString = nodeId + ':' + node.label
                    print pathString
                    
            if printSep:       
                print '---------------------'



            

    
    

if __name__ == '__main__':
    main()