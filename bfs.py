#  bfs.py
#  Breadth First Search creates a tree of a graph by first going as far
#  through the graph as possible and then working its way backward
#  Source: Dr. Chenyi Hu
#  Contributed by: Ross Adams

def bfs(graph, start):
    visited, queue = set(), [start]
    p =[]
    while queue:
        vertex = queue.pop(0)
        if vertex not in visited:
            visited.add(vertex)
            p.append(vertex)
            queue.extend(graph[vertex] - visited)
    return p


