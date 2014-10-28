# -*- coding: utf-8 -*-
"""
Created on Tue Oct 28 11:21:38 2014

@author: ivan lepoutre
"""

from Graph import Graph

class KruskalAlgorithm:
    
    
    def __init__(self, graph):
        self.graph = graph
        self.nodes_sets = self.__make_sets()
        self.sorted_edges = self.__sorts_edges()
        
    def __sorts_edges(self):
        """
        Returns sorted list of edges. 
        """
        
        if not self.graph.edges:
            raise ValueError('The graph has no edge.')
        else:
            return sorted(self.graph.edges, key=lambda x: x.weight)
    
    def __make_sets(self):
        nodes_sets = {}        
        for node in self.graph.nodes:
            nodes_sets[node.index] = set([node])
        return nodes_sets

    def print_set(self, node):
        string = "Set of Node " + str(node.index) + " : "
        for node in list(self.nodes_sets[node.index]):
            string = string + str(node.index) + " - "
        print string
    
    def kruskal(self):
        """
        Computes kruskal algorithm on graph. Returns minimal spanning tree A.
        """
        
        A = Graph() # Minimal spanning tree.   
    
        for edge in self.sorted_edges:
            if not self.nodes_sets[edge.node1.index] & self.nodes_sets[edge.node2.index]: 
                A.add_edge(edge)
                union = self.nodes_sets[edge.node1.index] | self.nodes_sets[edge.node2.index]
                self.nodes_sets[edge.node1.index] = union
                self.nodes_sets[edge.node2.index] = union                
                #print A
        return A