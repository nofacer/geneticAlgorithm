from visualize_tree import draw


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

    def vis(self):
        draw(self)
