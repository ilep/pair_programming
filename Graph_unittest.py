#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Tests:
1 - Vérifier que les coordonnées du Node sont bonnes après construction

"""

import unittest
from Graph import Node, Edge


class NodeTestCase(unittest.TestCase):
    
    def test_raise_attribute_error_if_coordinates_are_not_integer(self):
        """
        On test qu'une erreur est jetée lorsque l'un des paramètre n'est pas entier
        """
        with self.assertRaises(AttributeError):
            node = Node("3", 4)
            print node
            
        with self.assertRaises(AttributeError):
            node = Node(4, 4.3)
            print node

        with self.assertRaises(AttributeError):
            node = Node(None, 4)
            print node

    def test_integer_parameters_are_accepted(self):
        """
        L'objet est instancié et initialisé si les paramètres sont entiers
        """
        node = Node(1, -5)
        self.assertEqual(1, node.x)
        self.assertEqual(-5, node.y)

    def test_comparison_of_equal_nodes_returns_true(self):
        """
        Comparing two equal nodes returns true.
        """
        node1 = Node(-6, 4)
        node2 = Node(-6, 4)
        self.assertTrue(node1 == node2)


class EdgeTestCase(unittest.TestCase):

    def test_raise_attribute_error_if_one_extremity_is_not_a_node(self):
        """
        On test qu'une erreur est jetée lorsque l'une des extremités de l'arète n'est pas un Node.
        """

        with self.assertRaises(AttributeError):
            edge = Edge("heyyy", Node(3, 5), 6.4)
            print edge

        with self.assertRaises(AttributeError):
            edge = Edge(Node(-8, 2), None, 6.4)
            print edge


    def test_raise_value_error_if_same_extremities_are_passed(self):
        """
        On test qu'une erreur est jetée lorsque les deux extrémites du Edge sont égales.
        """

        with self.assertRaises(ValueError):
            edge = Edge(Node(1, 1), Node(1, 1), 6.4)
            print edge

    def test_an_edge_is_created_when_two_nodes_and_float_weight_are_given(self):
        """
        L'edge est instancié et initialisé si les paramètres sont deux nodes et un poids(float)
        """

        edge = Edge(Node(3, 6), Node(-43, 76), 4.5)
        self.assertEqual(Node(3, 6), edge.node1)
        self.assertEqual(Node(-43, 76), edge.node2)
        self.assertEqual(4.5, edge.weight)


class GraphTestCase(unittest.TestCase):
    pass  # TODO : ajouter les différents tests du Grahp


if __name__ == '__main__':
    unittest.main()