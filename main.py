# -*- coding: utf-8 -*-
"""
Created on Tue Oct 28 11:24:24 2014

@author: ivan lepoutre
"""

from utils import construct_graph
from KruskalAlgorithm import KruskalAlgorithm

graph = construct_graph()

ka = KruskalAlgorithm(graph)
A = ka.kruskal()
print(A)    