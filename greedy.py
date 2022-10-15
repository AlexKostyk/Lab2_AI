def greedy_method(start, end, graph):
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
            min_distance = 3000
            for cur_node in graph[node]:
                if direct_distance[cur_node] < min_distance:
                    if cur_node not in visited:
                        min_distance = direct_distance[cur_node]
                        min_node = cur_node
            if min_node not in visited:
                visited.append(min_node)
            if end in visited:
                break
    return visited

