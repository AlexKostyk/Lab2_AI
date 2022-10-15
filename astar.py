def astar_method(start, end, graph, node_cost):
    direct_distance = {'Вильнюс': 543, 'Витебск': 558, 'Воронеж': 754, 'Волгоград': 1156,
                       'Калининград': 740, 'Каунас': 608, 'Киев': 134, 'Житомир': 0,
                       'Кишинев': 359, 'С.Петербург': 1082, 'Москва': 855, 'Мурманск': 2095,
                       'Орел': 593, 'Одесса': 446, 'Рига': 802, 'Таллинн': 1051,
                       'Харьков': 540, 'Ярославль': 1098, 'Уфа': 1901, 'Брест': 402,
                       'Ниж.Новгород': 1219, 'Даугавпилс': 640, 'Донецк': 709,
                       'Казань': 1493, 'Минск': 412, 'Симферополь': 717, 'Самара': 1507}
    visited = [start]
    min_node = None
    while end not in visited:
        for node in visited:
            min_all_distance = 10000
            for cur_node in graph[node]:
                if ((direct_distance[cur_node] + find_node_cost(node_cost, node, cur_node)) < min_all_distance) and (
                        find_node_cost(node_cost, node, cur_node) is not None):
                    if cur_node not in visited:
                        min_all_distance = direct_distance[cur_node] + find_node_cost(node_cost, node, cur_node)
                        min_node = cur_node
            if min_node not in visited:
                visited.append(min_node)
            if end in visited:
                break
    return visited


def find_node_cost(node_cost, start, end):
    for i in node_cost:
        if (i[1] == start and i[2] == end) or (i[2] == start and i[1] == end):
            return i[0]
    return None
