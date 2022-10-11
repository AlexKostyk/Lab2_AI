
def iterative_method(start, end, graph, visited=None, depth=0, max_depth=1):
    if visited is None:
        visited = []
    if end in visited:
        return visited
    visited.append(start)
    for next in graph[start]:
        if next not in visited and depth <= max_depth:
            depth += 1
            iterative_method(next, end, graph, visited, depth, max_depth)
        else:
            depth -= 1
            max_depth += 1
    return visited
