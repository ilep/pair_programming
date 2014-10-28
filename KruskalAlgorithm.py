# -*- coding: utf-8 -*-
"""
Created on Tue Oct 28 11:21:38 2014

@author: ivan lepoutre
"""

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
            raise ValueError('the graph has no edge.')
        else:
            return self.graph.edges.sort()
    
    def __make_sets(self):
        nodes_sets = {}        
        for node in self.graph.nodes:
            nodes_sets[node.index] = set([node])
        
    
    def kruskal(self):
        """
        Computes kruskal algorithm on graph. Returns minimal spanning tree A.
        """
        
        A = graph() # Minimal spanning tree.       
        for edge in self.sorted_edges:
                        
            print 'hey'
            