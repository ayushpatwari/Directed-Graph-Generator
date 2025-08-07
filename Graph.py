from typing import List
import networkx as nx
import matplotlib.pyplot as plt
from Node import Node

class Graph:
    def __init__(self, nodes: List[int], connections: List[tuple[int, int]]):
        self.nodes = self.__fromArrayToNodeList(nodes)
        self.connections = self.__fromArrayToNodeListOfTuple(connections)
        self.graph = nx.DiGraph()
    
    def generate_graph(self):
        plt.close()
        
        self.graph.clear()
        
        self.graph.add_nodes_from(self.__fromNodeListToArray())         
        
        self.__addAllEdges()

        pos = nx.circular_layout(self.graph)

        plt.figure(figsize=(8, 8), dpi=120)
        plt.axis('off')

        node_size_val = 1200

        nx.draw_networkx_nodes(self.graph, pos, node_color='white', edgecolors='black', node_size=node_size_val, linewidths=2)
        
        nx.draw_networkx_edges(
            self.graph, pos, edge_color='black', arrows=True, arrowsize=28, width=2,
            connectionstyle='arc3,rad=0.18', arrowstyle='-|>', node_size=node_size_val 
        )

        nx.draw_networkx_labels(self.graph, pos, font_size=18, font_weight='bold', font_color='black')

        plt.title("Discrete Mathematics: Directed Graph", fontsize=20, fontweight='bold')
        plt.tight_layout()
        plt.show()
        
    def __fromNodeListToArray(self):
        array: List[int] = list()
        
        for node in self.nodes:
            array.append(node.value)
            
        print(array)
            
        return array
            
    def __fromArrayToNodeListOfTuple(self, array: List[tuple[int, int]]) -> List[tuple[Node, Node]]:
        node_list: list[tuple[Node, Node]] = []
        
        for start_val, end_val in array:
            start_node = next(node for node in self.nodes if node.value == start_val)
            end_node = next(node for node in self.nodes if node.value == end_val)
            node_list.append((start_node, end_node))
        
        return node_list
            
    def __fromArrayToNodeList(self, array):
        node_list: List[Node] = list()
        
        for value in array:
            node_list.append(Node.create_node(value))

        return node_list
    
    def __addAllEdges(self):
        for connection in self.connections:
            self.graph.add_edge(connection[0], connection[1])
    
    def __add_node(self, node: Node):
        self.nodes.append(node)
        
    def add_node(self, value: int):
        if value not in [node.value for node in self.nodes]:  
            self.__add_node(Node(value))
    
    def __add_connection(self, start_node: Node, end_node: Node):
        if (start_node, end_node) not in [(c[0].value, c[1].value) for c in self.connections]:
            self.connections.append((start_node, end_node))     
    
    def add_connection(self, start_node_value: int, end_node_value: int):
        start_node = next(node for node in self.nodes if node.value == start_node_value)
        end_node = next(node for node in self.nodes if node.value == end_node_value)
        self.__add_connection(start_node, end_node)
    #remove_node
    #remove_connection