class FunctionWrapper:
    def __init__(self, function, child_count, name):
        self.function = function
        self.child_count = child_count
        self.name = name


class Functions:
    def __init__(self):
        self.add_f = FunctionWrapper(lambda l: l[0] + l[1], 2, 'add')
        self.subtract_f = FunctionWrapper(lambda l: l[0] - l[1], 2, 'subtract')
        self.multiply_f = FunctionWrapper(lambda l: l[0] * l[1], 2, 'multiply')
        self.if_f = FunctionWrapper(if_function, 3, 'if')
        self.greater_f = FunctionWrapper(greater_function, 2, 'greater')


def if_function(l):
    if l[0] > 0:
        return l[1]
    else:
        return l[2]


def greater_function(l):
    if l[0] > l[1]:
        return 1
    else:
        return 0
