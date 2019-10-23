from unittest import TestCase
from utils import *

class TestUtils(TestCase):
    def setUp(self):
        self.node_tree = exampletree()

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
