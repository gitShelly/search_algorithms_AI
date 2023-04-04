graph = {'a': {'b': 6, 'c': 3},
         'b': {'c': 1, 'd': 2},
         'c': {'b': 4, 'd': 8, 'e': 2},
         'd': {'e': 9},
         'e': {'d': 7}}


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


UCS(graph, 'a', 'd')

# is complete
# optimal




            
    

















