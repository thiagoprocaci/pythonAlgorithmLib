# -*- coding: utf-8 -*-
import unittest
from Graph import *


#python -m unittest discover

class TestCaseApp(unittest.TestCase):

    def setUp(self):
        pass

    def testNodeGraph(self):
        idNode = 1
        label = 'label'
        status = 'status'

        node = Node(idNode, label, status)
        self.assertEqual(idNode, node.id)
        self.assertEqual(label, node.label)
        self.assertEqual(status, node.status)

        self.assertEqual("Node id: " + str(idNode), str(node))


    def testEdgeGraph(self):
        sourceId = 1
        destId = 2

        source = Node(sourceId)
        dest = Node(destId)

        edge = Edge(source, dest, 9)
        edgeId = (str(source.id) + "_" + str(dest.id))

        self.assertEqual(source.id, edge.source.id)
        self.assertEqual(dest.id, edge.dest.id)        
        self.assertEqual(edgeId, edge.id)
        self.assertEqual(9, edge.weight)
        self.assertEqual("Edge id: " + str(edge.id), str(edge))

    def testGraph(self):
        sourceId = 1
        destId = 2

        source = Node(sourceId)
        dest = Node(destId)

        edge = Edge(source, dest)

        nodeDict = {sourceId : source, destId : dest}
        edgeDict = {edge.id : edge}

        graph = Graph(nodeDict, edgeDict)
        toString = "Graph: #nodes: " + str(len(nodeDict)) + " #edges: " + str(len(edgeDict))

        self.assertEqual(2, len(graph.nodeDict))
        self.assertEqual(1, len(graph.edgeDict))
        self.assertEqual(toString, str(graph))

    def testGetAdjacentNodes(self):
        sourceId = 1
        destId = 2
        destId2 = 3

        source = Node(sourceId)
        dest = Node(destId)
        dest2 = Node(destId2)

        edge = Edge(source, dest)
        edge2 = Edge(source, dest2)

        nodeDict = {sourceId : source, destId : dest, destId2 : dest2}
        edgeDict = {edge.id : edge, edge2.id : edge2}

        graph = Graph(nodeDict, edgeDict)

        adjacentNodes =  graph.getAdjacentNodes(source)
        self.assertEqual(2, len(adjacentNodes))
        self.assertEqual(destId, adjacentNodes[destId].id)
        self.assertEqual(destId2, adjacentNodes[destId2].id)

    def testClearNodeStatus(self):
        node = Node(1, 'label', 'status')
        node2 = Node(2, 'label2', 'status2')

        nodeDict = {node.id : node, node2.id : node2}

        graph = Graph(nodeDict, None)
        for key in graph.nodeDict:
            node = graph.nodeDict[key]
            self.assertTrue(node.status is not None)

        graph.clearNodeStatus()
        for key in graph.nodeDict:
            node = graph.nodeDict[key]
            self.assertTrue(node.status is None)

    def testBuildGraphSupport(self):        
        text = 'AB2;AC3;BD5;DE1;BA3;AD1'
        graph = GraphSupport.buildGraph(text)
        self.assertEqual(5, len(graph.nodeDict))
        self.assertEqual(6, len(graph.edgeDict))

        self.assertEqual('A', graph.nodeDict['A'].id)
        self.assertEqual('B', graph.nodeDict['B'].id)
        self.assertEqual('C', graph.nodeDict['C'].id)
        self.assertEqual('D', graph.nodeDict['D'].id)
        self.assertEqual('E', graph.nodeDict['E'].id)


        self.assertEqual(2, graph.edgeDict[Edge.genId(graph.nodeDict['A'], graph.nodeDict['B'])].weight)
        self.assertEqual(3, graph.edgeDict[Edge.genId(graph.nodeDict['A'], graph.nodeDict['C'])].weight)
        self.assertEqual(5, graph.edgeDict[Edge.genId(graph.nodeDict['B'], graph.nodeDict['D'])].weight)
        self.assertEqual(1, graph.edgeDict[Edge.genId(graph.nodeDict['D'], graph.nodeDict['E'])].weight)
        self.assertEqual(3, graph.edgeDict[Edge.genId(graph.nodeDict['B'], graph.nodeDict['A'])].weight)
        self.assertEqual(1, graph.edgeDict[Edge.genId(graph.nodeDict['A'], graph.nodeDict['D'])].weight)

    def testDepthFirstSearchFindPath(self):
        text = 'AB1;AC1;CD1;BD1;CF1;BA1;FC1'
        graph = GraphSupport.buildGraph(text)
        originNode = graph.nodeDict['A']
        goalNode = graph.nodeDict['F']
        
        path = DepthFirstSearch.findPath(graph, originNode, goalNode)

        self.assertEqual(3, len(path))
        self.assertEqual('A', path[0])
        self.assertEqual('C', path[1])
        self.assertEqual('F', path[2])


        path = DepthFirstSearch.findPath(graph, originNode, Node('H'))
        self.assertTrue(path is None)

    def testBreadthFirstSearchFindAllPaths(self):
        text = 'AB1;AC1;CD1;BD1;CF1;BA1;FC1;BF1;DF1'

        graph = GraphSupport.buildGraph(text)
        originNode = graph.nodeDict['A']
        goalNode = graph.nodeDict['F']
        
        pathList = BreadthFirstSearch.findAllPath(graph, originNode, goalNode)

        self.assertEquals(4, len(pathList))
        expectedPaths = [['A', 'B', 'F'], ['A', 'B', 'D', 'F'], ['A', 'C', 'F'], ['A', 'C', 'D', 'F']]
        for path in expectedPaths:
            self.assertTrue(path in pathList)

        text = 'AB1;AE1;AD1;AF1;BC1;BD1;BA1;CD1;CF1;DA1;DE1;DF1;ED1'
        graph = GraphSupport.buildGraph(text)
        originNode = graph.nodeDict['A']
        goalNode = graph.nodeDict['F']
        
        pathList = BreadthFirstSearch.findAllPath(graph, originNode, goalNode)
        self.assertEquals(6, len(pathList))

    def testBreadthFirstSearchFindAllPathsIlegalArguments(self):
        text = 'AB1;AC1;CD1;BD1;CF1;BA1;FC1;BF1;DF1'

        graph = GraphSupport.buildGraph(text)
        originNode = None
        goalNode = graph.nodeDict['F']
        
        pathList = BreadthFirstSearch.findAllPath(graph, originNode, goalNode)
        self.assertEqual([], pathList)

        originNode = graph.nodeDict['F']
        goalNode = None
        
        pathList = BreadthFirstSearch.findAllPath(graph, originNode, goalNode)
        self.assertEqual([], pathList)

        originNode = graph.nodeDict['A']
        originNode.id = None
        goalNode = graph.nodeDict['F']
        
        pathList = BreadthFirstSearch.findAllPath(graph, originNode, goalNode)
        self.assertEqual([], pathList)

        originNode = graph.nodeDict['A']        
        goalNode = graph.nodeDict['F']
        goalNode.id = None

        pathList = BreadthFirstSearch.findAllPath(graph, originNode, goalNode)
        self.assertEqual([], pathList)

        originNode = graph.nodeDict['A']        
        goalNode = graph.nodeDict['A']

        pathList = BreadthFirstSearch.findAllPath(graph, originNode, goalNode)
        self.assertEqual([], pathList)

    def testFindAllPathWithNoGoal(self):
        text = 'AB1;AC1;CD1;BD1;CF1;BA1;FC1;BF1;DF1'

        graph = GraphSupport.buildGraph(text)
        originNode = graph.nodeDict['A']

        pathList = BreadthFirstSearch.findAllPathWithNoGoal(graph, originNode, 1)
        self.assertTrue(['A', 'C'] in pathList) 
        self.assertTrue(['A', 'B'] in pathList) 
        self.assertEqual(2, len(pathList))

        pathList = BreadthFirstSearch.findAllPathWithNoGoal(graph, originNode)
        self.assertTrue(['A', 'C'] in pathList) 
        self.assertTrue(['A', 'B'] in pathList) 
        self.assertEqual(2, len(pathList))

        pathList = BreadthFirstSearch.findAllPathWithNoGoal(graph, originNode, 2)
        self.assertTrue(['A', 'C', 'D'] in pathList) 
        self.assertTrue(['A', 'C', 'F'] in pathList) 
        self.assertTrue(['A', 'B', 'D'] in pathList) 
        self.assertTrue(['A', 'B', 'A'] in pathList) 
        self.assertTrue(['A', 'B', 'F'] in pathList) 
        self.assertEqual(5, len(pathList))

        pathList = BreadthFirstSearch.findAllPathWithNoGoal(graph, originNode, 20)
        for p in pathList:
            self.assertEqual(21, len(p))
    
    def testFindAllPathWithNoGoalIlegalArguments(self):
        text = 'AB1;AC1;CD1;BD1;CF1;BA1;FC1;BF1;DF1'

        graph = GraphSupport.buildGraph(text)
        originNode = None
        pathList = BreadthFirstSearch.findAllPathWithNoGoal(graph, originNode, 1)
        self.assertEqual([], pathList)

        originNode = graph.nodeDict['A']
        originNode.id = None
        pathList = BreadthFirstSearch.findAllPathWithNoGoal(graph, originNode, 1)
        self.assertEqual([], pathList)
        

        



def main():
    unittest.main()

if __name__ == '__main__':
    main()
