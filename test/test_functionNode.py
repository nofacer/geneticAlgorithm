from unittest import TestCase
from functionnode import FunctionNode
from functionwrapper import FunctionWrapper
from paramnode import ParamNode
from constnode import ConstNode


class TestFunctionNode(TestCase):
    def setUp(self):
        add_wrapper = FunctionWrapper(lambda l: l[0] + l[1], 2, 'add')
        mul_wrapper = FunctionWrapper(lambda l: l[0] * l[1], 2, 'multiply')

        parameter_x = ParamNode(0, 'x')
        parameter_y = ParamNode(1, 'y')
        const_1 = ConstNode(1)

        # (x + 1 + y) * y
        self.node_tree = FunctionNode(mul_wrapper, [
            FunctionNode(add_wrapper, [FunctionNode(add_wrapper, [parameter_x, const_1]), parameter_y]), parameter_y])

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
