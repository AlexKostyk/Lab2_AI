import numpy as np
import BFC
from auxiliary import make_graph


city1 = np.loadtxt('data.txt', dtype = 'str', usecols=(0), encoding='utf-8')
city2 = np.loadtxt('data.txt', dtype = 'str', usecols=(1), encoding='utf-8')
distance = np.loadtxt('data.txt', dtype = 'i2', usecols=(2), encoding='utf-8')
graph = make_graph(city1, city2)
print(BFC.bfs_method('С.Петербург', 'Житомир', graph))




