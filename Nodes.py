class ConstNode:
    def __init__(self, value):
        self.value = value
        self.name = str(value)
        self.id = None

    def forward(self, input):
        return self.value

    def display(self, indent=0):
        return "{}{}\n".format(" " * indent, self.value)

    def cal_node_amount(self):
        return 1


class FunctionNode:
    def __init__(self, function_wrapper, children):
        self.function = function_wrapper.function
        self.children = children
        self.name = function_wrapper.name
        self.node_amount = None
        self.max_child_amount = None
        self.id = None

    def __str__(self):
        return self.display()

    def forward(self, input):
        results = [n.forward(input) for n in self.children]
        return self.function(results)

    def display(self, indent=0):
        display_string = ""
        display_string += "{}{}\n".format(' ' * indent, self.name)
        for child in self.children:
            display_string += child.display(indent + 1)
        return display_string


class ParamNode:
    def __init__(self, idx, name):
        self.idx = idx
        self.name = name
        self.id = None

    def forward(self, input):
        return input[self.idx]

    def display(self, indent=0):
        return "{}{}\n".format(" " * indent, self.name)

    def cal_node_amount(self):
        return 1
