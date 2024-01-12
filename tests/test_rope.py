import unittest
from parser import Node


class TestLeaf(unittest.TestCase):
    def test_case1(self):
        input_str = 'This is a test'
        node = Node(data=input_str)
        self.assertTrue(node.is_leaf())

    def test_case2(self):
        left_str = 'This is '
        left_node = Node(data=left_str)
        right_str = 'a test'
        right_node = Node(data=right_str)
        root_node = Node(left=left_node, right=right_node)
        self.assertFalse(root_node.is_leaf())
        self.assertTrue(left_node.is_leaf())
        self.assertTrue(right_node.is_leaf())

    def test_case3(self):
        left_str = 'This is '
        left_node = Node(data=left_str)
        right_str = 'a test'
        right_node = Node(data=right_str)
        first_left_node = Node(left=left_node, right=right_node)
        root_node = Node(left=first_left_node)
        self.assertFalse(root_node.is_leaf())
        self.assertFalse(first_left_node.is_leaf())
        self.assertTrue(left_node.is_leaf())
        self.assertTrue(right_node.is_leaf())

class TestConcat(unittest.TestCase):

    def test_case1(self):
        left_node = Node(data='This is ')
        right_node = Node(data='a test')
        result = left_node.concat(right_node)
        self.assertFalse(result.is_leaf())
        self.assertIs(result.left, left_node)
        self.assertIs(result.right, right_node)
        self.assertEqual(len(result), len(left_node))

class TestNodeLength(unittest.TestCase):
    def test_leaf_length(self):
        input_str = 'This is a test'
        node = Node(data=input_str)
        self.assertEqual(len(node), len(input_str))

    def test_single_split_length(self):
        left_str = 'This is '
        left_node = Node(data=left_str)
        right_str = 'a test'
        right_node = Node(data=right_str)
        root_node = Node(left=left_node, right=right_node)
        self.assertEqual(len(root_node), len(left_node))

    def test_double_split_length(self):
        left_str = 'This is '
        left_node = Node(data=left_str)
        right_str = 'a test'
        right_node = Node(data=right_str)
        first_left_node = Node(left=left_node, right=right_node)
        root_node = Node(left=first_left_node)
        self.assertEqual(len(root_node), len(left_node) + len(right_node))
        self.assertEqual(len(root_node), len(left_str) + len(right_str))
