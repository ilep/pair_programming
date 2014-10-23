#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Kruskal algorithm implementation:
input.txt :
N
x1 y1
x2 y2
...
xN yN
M
i1 j1
i2 j2
...
iM jM

output.txt :
x1 y1
x2 y2
...
xN yN
M'
i1 j1
i2 j2
...
iM' jM'

Modeling (Node, Edge, Graph)
Sort algorithm
Algorithme de calcul d'arbre couvrant de poid min
"""
#-----------------------------------------------


class Node:
    """
    This class represents a node in the graph
    """
    
    def __init__(self, x, y):
        if isinstance(x, int) and isinstance(y, int):
            self.x = x
            self.y = y
        else:
            raise AttributeError()
    
    def __eq__(self, other):
        if isinstance(other, Node):
            return self.x == other.x and self.y == other.y
        else:
            raise AttributeError()
            
    def __ne__(self, other):
        return not self.__eq__(other)


class Edge:
    """
    This class represents an edge in the graph
    """
    
    def __init__(self, node1, node2, weight):
        if isinstance(node1, Node) and isinstance(node2, Node) and isinstance(weight, float):
            if node1 != node2:
                self.node1 = node1
                self.node2 = node2
                self.weight = weight
            else:
                raise ValueError()
        else:
            raise AttributeError()


class Graph:
    """
    This class represents the graph
    """
    
    def __init__(self):
        self.nodes = set()
        self.edges = set()
    
    def add_node(self, node):
        if isinstance(node, Node):
            self.nodes.add(node)
        else:
            raise AttributeError()
    
    def add_edge(self, edge):
        if isinstance(edge, Edge):
            self.edges.add(edge)
        else:
            raise AttributeError()