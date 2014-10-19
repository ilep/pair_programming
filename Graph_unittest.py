import unittest
from Graph import Node

class NodeTestCase(unittest.TestCase):
    
    def test_raise_attribute_error_if_coordinates_are_not_integer(self):
        """
        On test qu'une erreur est jetee lorsque l'un des parametre n'est pas entier
        """
        with self.assertRaises(AttributeError):
            node = Node("3", 4)
            
        with self.assertRaises(AttributeError):
            node = Node(4, 4.3)

        with self.assertRaises(AttributeError):
            node = Node(None, 4)
    
    def test_integer_parameters_are_accepted(self):
        node = Node(1, 1)
        
        self.assertEqual(1, node.x)
        self.assertEqual(1, node.y)

if __name__ == '__main__':
    unittest.main()