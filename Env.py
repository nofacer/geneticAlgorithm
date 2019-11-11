from random import randint, random
from utils import *
from copy import deepcopy
from math import log
from Functions import Functions

functions = Functions()
flist = [functions.add_f, functions.subtract_f, functions.multiply_f, functions.if_f, functions.greater_f]


def hidden_function(x, y):
    return x ** 2 + 2 * y + 3 * x + 5


def build_hidden_set():
    rows = []
    for i in range(200):
        x = randint(0, 40)
        y = randint(0, 40)
        rows.append([x, y, hidden_function(x, y)])
    return rows


def score_function(tree, s):
    dif = 0
    for data in s:
        v = tree.forward([data[0], data[1]])
        dif += abs(v - data[2])
    return dif


def mutate(t, pc, probchange=0.1):
    if random() < probchange:
        return make_random_tree(pc, flist)
    else:
        result = deepcopy(t)
        if hasattr(t, "children"):
            result.children = [mutate(c, pc, probchange) for c in t.children]
        return result


def crossover(t1, t2, probswap=0.7, top=1):
    if random() < probswap and not top:
        return deepcopy(t2)
    else:
        result = deepcopy(t1)
        if hasattr(t1, 'children') and hasattr(t2, 'children'):
            result.children = [crossover(c, choice(t2.children), probswap, 0)
                               for c in t1.children]
        return result


def getrankfunction(dataset):
    def rankfunction(population):
        scores = [(score_function(t, dataset), t) for t in population]
        scores.sort(key=lambda x: x[0])
        return scores

    return rankfunction


def evolve(parameter_number, population_size, rank_function, max_generation=500,
           mutation_rate=0.1, breeding_rate=0.4, pexp=0.7, pnew=0.05):
    def selectindex():
        return int(log(random()) / log(pexp))

    # Create a random initial population
    population = [make_random_tree(parameter_number, flist) for i in range(population_size)]
    for i in range(max_generation):
        scores = rank_function(population)
        print(scores[0][0])
        if scores[0][0] == 0: break

        # The two best always make it
        newpop = [scores[0][1], scores[1][1]]

        # Build the next generation
        while len(newpop) < population_size:
            if random() > pnew:
                newpop.append(mutate(
                    crossover(scores[selectindex()][1],
                              scores[selectindex()][1],
                              probswap=breeding_rate),
                    parameter_number, probchange=mutation_rate))
            else:
                # Add a random node to mix things up
                newpop.append(make_random_tree(parameter_number, flist))

        population = newpop
    scores[0][1].display()
    return scores[0][1]
