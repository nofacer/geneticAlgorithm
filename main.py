from utils import *
from Functions import Functions

functions = Functions()

flist = [functions.add_f, functions.subtract_f, functions.multiply_f, functions.if_f, functions.greater_f]
random_tree = make_random_tree(2, flist)

draw(random_tree)
print(random_tree.forward([1, 2]))
