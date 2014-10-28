# -*- coding: utf-8 -*-
"""
Created on Tue Oct 28 11:27:28 2014

@author: ivan lepoutre
"""

from Graph import Node, Edge, Graph
import os 


def construct_graph(path = None):
    """
    Returns a graph object built from input.txt
    """
    
    graph = Graph()
    
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
                    graph.N = N
                else: 
                    M = int(parsed[0])
                    graph.M = M
            else: # Line define a Node (x, y) or an Edge (index_node1, index_node2)
                if row <= N: # If line define a node
                    x = int(parsed[0])
                    y = int(parsed[1])
                    index = row
                    graph.add_node( Node(x, y, index) )
                else: # Else line define an edge
                    index1 = int(parsed[0])
                    index2 = int(parsed[1])
                    node1 = graph._get_node(index1)
                    node2 = graph._get_node(index2)
                    try:
                        graph.add_edge(Edge(node1, node2)) # Lengths of edges as weights
                    except AttributeError, e:
                        print e
            row = row + 1 # Next line...    
    return graph
    
    
    
    
    
    
    
    