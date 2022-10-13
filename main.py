import numpy as np
from BFS import bfs_method
from DFS import dfs_method
from maxDepth import maxdepth_method
from iterativeDepth import iterative_method
from auxiliary import make_graph


city1 = np.loadtxt('data.txt', dtype = 'str', usecols=(0), encoding='utf-8')
city2 = np.loadtxt('data.txt', dtype = 'str', usecols=(1), encoding='utf-8')
distance = np.loadtxt('data.txt', dtype = 'i2', usecols=(2), encoding='utf-8')
graph = make_graph(city1, city2)

bfs = bfs_method('С.Петербург', 'Житомир', graph)
dfs = dfs_method('С.Петербург', 'Житомир', graph)
maxdepth = maxdepth_method('С.Петербург', 'Житомир', graph)
iterativedepth = iterative_method('С.Петербург', 'Житомир', graph)

print('Все посещенные вершины в методе BFS:')
print(bfs)
print('Все посещенные вершины в методе DFS:')
print(dfs)
print(maxdepth)
print(iterativedepth)
