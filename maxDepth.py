def maxdepth_method(start, end, graph, maxdepth=5, path=[], visited=[]):
    if depth_loop(start, end, graph, maxdepth, path, visited):
        return path

def depth_loop(start, end, graph, maxdepth, path, visited):
    if start == end:
        path.append(start)
        return True
    if maxdepth <= 0:
        return False
    if start not in visited:
        path.append(start)
        visited.append(start)
    for cur_node in graph[start]:
        if depth_loop(cur_node, end, graph, maxdepth - 1, path, visited):
            return True
    return False
