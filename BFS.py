from collections import deque


def bfs_method(start, end, graph):
    res = []
    queue = deque([start])  # Начальная вершина кладётся в очередь
    visited = {start: None}  # Словарь посещенных вершин
    tmp = end
    while queue:
        cur_node = queue.popleft()  # Пока очередь не пуста достаётся первый элемент
        if cur_node == end:
            break
        next_nodes = graph[cur_node]
        for next_node in next_nodes:
            if next_node not in visited:  # Добавление в словарь посещенных вершин всех смежных вершин
                queue.append(next_node)
                visited[next_node] = cur_node
    while tmp is not None:  # Выбор пути
        res.append(tmp)
        tmp = visited[tmp]

    return res[::-1]
