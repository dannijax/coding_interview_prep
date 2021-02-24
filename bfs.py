def bfs(graph, visited, node):
    queue = []
    visited.append(node)
    queue.append(node)

    while queue:
        s = queue.pop(0)
        print(s)
        for elem in graph[s]:
            if elem not in visited:
                visited.append(elem)
                queue.append(elem)
    return visited


graph = {
  'A' : ['B','C'],
  'B' : ['D', 'E'],
  'C' : ['F'],
  'D' : [],
  'E' : ['F'],
  'F' : []
}

visited = []

print(bfs(graph, visited, 'A'))