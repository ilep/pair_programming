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

import math

class Node:
    """
    This class represents a node in the graph
    """
    
    def __init__(self, x, y, index):
        if isinstance(x, int) and isinstance(y, int) and isinstance(index, int):
            self.x = x
            self.y = y
            self.index = index
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
    
    def __init__(self, node1, node2, weight = None):
        if isinstance(node1, Node) and isinstance(node2, Node) and isinstance(weight, float):
            if node1 != node2:
                self.node1 = node1
                self.node2 = node2
                if weight is not None:
                    self.weight = weight
                else:
                    self.weight = self._compute_length(self)
            else:
                raise ValueError()
        else:
            raise AttributeError()

    def _compute_length(self):
        """
        Returns the length between node1 and node2.
        """
        return math.sqrt( pow(self.node1.x - self.node2.x, 2) + pow(self.node1.y - self.node2.y, 2) )


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
    
    def _sort_edges(self):
        """
        Recomputes a new sorted by weight self.edges set
        """
        if not self.edges:
            raise ValueError('the graph has no edge.')
        else:
            list_edges = list(self.edges)
            list_edges.sort(key=lambda x: x.weight, reverse=True)
            self.edges = set(list_edges)
                
    def kruskal(self):
        pass               














