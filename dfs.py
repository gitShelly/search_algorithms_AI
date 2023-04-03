graph={
  'A' : ['B','C','D'],
  'B' : ['A', 'E','F'],
  'C' : ['A','F','G'],
  'D' : ['A','G','H'],
  'E' : ['B','I'],
  'F' : ['B','C'],
  'G' : ['C','D'],
  'H' : ["D"],
  'I' : []
}

visited_dfs=set()

def dfs(visited_dfs,graph,node):
    if node not in visited_dfs:
        print(node , end=' ')
        visited_dfs.add(node)
        for neighbour in graph[node]:
            dfs(visited_dfs,graph,neighbour)

print("The DFS sequence of the following graph system is: ")
dfs(visited_dfs,graph,'A')