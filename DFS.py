def dfs_method(start, end, graph, visited=[]):
    if end in visited:
        return visited
    visited.append(start)
    for next in graph[start]:
        if next not in visited:
            dfs_method(next, end, graph, visited)
    return visited

