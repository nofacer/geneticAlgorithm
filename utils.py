from igraph import Graph
from plotly import graph_objects as go

from Functions import FunctionWrapper
from Nodes import ConstNode, FunctionNode, ParamNode
from random import *


def example_tree():
    add_wrapper = FunctionWrapper(lambda l: l[0] + l[1], 2, 'add')
    mul_wrapper = FunctionWrapper(lambda l: l[0] * l[1], 2, 'multiply')

    parameter_x = ParamNode(0, 'x')
    parameter_y = ParamNode(1, 'y')
    const_1 = ConstNode(1)

    # (x + 1 + y) * y
    node_tree = FunctionNode(mul_wrapper, [
        FunctionNode(add_wrapper, [FunctionNode(add_wrapper, [parameter_x, const_1]), parameter_y]), parameter_y])
    return node_tree


def cal_node_amount(node):
    count = 1
    if hasattr(node, 'children'):
        for child in node.children:
            count += cal_node_amount(child)
    return count


def cal_max_children_number(node):
    count = 1
    if hasattr(node, 'children'):
        count = max(count, len(node.children))
        for child in node.children:
            count = max(count, cal_max_children_number(child))
        return count

    else:
        return 0


def create_layout(node):
    node_list = []
    pool = {}
    edge = []

    def temp(tree_node, parent_id=None):
        if tree_node.name not in pool:
            new_name = tree_node.name + '_' + '0'
            pool[tree_node.name] = 1
        else:
            new_name = tree_node.name + '_' + str(pool[tree_node.name])
            pool[tree_node.name] += 1
        id = len(node_list)
        node_list.append(new_name)

        if parent_id is not None:
            edge.append((parent_id, id))

        if hasattr(tree_node, 'children'):
            for child in tree_node.children:
                temp(child, id)

    temp(node)
    return node_list, edge


def draw(node_tree):
    vertices_number = cal_node_amount(node_tree)
    vertices_labels = node_tree.display().replace(" ", "").strip().split("\n")  # DLR
    node_list, edge_list = create_layout(node_tree)

    G = Graph(n=vertices_number)
    G.add_edges(edge_list)

    lay = G.layout_reingold_tilford(mode="in", root=[0], rootlevel=None)

    position = {k: lay[k] for k in range(vertices_number)}
    Y = [lay[k][1] for k in range(vertices_number)]
    M = max(Y)

    E = [e.tuple for e in G.es]  # list of edges

    L = len(position)
    Xn = [position[k][0] for k in range(L)]
    Yn = [2 * M - position[k][1] for k in range(L)]
    Xe = []
    Ye = []
    for edge in E:
        Xe += [position[edge[0]][0], position[edge[1]][0], None]
        Ye += [2 * M - position[edge[0]][1], 2 * M - position[edge[1]][1], None]

    labels = vertices_labels

    fig = go.Figure()
    fig.add_trace(go.Scatter(x=Xe,
                             y=Ye,
                             mode='lines',
                             line=dict(color='rgb(210,210,210)', width=1),
                             hoverinfo='none'
                             ))
    fig.add_trace(go.Scatter(x=Xn,
                             y=Yn,
                             mode='markers',
                             name='bla',
                             marker=dict(symbol='circle-dot',
                                         size=50,
                                         color='#6175c1',  # '#DB4551',
                                         line=dict(color='rgb(50,50,50)', width=1)
                                         ),
                             text=labels,
                             hoverinfo='text',
                             opacity=0.8
                             ))

    def make_annotations(pos, text, font_size=10, font_color='rgb(250,250,250)'):
        L = len(pos)
        if len(text) != L:
            raise ValueError('The lists pos and text must have the same len')
        annotations = []
        for k in range(L):
            annotations.append(
                dict(
                    text=labels[k],  # or replace labels with a different list for the text within the circle
                    x=pos[k][0], y=2 * M - position[k][1],
                    xref='x1', yref='y1',
                    font=dict(color=font_color, size=font_size),
                    showarrow=False)
            )
        return annotations

    axis = dict(showline=False,  # hide axis line, grid, ticklabels and  title
                zeroline=False,
                showgrid=False,
                showticklabels=False,
                )

    fig.update_layout(title='Generated Program Tree',
                      annotations=make_annotations(position, vertices_labels),
                      font_size=18,
                      showlegend=False,
                      xaxis=axis,
                      yaxis=axis,
                      margin=dict(l=40, r=40, b=85, t=100),
                      hovermode='closest',
                      plot_bgcolor='rgb(248,248,248)'
                      )
    fig.show()


def make_random_tree(parameter_count, function_list, max_depth=4, function_node_p=0.5, parameter_node_p=0.6):
    if random() < function_node_p and max_depth > 0:
        f = choice(function_list)
        children = [make_random_tree(parameter_count, function_list, max_depth - 1, function_node_p, parameter_node_p)
                    for _ in range(f.child_count)]
        return FunctionNode(f, children)
    elif random() < parameter_node_p:
        number = randint(0, parameter_count - 1)
        return ParamNode(number, chr(number + 97))
    else:
        return ConstNode(randint(0, 10))
