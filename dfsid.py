from collections import defaultdict


class Graph:

    def __init__(self, vertices):

        # No. of vertices
        self.V = vertices

        # default dictionary to store graph
        self.graph = defaultdict(list)

    # function to add an edge to graph
    def addEdge(self, u, v):
        self.graph[u].append(v)

    # A function to perform a Depth-Limited search
    # from given source 'src'
    def DLS(self, src, target, maxDepth):

        if src == target:
            return True

        # If reached the maximum depth, stop recursing.
        if maxDepth <= 0:
            return False

        # Recur for all the vertices adjacent to this vertex
        for i in self.graph[src]:
            if (self.DLS(i, target, maxDepth-1)):
                return True
        return False

    # IDDFS to search if target is reachable from v.
    # It uses recursive DLS()
    def IDDFS(self, src, target, maxDepth):

        # Repeatedly depth-limit search till the
        # maximum depth
        for i in range(maxDepth):
            if (self.DLS(src, target, i)):
                return True
        return False


# Create a graph given in the above diagram
g = Graph(4)
g.addEdge(1, 2)
g.addEdge(1, 3)
g.addEdge(1, 4)
g.addEdge(2, 1)
g.addEdge(2, 3)
g.addEdge(2, 4)
g.addEdge(3, 1)
g.addEdge(3, 2)
g.addEdge(3, 4)
g.addEdge(4, 1)
g.addEdge(4, 2)
g.addEdge(4, 3)


target = 4
maxDepth = 3
src = 1

for i_depth in range(1, maxDepth+1):
    print(i_depth)
    if g.IDDFS(src, target,i_depth) == True:
        print("Target is reachable from source " +
              "within max depth")
    else:
        print("Target is NOT reachable from source " +
          "within max depth")
# graph = {
#     'V2': [('V4', 67), ('V3', 16), ('V5', 20)],
#     'V4': [('V2', 67), ('V3', 45), ('V5', 8)],
#     'V3': [('V2', 16), ('V4', 45), ('V5', 34)],
#     'V5': [('V2', 20), ('V4', 8), ('V3', 34)]
# }

# def get_neighbors(node):
#     return [neighbor for neighbor, weight in graph[node]]

# def DFS_iterative_deepening(start, goal, depth_limit):
#     for depth in range(depth_limit):
#         visited = set()
#         stack = [(start, 0)]
#         while stack:
#             node, node_depth = stack.pop()
#             print(f"Iteration: {node}, Depth: {node_depth}")
#             if node == goal:
#                 print(f"Found at depth {node_depth}")
#                 return True, node_depth
#             if node_depth < depth:
#                 for neighbor, weight in graph[node]:
#                     if neighbor not in visited:
#                         stack.append((neighbor, node_depth+1))
#                         visited.add(neighbor)
#     return False, -1

# found, depth = DFS_iterative_deepening('V2', 'V5', 5)
# print(f"Found: {found}, Depth: {depth}")

