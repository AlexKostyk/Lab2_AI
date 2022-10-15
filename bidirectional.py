def bidirectional_method(start, end, graph):
    # Cловарь активных в данный момент вершин с соответствующими им путями
    active_node_dict = {start: [start], end: [end]}
    visited = set()
    path = []
    while len(active_node_dict) > 0:

        # Создание копии вершин, чтобы можно было изменять исходный словарь
        vertices = list(active_node_dict.keys())
        for node in vertices:
            path.append(node)
            cur_node = active_node_dict[node]
            origin = cur_node[0]
            # Проверка на наличие новых путей
            current_neighbours = set(graph[node]) - visited
            # Проверка попали ли пути в vertices
            if len(current_neighbours.intersection(vertices)) > 0:
                for meeting in current_neighbours.intersection(vertices):
                    # Проверка, что бы два пути не начинались в одном и том же месте
                    if origin != active_node_dict[meeting][0]:
                        # Переворот пути
                        active_node_dict[meeting].reverse()
                        # Объединение результата
                        return active_node_dict[node] + active_node_dict[meeting]

            #  Проверка нет ли новых путей, чтобы расширить текущие пути
            if len(set(current_neighbours) - visited - set(vertices)) == 0:
                # Если нет, то удаляется текущий путь и записывается конечная точка в visited
                active_node_dict.pop(node, None)
                visited.add(node)
            else:
                # Иначе расширяется путь, удаляется предыдущий путь и обновляется visited
                for next_node in current_neighbours - visited - set(vertices):
                    active_node_dict[next_node] = cur_node + [next_node]
                    vertices.append(next_node)
                active_node_dict.pop(node, None)
                visited.add(node)
    return visited
