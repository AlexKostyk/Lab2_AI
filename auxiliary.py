def make_graph(city1, city2):
    graph = {}
    cities = []
    for city in city1:  # Объединение city1 с cities
        if city not in cities:
            cities.append(city)
    for city in city2:  # Объединение city2 с cities
        if city not in cities:
            cities.append(city)
    for city in cities:  # Перебор всех городов из cities и создание связей в словаре
        array = []
        graph[city] = find_node(city, city1, city2, array)
    return graph


def find_node(city, city1, city2, array):
    count = 0
    for i in city1:
        if city == i:
            array.append(city2[count])
        count += 1
    count = 0
    for i in city2:
        if city == i:
            array.append(city1[count])
        count += 1
    return array
