from unittest import TestCase
from utils import cal_node_amount, cal_max_children_number, create_layout
from functionnode import FunctionNode
from functionwrapper import FunctionWrapper
from paramnode import ParamNode
from constnode import ConstNode


class TestUtils(TestCase):
    def setUp(self):
        add_wrapper = FunctionWrapper(lambda l: l[0] + l[1], 2, 'add')
        mul_wrapper = FunctionWrapper(lambda l: l[0] * l[1], 2, 'multiply')

        parameter_x = ParamNode(0, 'x')
        parameter_y = ParamNode(1, 'y')
        const_1 = ConstNode(1)

        # (x + 1 + y) * y
        self.node_tree = FunctionNode(mul_wrapper, [
            FunctionNode(add_wrapper, [FunctionNode(add_wrapper, [parameter_x, const_1]), parameter_y]), parameter_y])

    def test_cal_node_amount(self):
        self.assertEqual(7, cal_node_amount(self.node_tree))

    def test_max_child_count(self):
        self.assertEqual(2, cal_max_children_number(self.node_tree))

    def test_create_layout(self):
        expect_result = (
            ['multiply_0', 'add_0', 'add_1', 'x_0', '1_0', 'y_0', 'y_1'],
            [(0, 1), (1, 2), (2, 3), (2, 4), (1, 5), (0, 6)]
        )
        self.assertEqual(expect_result, create_layout(self.node_tree))
