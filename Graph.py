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
            raise AttributeError('error during init Edge')

    def _compute_length(self):
        """
        Returns the length between node1 and node2.
        """
        return math.sqrt( pow(self.node1.x - self.node2.x, 2) + pow(self.node1.y - self.node2.y, 2) )

    def __hash__(self): 
        return hash((self.node1, self.node2))

    def __str__(self):
        return "Edge between (" + str(self.node1) + ") AND (" + str(self.node2) + "), weight = " + str(self.weight)
        
        
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
            raise AttributeError('error during add_edge')

    def _get_node(self, index):
        """
        Returns a node given its index.
        """
        list_nodes = list(self.nodes)
        for node in list_nodes:
            if index == node.index:
                return node

    def _construct_graph(self, path = None):
        """
        Method to build the graph object from input.txt
        """
        
        if not path or not os.path.exists(os.path.join(os.getcwd(), 'input.txt')):
            path = os.path.join(os.getcwd(), 'input.txt')
        else: 
            raise IOError('No input.txt file.')
        
        with open(path, 'r') as input:
            N = None # Number of nodes
            M = None  # Number of edges
            row = 0 # Index of the row we are reading in our file. Incremented line after line.            
            for line in input:
                parsed = line.split()         
                if len(parsed) == 1: # Line define N = number of nodes or M = number of edges
                    if not N:
                        N = int(parsed[0])
                    else: 
                        M = int(parsed[0])
                else: # Line define a Node (x, y) or an Edge (index_node1, index_node2)
                    if row <= N: # If line define a node
                        x = int(parsed[0])
                        y = int(parsed[1])
                        index = row
                        self.add_node( Node(x, y, index) )
                    else: # Else line define an edge
                        index1 = int(parsed[0])
                        index2 = int(parsed[1])
                        node1 = self._get_node(index1)
                        node2 = self._get_node(index2)
                        try:
                            self.add_edge(Edge(node1, node2)) # Lengths of edges as weights
                        except AttributeError, e:
                            print e
                row = row + 1 # Next line...
    
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

    def __str__(self):
        str_graph = '------------------------------------------\n'
        str_graph = str_graph +'Il y a ' + str(len(self.edges)) + ' edges \n' 
        str_graph = str_graph + '------------------------------------------\n'
        COUNT = 0        
        for edge in list(self.edges): 
            str_graph = str_graph + str(COUNT) + " - " + str(edge) + '\n'
            COUNT = COUNT + 1
        return str_graph
                
    def kruskal(self):
        pass               


g = Graph()
g._construct_graph()
print(g)
g._sort_edges()
print(g)
#for i in range(len(g.nodes)):
#    print(list(g.nodes)[i])
