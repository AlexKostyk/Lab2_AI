def make_graph(city1, city2):
    graph = {}
    for city in city1:
        graph[city] = find_node(city, city1, city2)
    for city in city2:
        graph[city] = find_node(city, city2, city1)
    return graph


def find_node(city, city1, city2):
    array = []
    count = 0
    for i in city1:
        if city == i:
            array.append(city2[count])
        count += 1
    return array


