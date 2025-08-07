from Graph import Graph

"""Replace with all node values""",
nodes = [
    1,
    2,
    3,
    4,
    6,
    7
]

"""Replace with (start_node, end_node)"""
connections = [
    (1, 3),
    (3, 4)
]

graph = Graph(nodes, connections)

graph.add_connection(1, 2)
graph.add_node(10)

graph.generate_graph()