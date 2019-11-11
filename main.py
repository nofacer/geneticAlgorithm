from utils import *

from Env import *




dataset = build_hidden_set()
rank_function = getrankfunction(dataset)
t=evolve(2,200,rank_function)
draw(t)