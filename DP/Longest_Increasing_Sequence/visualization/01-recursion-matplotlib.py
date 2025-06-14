import matplotlib.pyplot as plt
import networkx as nx

def build_lis_graph(nums):
    G = nx.DiGraph()
    node_counter = [0]  # Unique node ID tracker

    def helper(curr_index, prev_index, parent_id=None):
        node_label = f"({curr_index},{prev_index})"
        node_id = node_counter[0]
        node_counter[0] += 1

        G.add_node(node_id, label=node_label)

        if parent_id is not None:
            G.add_edge(parent_id, node_id)

        if curr_index > len(nums) - 1:
            return

        # Exclude case
        helper(curr_index + 1, prev_index, node_id)

        # Include case
        if prev_index == -1 or nums[curr_index] > nums[prev_index]:
            helper(curr_index + 1, curr_index, node_id)

    helper(0, -1)
    return G


def draw_graph(G):
    pos = nx.spring_layout(G, seed=42)  # Layout algorithm
    labels = nx.get_node_attributes(G, 'label')

    plt.figure(figsize=(12, 8))
    nx.draw(G, pos, with_labels=True, labels=labels, node_color='skyblue',
            node_size=1500, font_size=15, font_weight='bold', arrows=True)
    plt.title("LIS Recursion Tree")
    plt.show()


# Run
nums = [1, 2, 3]
graph = build_lis_graph(nums)
draw_graph(graph)
