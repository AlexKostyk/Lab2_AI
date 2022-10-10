import numpy as np
from BFS import bfs_method
from auxiliary import make_graph


city1 = np.loadtxt('data.txt', dtype = 'str', usecols=(0), encoding='utf-8')
city2 = np.loadtxt('data.txt', dtype = 'str', usecols=(1), encoding='utf-8')
distance = np.loadtxt('data.txt', dtype = 'i2', usecols=(2), encoding='utf-8')
graph = make_graph(city1, city2)

bfs = bfs_method('С.Петербург', 'Житомир', graph)
print('Поиск в ширину:')
print(bfs)
print(graph)




