class FunctionNode:
    def __init__(self, function_wrapper, children):
        self.function = function_wrapper.function
        self.children = children
        self.name = function_wrapper.name

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

    def cal_node_amount(self):
        count = 1
        for child in self.children:
            count += child.cal_node_amount()
        return count
