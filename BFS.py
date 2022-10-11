
def bfs_method(start, end, graph):
    visited = [start]
    cur_node = start
    count = 0
    while end not in visited:
        queue = graph[cur_node]
        cur_node = visited[count]
        count += 1
        for node in queue:
            if node not in visited:
                visited.append(node)
    return visited
