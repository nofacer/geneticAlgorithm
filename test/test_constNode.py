from unittest import TestCase
from Nodes import ConstNode


class TestConstNode(TestCase):
    def test_should_return_value(self):
        const_node = ConstNode(6)
        self.assertEqual(const_node.forward([1, 2]), 6)

    def test_should_display_with_indent(self):
        const_node = ConstNode(6)
        expect_result = "  6\n"
        self.assertEqual(const_node.display(2), expect_result)
