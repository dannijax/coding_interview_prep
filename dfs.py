#implement dfs in python

def dfs(graph, node):
    visited = set()

    if node not in visited:
        visited.add(node)
        for element in graph[node]:
            dfs(graph, element)

    print(visited)


graph = {
    'A' : ['B','C'],
    'B' : ['D', 'E'],
    'C' : ['F'],
    'D' : [],
    'E' : ['F'],
    'F' : []
}

dfs(graph, 'A')