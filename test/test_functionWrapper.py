from unittest import TestCase
from functionwrapper import FunctionWrapper


class TestFunctionWrapper(TestCase):
    def test_should_set_function(self):
        function_wrapper = FunctionWrapper(lambda input: input[0] + input[1], 2, 'add')
        result=function_wrapper.function([1, 2])
        self.assertEqual(function_wrapper.function([1, 2]), 3)
