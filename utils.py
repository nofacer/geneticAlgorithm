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
