
def maxdepth_method(start, end, graph, visited=None, maxdepth=4):
    if visited is None:
        visited = []
    if end in visited:
        return visited
    visited.append(start)
    for next in graph[start]:
        if next not in visited and maxdepth >= 0:
            maxdepth -= 1
            maxdepth_method(next, end, graph, visited, maxdepth)
        else:
            maxdepth += 1
    return visited
