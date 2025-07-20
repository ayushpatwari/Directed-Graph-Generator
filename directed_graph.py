import networkx as nx
import matplotlib.pyplot as plt

# Create a directed graph
G = nx.DiGraph()

# Define your nodes
nodes = []

# Add nodes to the graph
G.add_nodes_from(nodes)

# Add edges based on the modulo 5 condition
for index, node in enumerate(nodes):
    for j in range(len(nodes)):
        if (node - nodes[j]) % 5 == 0:
            G.add_edge(node, nodes[j])
            print(f"({node}, {nodes[j]}): 5 | {node} - {nodes[j]} = 5 | {node - nodes[j]} -> {node - nodes[j]} = 5 * k where k = {(node - nodes[j]) / 5} -> Relation")
        else:
            print(f"({node}, {nodes[j]}): 5 | {node} - {nodes[j]} -> 5 | {node - nodes[j]} = {node - nodes[j]} != 5 * k where k is not an integer -> No Relation")

# Use a circular layout for better spacing and less overlap
pos = nx.circular_layout(G)

plt.figure(figsize=(8, 8), dpi=120)
plt.axis('off')  # Hide axes for a cleaner look

# Define a node_size that will be used for both nodes and edges
node_size_val = 1200

# Draw nodes with a bold outline
nx.draw_networkx_nodes(G, pos, node_color='white', edgecolors='black', node_size=node_size_val, linewidths=2)

# Draw edges with strong arrows and slight curvature to avoid overlap,
# and also to prevent the arrow tips from going inside the nodes.
# Use 'arrowstyle' and 'node_size' to control arrow appearance and distance from nodes.
nx.draw_networkx_edges(
    G, pos, edge_color='black', arrows=True, arrowsize=28, width=2,
    connectionstyle='arc3,rad=0.18', arrowstyle='-|>', node_size=node_size_val 
)

# Draw node labels in bold
nx.draw_networkx_labels(G, pos, font_size=18, font_weight='bold', font_color='black')

# Removed the edge label drawing code, as requested (no more red arrows).

plt.title("Discrete Mathematics: Directed Graph", fontsize=20, fontweight='bold')
plt.tight_layout()
plt.show()

