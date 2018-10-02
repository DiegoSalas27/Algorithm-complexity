graph = {'s':{'a': 2, 'd': 20}, 'a':{'e': 3}, 'b':{'c': 7}, 'c':{'f': 5}, 'd':{}, 'e':{'b': 1, 'g': 6, 'h': 4}, 'f':{'b': 0},
 'g':{'d': 2}, 'h':{'e': 2, 'g': 1}}

def Dijkstra(graph, start, goal):
    shortest_distance = {}
    predecessor = {}
    unseenNodes = graph
    infinity = 999999
    path =[]

    for node in unseenNodes:
        shortest_distance[node] = infinity
    shortest_distance[start] = 0

    while unseenNodes:
        minNode = None
        for node in unseenNodes:
            if minNode is None:
                minNode = node
            elif shortest_distance[node] < shortest_distance[minNode]:
                minNode = node
        
        for childNode, weight in graph[minNode].items():
            if weight + shortest_distance[minNode] < shortest_distance[childNode]:
                shortest_distance[childNode] = weight + shortest_distance[minNode]
                predecessor[childNode] = minNode
        unseenNodes.pop(minNode)
    
    currentNode = goal
    while currentNode != start:
        try:
            path.insert(0, currentNode)
            currentNode = predecessor[currentNode]
        except KeyError:
            print('Not reachable path')
            break
    
    if shortest_distance[goal] != infinity:
        print('Shortest distance is: ' + str(shortest_distance[goal]))
        print('The path is: ' + str(path))


Dijkstra(graph, 's', 'c')