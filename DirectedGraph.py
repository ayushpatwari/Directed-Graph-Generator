from typing import List
import networkx as nx
import matplotlib.pyplot as plt
from Node import Node

class DirectedGraph:
    """
    This is a class for making a directed graph used in discrete mathematics
    """
    def __init__(self, nodes: List[int], connections: List[tuple[int, int]]):
        self.nodes = self.__fromValueListToNodeList(nodes)
        self.connections = self.__fromValueListToNodeListOfTuple(connections)
        self.graph = nx.DiGraph()
    
    def generate_graph(self):
        """
        Generates a directed graph created from nodes and connections
        """

        plt.close()
        
        self.graph.clear()
        
        self.graph.add_nodes_from(self.nodes)         
        
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
        
    def __fromNodeListToValueList(self):
        """
        Converts the nodes list to an list
        """
        array: List[int] = list()
        
        for node in self.nodes:
            array.append(node.value)
            
        return array
            
    def __fromValueListToNodeListOfTuple(self, array: List[tuple[int, int]]) -> List[tuple[Node, Node]]:
        """
        Converts value list to list of tuple of nodes
        """
        node_list: list[tuple[Node, Node]] = []
        
        for start_val, end_val in array:
            start_node = next(node for node in self.nodes if node.value == start_val)
            end_node = next(node for node in self.nodes if node.value == end_val)
            node_list.append((start_node, end_node))
        
        return node_list
            
    def __fromValueListToNodeList(self, array):
        """
        Converts value list to list of Nodes
        """
        node_list: List[Node] = list()
        
        for value in array:
            node_list.append(Node(value))

        return node_list
    
    def __addAllEdges(self):
        """
        Adds all the connections as edges in the graph
        """
        for connection in self.connections:
            self.graph.add_edge(connection[0], connection[1])

        return True
    
    def __add_node(self, node: Node):
        """
        Private function that adds node into nodes list

        Args:
            node(Node): node to be inserted into the graph
        
        Returns:
            boolean: whether inserting the node into the node list was successful
        """
        self.nodes.append(node)

        return True
        
    def add_node(self, value: int):
        """
        Adds node into node list using private function __add_node while also checking for duplicates

        Args:
            value(int): integer to add into graph

        Returns:
            bool: whether adding the node to the graph was successful
        """
        if value not in [node.value for node in self.nodes]:  
            return self.__add_node(Node(value))

        return False
    
    def __add_connection(self, start_node: Node, end_node: Node):
        """
        Private function that adds connection into the connections list

        Args:
            start_node(Node): Start node for the connection
            end_node(Node): End node for the connection
        
        Returns:
            bool: whether adding the connection to the connections list was successful
        """
        if (start_node, end_node) not in [(c[0].value, c[1].value) for c in self.connections]:
            self.connections.append((start_node, end_node))
            return True

        return False
    
    def add_connection(self, start_node_value: int, end_node_value: int):
        """
        Adds connection into connections list using private function __add_connection while also checking for duplicates

        Args:
            start_node_value(int): starting integer for connection
            end_node_value(int): ending integer for connection

        Returns:
            bool: whether adding the connection to the graph was successful
        """
        start_node = next(node for node in self.nodes if node.value == start_node_value)
        end_node = next(node for node in self.nodes if node.value == end_node_value)

        return self.__add_connection(start_node, end_node)
        
    #remove_node
    #remove_connection