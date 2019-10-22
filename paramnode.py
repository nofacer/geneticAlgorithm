class ParamNode:
    def __init__(self, idx, name):
        self.idx = idx
        self.name = name

    def forward(self, input):
        return input[self.idx]

    def display(self, indent):
        return "{}{}\n".format(" " * indent, self.name)

    def cal_node_amount(self):
        return 1
