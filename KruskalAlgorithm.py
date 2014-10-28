# -*- coding: utf-8 -*-
"""
Created on Tue Oct 28 11:21:38 2014

@author: ivan lepoutre
"""

class KruskalAlgorithm:
    
    
    def __init__(self, graph):
        self.graph = graph
        
    
    def sort_edges(self):
        """
        Returns sorted list of edges. 
        """
        
        if not self.graph.edges:
            raise ValueError('the graph has no edge.')
        else:
            return self.graph.edges.sort()