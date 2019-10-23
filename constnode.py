class ConstNode:
    def __init__(self, value):
        self.value = value
        self.name = str(value)
        self.id = None

    def forward(self, input):
        return self.value

    def display(self, indent):
        return "{}{}\n".format(" " * indent, self.value)

    def cal_node_amount(self):
        return 1
