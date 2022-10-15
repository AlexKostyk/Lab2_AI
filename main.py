import numpy as np
from BFS import bfs_method
from DFS import dfs_method
from maxDepth import maxdepth_method
from iterativeDepth import iterative_method
from bidirectional import bidirectional_method
from greedy import greedy_method
from astar import astar_method
from auxiliary import make_graph
from auxiliary import node_cost

city1 = np.loadtxt('data.txt', dtype='str', usecols=(0), encoding='utf-8')
city2 = np.loadtxt('data.txt', dtype='str', usecols=(1), encoding='utf-8')
distance = np.loadtxt('data.txt', dtype='i2', usecols=(2), encoding='utf-8')
graph = make_graph(city1, city2)
node_cost = node_cost(city1, city2, distance)

bfs = bfs_method('С.Петербург', 'Житомир', graph)
dfs = dfs_method('С.Петербург', 'Житомир', graph)
maxdepth = maxdepth_method('С.Петербург', 'Житомир', graph)
iterativedepth = iterative_method('С.Петербург', 'Житомир', graph)
bidirectional = bidirectional_method('С.Петербург', 'Житомир', graph)
greedy = greedy_method('С.Петербург', 'Житомир', graph)
astar = astar_method('С.Петербург', 'Житомир', graph, node_cost)

print('Все посещенные вершины в методе BFS:')
print(bfs)
print('Все посещенные вершины в методе DFS:')
print(dfs)
print('Все посещенные вершины в методе DFS с ограничением глубины:')
print(maxdepth)
print('Все посещенные вершины в методе DFS с итерацией:')
print(iterativedepth)
print('Все посещенные вершины в методе двунаправленного поиска:')
print(bidirectional)
print('Все посещенные вершины в методе жадного поиска:')
print(greedy)
print('Все посещенные вершины в методе жадного поиска:')
print(astar)
