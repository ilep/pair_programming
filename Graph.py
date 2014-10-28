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
import os

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

    def __str__(self):
        return "Node " + str(self.index)+ " | x= " +str(self.x) + ", y= " +str(self.y) 

    def __hash__(self):
        return hash((self.x, self.y))            

class Edge:
    """
    This class represents an edge in the graph
    """
    
    def __init__(self, node1, node2, weight = None):
        if isinstance(node1, Node) and isinstance(node2, Node):
            if node1 != node2:
                self.node1 = node1
                self.node2 = node2
                if weight is not None and isinstance(weight, float):
                    self.weight = weight
                else:
                    self.weight = self._compute_length()
            else:
                raise ValueError()
        else:
            raise AttributeError('Error during init Edge')

    def _compute_length(self):
        """
        Returns the length between node1 and node2.
        """
        return math.sqrt( pow(self.node1.x - self.node2.x, 2) + pow(self.node1.y - self.node2.y, 2) )

    def __str__(self):
        return "Edge between (" + str(self.node1) + ") AND (" + str(self.node2) + "), weight = " + str(self.weight)
        
        
class Graph:
    """
    This class represents the graph
    """
    
    def __init__(self):
        self.nodes = list()
        self.edges = list()
        self.N = 0 # number of nodes
        self.M = 0 # number of edges
    
    def add_node(self, node):
        if isinstance(node, Node):
            if node not in self.nodes:
                self.nodes.append(node)
            else: 
                raise ValueError('Cannot insert a node that is already in graph')
        else:
            raise AttributeError()
            
    def add_edge(self, edge):
        if isinstance(edge, Edge):
            if edge not in self.edges:
                self.edges.append(edge)
            else: 
                raise ValueError('Cannot insert an edge that is already in graph')
        else:
            raise AttributeError('Error during add_edge')

    def _get_node(self, index):
        """
        Returns a node given its index.
        """
        for node in self.nodes:
            if index == node.index:
                return node

    def __str__(self):
        str_graph = '------------------------------------------\n'
        str_graph = str_graph +'Il y a ' + str(len(self.edges)) + ' edges \n' 
        str_graph = str_graph + '------------------------------------------\n'
        COUNT = 0        
        for edge in list(self.edges): 
            str_graph = str_graph + str(COUNT) + " - " + str(edge) + '\n'
            COUNT = COUNT + 1
        return str_graph
                              