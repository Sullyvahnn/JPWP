from collections import defaultdict


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.children = []


def build_tree(edges, root_val):
    adj = defaultdict(list)
    for u, v in edges:
        adj[u].append(v)
        adj[v].append(u)

    def dfs(node_val, parent_val):
        node = TreeNode(node_val)
        for neighbor in adj[f'{node_val}']:
            if neighbor != f"{parent_val}":
                node.children.append(dfs(neighbor, node_val))
        return node

    return dfs(root_val, None)


