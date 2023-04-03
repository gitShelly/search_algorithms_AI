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

visited=[]
queue=[]
def BFS(visited,graph,node):
    visited.append(node)
    queue.append(node)
    while queue:
        m=queue.pop(0)
        print(m,end=' ')
        for neighbour in graph[m]:
            if neighbour  not in visited:
                visited.append(neighbour)
                queue.append(neighbour)

print("The BFS sequence of the following graph system is: ")
BFS(visited,graph,'A')

#complete
#optimal when path cost are constant

