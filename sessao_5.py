import pandas as pd

"""v = list((22, 55, 7, 9))
print(v)

print(v[2])
print(v[-1])"""
# MultiIndex em Arrays
arrays = [[1, 1, 2, 2], ['red', 'blue', 'red', 'blue']]
# print(pd.MultiIndex.from_arrays(arrays, names=('numeros', 'cores')))

"""
MultiIndex(levels=[[1, 2], ['blue', 'red']],
           codes=[[0, 0, 1, 1], [1, 0, 1, 0]],
           names=['number', 'color'])
"""

# Test
"""arrays = [[1, 1, 2, 2, 3, 3], ['red', 'blue', 'red', 'blue', 'black', 'black']]
print(pd.MultiIndex.from_arrays(arrays, names=('numeros', 'cores')))"""

#  MultiIndex com Prod. Cartesiano

numbers = [0, 1, 2]
colors = ['green', 'purple']
a = pd.MultiIndex.from_product([numbers, colors], names=['names', 'colors'])
print(a)
"""
MultiIndex(levels=[[0, 1, 2], ['green', 'purple']],
           codes=[[0, 0, 1, 1, 2, 2], [0, 1, 0, 1, 0, 1]],
           names=['number', 'color'])
"""
