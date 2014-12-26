from Graph import *
import math


def main():
	text = 'AB5;BC4;CD8;DC8;DE6;AD5;CE2;EB3;AE7'
	graph = GraphSupport.buildGraph(text)
	
	
	#1. The distance of the route A-B-C.
	originNode = graph.nodeDict['A']
	goalNode = graph.nodeDict['C']
	pathList = BreadthFirstSearch.findAllPath(graph, originNode, goalNode, 2)
	found = False

	for path in pathList:
		if path == ['A', 'B', 'C']:
			found = True
			print '1. The distance of the route A-B-C:', graph.getPathCost(path)
	if not found:
		print '1. The distance of the route A-B-C', 'NO SUCH ROUTE'

	#2. The distance of the route A-D.
	originNode = graph.nodeDict['A']
	goalNode = graph.nodeDict['D']
	pathList = BreadthFirstSearch.findAllPath(graph, originNode, goalNode, 1)
	found = False

	for path in pathList:
		if path == ['A', 'D']:
			found = True
			print '2. The distance of the route A-D:', graph.getPathCost(path)
	if not found:
		print '2. The distance of the route A-D:', 'NO SUCH ROUTE'

	#3. The distance of the route A-D-C.
	originNode = graph.nodeDict['A']
	goalNode = graph.nodeDict['C']
	pathList = BreadthFirstSearch.findAllPath(graph, originNode, goalNode, 2)
	found = False

	for path in pathList:
		if path == ['A', 'D', 'C']:
			found = True
			print '3. The distance of the route A-D-C:', graph.getPathCost(path)
	if not found:
		print '3. The distance of the route A-D-C:', 'NO SUCH ROUTE'

	#4. The distance of the route A-E-B-C-D.
	originNode = graph.nodeDict['A']
	goalNode = graph.nodeDict['D']
	pathList = BreadthFirstSearch.findAllPath(graph, originNode, goalNode, 4)
	found = False

	for path in pathList:
		if path == ['A', 'E', 'B', 'C', 'D']:
			found = True
			print '4. The distance of the route A-E-B-C-D:', graph.getPathCost(path)
	if not found:
		print '4. The distance of the route A-E-B-C-D:', 'NO SUCH ROUTE'

	#5. The distance of the route A-E-D.
	originNode = graph.nodeDict['A']
	goalNode = graph.nodeDict['D']
	pathList = BreadthFirstSearch.findAllPath(graph, originNode, goalNode, 4)
	found = False

	for path in pathList:
		if path == ['A', 'E','D']:
			found = True
			print '5. The distance of the route A-E-D:', graph.getPathCost(path)
	if not found:
		print '5. The distance of the route A-E-D:', 'NO SUCH ROUTE'

	#6. The number of trips starting at C and ending at C with a maximum of 3 stops.  
	#In the sample data below, there are two such trips: C-D-C (2 #stops). and C-E-B-C (3 stops).
	originNode = graph.nodeDict['C']
	pathList2Stops = BreadthFirstSearch.findAllPathWithNoGoal(graph, originNode, 2)
	pathList3Stops = BreadthFirstSearch.findAllPathWithNoGoal(graph, originNode, 3)
	sumPath = 0
	for path in pathList2Stops:
		if path[-1] == 'C':
			sumPath = sumPath + 1
	for path in pathList3Stops:
		if path[-1] == 'C':
			sumPath = sumPath + 1	
	print '6. The number of trips starting at C and ending at C with a max 3 stops:', sumPath

	#7. The number of trips starting at A and ending at C with exactly 4 stops.  
	#In the sample data below, there are three such trips: A to C (via #B,C,D); A to C (via D,C,D); and A to C (via D,E,B).
	originNode = graph.nodeDict['A']
	pathList4Stops = BreadthFirstSearch.findAllPathWithNoGoal(graph, originNode, 4)
	sumPath = 0
	for path in pathList4Stops:
		if path[-1] == 'C':
			sumPath = sumPath + 1
	print '7. The number of trips starting at A and ending at C with exactly 4 stops:', sumPath

	#8. The length of the shortest route (in terms of distance to travel) from A to C.
	originNode = graph.nodeDict['A']
	goalNode = graph.nodeDict['C']
	pathList = BreadthFirstSearch.findAllPath(graph, originNode, goalNode)
	found = False
	shortestLength = None
	shortestPath = None
	for path in pathList:		
		lengthRoute = graph.getPathCost(path)
		if shortestLength is None:
			shortestLength = lengthRoute
			shortestPath = path
		elif lengthRoute < shortestLength:
			shortestLength = lengthRoute
			shortestPath = path
		found = True
		
	if not found:
		print '8. The length of the shortest route (in terms of distance to travel) from A to C.', 'NO SUCH ROUTE'
	else:
		print '8. The length of the shortest route (in terms of distance to travel) from A to C.', shortestLength, shortestPath

	#9. The length of the shortest route (in terms of distance to travel) from B to B.
	originNode = graph.nodeDict['B']
	i =  1
	shortestLength = None
	shortestPath = None
	while i <= len(graph.nodeDict):
		pathList = BreadthFirstSearch.findAllPathWithNoGoal(graph, originNode, i)
		i = i + 1
		for path in pathList:		
			if path[-1] != 'B':
				continue
			lengthRoute = graph.getPathCost(path)
			if shortestLength is None:
				shortestLength = lengthRoute
				shortestPath = path
			elif lengthRoute < shortestLength:
				shortestLength = lengthRoute
				shortestPath = path
			found = True
	
	if not found:
		print '9. The length of the shortest route (in terms of distance to travel) from B to B.', 'NO SUCH ROUTE'
	else:
		print '9. The length of the shortest route (in terms of distance to travel) from B to B.', shortestLength, shortestPath

	#10.The number of different routes from C to C with a distance of less than 30.  In the sample data, the trips are: CDC, CEBC, CEBCDC, CDCEBC, #CDEBC, CEBCEBC, CEBCEBCEBC.
	originNode = graph.nodeDict['C']
	i =  1
	numberDiffRoute = 0	
	finished = False
	while True:
		if finished:
			break
		pathList = BreadthFirstSearch.findAllPathWithNoGoal(graph, originNode, i)
		i = i + 1
		if len(pathList) == 0:
			break
		finished = True
		for path in pathList:	
			cost = graph.getPathCost(path)			
			if (path[-1] == 'C') and  cost < 30:				
				numberDiffRoute = numberDiffRoute + 1
			if cost < 30:
				finished = False
			
	
	print '10.The number of different routes from C to C with a distance of less than 30.', numberDiffRoute 




if __name__ == '__main__':
    main()




#Problem One: Trains

#The local commuter railroad services a number of towns in Kiwiland.  Because of monetary concerns, all of the tracks are 'one-way.'  That is, #a route from Kaitaia to Invercargill does not imply the existence of a route from Invercargill to Kaitaia.  In fact, even if both of these #routes do happen to exist, they are distinct and are not necessarily the same distance!

#The purpose of this problem is to help the railroad provide its customers with information about the routes.  In particular, you will compute #the distance along a certain route, the number of different routes between two towns, and the shortest route between two towns.

#Input:  A directed graph where a node represents a town and an edge represents a route between two towns.  The weighting of the edge #represents the distance between the two towns.  A given route will never appear more than once, and for a given route, the starting and #ending town will not be the same town.

#Output: For test input 1 through 5, if no such route exists, output 'NO SUCH ROUTE'.  Otherwise, follow the route as given; do not make any #extra stops!  For example, the first problem means to start at city A, then travel directly to city B (a distance of 5), then directly to #city C (a distance of 4).

#1. The distance of the route A-B-C.
#2. The distance of the route A-D.
#3. The distance of the route A-D-C.
#4. The distance of the route A-E-B-C-D.
#5. The distance of the route A-E-D.
#6. The number of trips starting at C and ending at C with a maximum of 3 stops.  In the sample data below, there are two such trips: C-D-C (2 #stops). and C-E-B-C (3 stops).
#7. The number of trips starting at A and ending at C with exactly 4 stops.  In the sample data below, there are three such trips: A to C (via #B,C,D); A to C (via D,C,D); and A to C (via D,E,B).
#8. The length of the shortest route (in terms of distance to travel) from A to C.
#9. The length of the shortest route (in terms of distance to travel) from B to B.
#10.The number of different routes from C to C with a distance of less than 30.  In the sample data, the trips are: CDC, CEBC, CEBCDC, CDCEBC, #CDEBC, CEBCEBC, CEBCEBCEBC.

#Test Input:
#For the test input, the towns are named using the first few letters of the alphabet from A to D.  A route between two towns (A to B) with a #distance of 5 is represented as AB5.
#Graph: AB5, BC4, CD8, DC8, DE6, AD5, CE2, EB3, AE7
#Expected Output:
#Output #1: 9
#Output #2: 5
#Output #3: 13
#Output #4: 22
#Output #5: NO SUCH ROUTE
#Output #6: 2
#Output #7: 3
#Output #8: 9
#Output #9: 9
#Output #10: 7