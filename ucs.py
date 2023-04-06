graph = {'0': {'1': 2, '2': 6},
    '1': {'3': 5,'0':2},
    '2': {'3': 8, '0': 6},
    '3': {'4': 10, '5': 15, '2': 8,'1':5},
    '4': {'6': 2, '3': 10},
    '5': {'6': 6, '3': 15},
    '6': {'4': 2, '5': 6}}
         


def min_and_predecessor(graph, src):
    queue = [src]
    minDistances = {v: float("inf") for v in graph}
    minDistances[src] = 0
    predecessor = {}

    while queue:
        currentNode = queue.pop(0)
        for neighbor in graph[currentNode]:
            newDist = minDistances[currentNode]+graph[currentNode][neighbor]

            if newDist < minDistances[neighbor]:
                minDistances[neighbor] = min(newDist, minDistances[neighbor])
                queue.append(neighbor)
                predecessor[neighbor] = currentNode

    return minDistances, predecessor


def UCS(graph, src, dest):
    minDistances, predecessor = min_and_predecessor(graph, src)
    currentNode = dest
    path = []
    while currentNode != src:
        if currentNode not in predecessor:
            print('path is not reachable')
            break
        else:
            path.insert(0, currentNode)
            currentNode = predecessor[currentNode]
    path.insert(0, src)

    if dest in minDistances and minDistances[dest] != float('inf'):
        print('Shortest distance is ' + str(minDistances[dest]))
        print('and path is ' + str(path))


UCS(graph, '0', '6')

# is complete
# optimal


# def min_predecessor(graph,src):
#     queue=[src]
#     min_distances={v:float('inf')for v in graph}
#     min_distances[src]=0
#     predecessor={}
    
#     while queue:
#         current_node=queue.pop(0)
#         for neighbor in graph[current_node]:
#             new_dist=min_distances[current_node] + graph[current_node][neighbor]
            
#             if new_dist<min_distances[neighbor]:
#                 min_distances[neighbor]=min(new_dist,min_distances[neighbor])
#                 queue.append[neighbor]
#                 predecessor[neighbor]=current_node
    
#     return min_distances,predecessor




            
    

















