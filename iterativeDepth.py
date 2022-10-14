import maxDepth


def iterative_method(start, end, graph, path=[], visited=[]):
    for depth in range(4):
        if end not in path:
            path = []
            visited = []
        if maxDepth.depth_loop(start, end, graph, depth, path, visited):
            return path
