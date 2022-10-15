import collections

def bfs_method(start, end, graph):
    visited = [start]
    queue = collections.deque([start])
    while end not in visited:
        cur_node = queue.popleft()
        for next in graph[cur_node]:
            if next not in visited:
                visited.append(next)
                queue.append(next)
    return visited
