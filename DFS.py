
def dfs_method(start, end, graph, visited=None):
    if visited is None:
        visited = []
    if end in visited:
        return visited
    visited.append(start)
    for next in graph[start]:
        if next not in visited:
            dfs_method(next, end, graph, visited)
    return visited

