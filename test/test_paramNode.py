from unittest import TestCase
from Nodes import ParamNode


class TestParamNode(TestCase):
    def test_should_get_related_parameter(self):
        parameter_node = ParamNode(0, 'x')
        self.assertEqual(parameter_node.forward([1, 2]), 1)

    def test_should_display_with_indent(self):
        parameter_node = ParamNode(1, 'x')
        expect_result = "   x\n"
        self.assertEqual(parameter_node.display(3), expect_result)
