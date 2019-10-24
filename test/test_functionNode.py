from unittest import TestCase
from utils import *


class TestFunctionNode(TestCase):
    def setUp(self):
        self.node_tree = example_tree()

    def test_forward(self):
        result = self.node_tree.forward([2, 3])
        self.assertEqual(result, 18)

    def test_display(self):
        result = self.node_tree.display()
        expected_result = "multiply\n" \
                          + " add\n" \
                          + "  add\n" \
                          + "   x\n" \
                          + "   1\n" \
                          + "  y\n" \
                          + " y\n"
        self.assertEqual(expected_result, result)
