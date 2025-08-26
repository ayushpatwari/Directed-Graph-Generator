from typing import List
import networkx as nx
import matplotlib.pyplot as plt
from utils.Node import Node
from utils.NodeConnection import NodeConnection

class DirectedGraph:
    """
    This is a class for making a directed graph used in discrete mathematics
    """
    def __init__(self, nodes: List[int], connections: List[tuple[int, int]]):
        self.nodes = self.__fromValueListToNodeList(nodes)
        self.connections = self.__fromValueListToNodeConnectionList(connections)
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

    def degree(self) -> int:
        """
        Returns the degree of the graph
        
        Returns:
            int: degree of the graph
        """
        degree: int = 0

        for node in self.nodes:
            degree += node.connection_count
        
        return degree

    def isConnected(self) -> bool:
        """
        Returns whether the graph is connected at all
        
        Returns:
            bool: whether the graph is connected at all
        """
        return self.__isNormalConnected() or self.__isTransposeConnected()
    
    def connectivenessType(self) -> str:
        """
        Returns the type of the connectiveness of the graph
        
        Returns:
            str: the type of connectiveness
        """
        if (self.isStronlyConnected()):
            return "strong"
        elif (self.isWeaklyConnected()):
            return "weak"
        
        return "None"

    def isStronlyConnected(self) -> bool:
        """
        Returns whether the graph is strongly connected
        
        Returns:
            bool: whether the graph is strongly connected
        """
        return self.__isNormalConnected() and self.__isTransposeConnected()
    
    def isWeaklyConnected(self) -> bool:
        """
        Returns whether the graph is weakly connected
        
        Returns:
            bool: whether the graph is weakly connected
        """
        return self.__isNormalConnected() and (not self.__isTransposeConnected())

    def isEuclideanCircuit(self) -> bool:
        """
        Returns whether the graph is a euclidean circuit
        
        Returns:
            bool: whether the graph is an euclidean circuit
        """
        for node in self.nodes:
            if node.degree % 2 != 0:
                return False
        
        return self.isStronlyConnected()
    def isEuclideanTrail(self) -> bool:
        """
        Returns whether the graph is an euclidean trail
        
        Returns:
            bool: whether the graph is an euclidean trail
        """
        odd_degree_count: int = 0

        for node in self.nodes:
            if node.degree % 2 != 0:
                odd_degree_count += 1
                
                if odd_degree_count > 2:
                    return False

        return self.isStronlyConnected()
            

    def __isNormalConnected(self) -> bool:
        """
        Returns whether the normal graph is connected

        Returns:
            bool: whether the graph forward is connected
        """
        visited = set()
        self.__DFS(self.nodes[0], visited, self.connections)

        return len(visited) == len(self.nodes)

    def __isTransposeConnected(self) -> bool:
        """
        Returns whether the transpose graph is connected
        
        Returns:
            bool: whether the graph transposed is connected
        """
        visited = set()
        reverse_connections: List[NodeConnection] = self.__transpose_graph()
        self.__DFS(self.nodes[0], visited, reverse_connections)
        
        return len(visited) == len(self.nodes)
    
    def __DFS(self, node: Node, visited: set, connections: List[NodeConnection]):
        """
        Depth first searches the graph to find the connectiveness
        
        Args:
            node(Node): start node for current search iteration
            visited(set): current node visited list
            connections(List[NodeConnection]): connections of the graph
        """
        visited.add(node)
        for connection in connections:
            if (connection.start_node == node):
                if (connection.end_node not in visited):
                    self.__DFS(connection.end_node, visited, connections)

    def __transpose_graph(self) -> List[NodeConnection]:
        """
        Tranposes the graph by swapping all the connections

        Returns:
            List[NodeConnection]: new reversed node connections list
        """
        new_connections: List[NodeConnection] = []

        for connection in self.connections:
            new_connections.append(NodeConnection(connection.end_node, connection.start_node))
        
        return new_connections
        
    def __addAllEdges(self) -> bool:
        """
        Adds all the connections as edges in the graph

        Returns:
            bool: whether adding all the edges was successful
        """
        for connection in self.connections:
            self.graph.add_edge(connection.start_node, connection.end_node)

        return True

    def nodes(self) -> List[Node]:
        """
        Returns the nodes of the graphs
        
        Returns:
            List[Node]: list of nodes
        """
        return self.nodes
    
    def connections(self) -> List[NodeConnection]:
        """
        Returns the connections of the graphs
        
        Returns:
            List[NodeConnection]: list of connections
        """
        return self.connections
    
    def __add_node(self, node: Node) -> bool:
        """
        Private function that adds node into nodes list

        Args:
            node(Node): node to be inserted into the graph
        
        Returns:
            boolean: whether inserting the node into the node list was successful
        """
        self.nodes.append(node)

        return True
        
    def add_node(self, value: int) -> bool:
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
    
    def __add_connection(self, start_node: Node, end_node: Node) -> bool:
        """
        Private function that adds connection into the connections list

        Args:
            start_node(Node): Start node for the connection
            end_node(Node): End node for the connection
        
        Returns:
            bool: whether adding the connection to the connections list was successful
        """
        if not any(connection.start_node == start_node and connection.end_node == end_node for connection in self.connections):
            self.connections.append(NodeConnection(start_node, end_node))
            start_node.add_connection_count()
            end_node.add_connection_count()
            return True

        return False
    
    def add_connection(self, start_node_value: int, end_node_value: int) -> bool:
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

    def __remove_node(self, node: Node) -> bool:
        """
        Private function that removes node from the node list while also removing any connections associated with node
        Args:
            node(node): node to remove
        
        Returns:
            bool: whether removing the node from the node list was successful
        """
        self.nodes.remove(node)
        
        connections_to_remove = [connection for connection in self.connections if connection.start_node == node or connection.end_node == node]
        
        if len(connections_to_remove) == 0:
            return False

        for connection in connections_to_remove:
            self.__remove_connection(connection)
            
        return True
    
    def remove_node(self, value: int) -> bool:
        """
        Removes node from the graph using private function __remove_node while also checking its presense
        Args:
            value(int): value of the node to remove
        
        Returns:
            bool: whether removing the node from the graph was successful
        """
        for node in self.nodes:
            if node.value == value:
                self.__remove_node(node)
                return True
        
        return False
    
    def __remove_connection(self, node_connection: NodeConnection) -> bool:
        """
        Private function that removes the connection from the connections list
        Args:
            node_connection(NodeConnection): connection to remove
        
        Returns:
            bool: whether removing the connection from the connection list was successful
        """
        self.connections.remove(node_connection)
        return True

    def remove_connection(self, start_node_value: int, end_node_value: int) -> bool:
        """
        Removes connection from the graph using private function __remove_connection while checking for presense
        Args:
            start_node(int): value of the start node of the connection to remove
            end_node(int): value of the end node of the connection to remove
        
        Returns:
            bool: whether removing the connection from the graph list was successful
        """
        for connection in self.connections:
            if connection.start_node.value == start_node_value and connection.end_node.value == end_node_value:
                self.__remove_connection(connection)
                return True
            
        return False

    def __fromNodeListToValueList(self) -> List[int]:
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
        node_list: List[tuple[Node, Node]] = []
        
        for start_val, end_val in array:
            start_node = next(node for node in self.nodes if node.value == start_val)
            end_node = next(node for node in self.nodes if node.value == end_val)
            node_list.append((start_node, end_node))
        
        return node_list

    def __fromValueListToNodeConnectionList(self, array: List[tuple[int, int]]) -> List[NodeConnection]:
        """
        Converts value list to list of node connection
        """
        node_connection_list: List[NodeConnection] = []

        for start_val, end_val in array:
            start_node: Node = None
            end_node: Node = None
            for node in self.nodes:
                if node.value == start_val:
                    start_node = node
                    node.add_connection_count()
                if node.value == end_val:
                    end_node = node
                    node.add_connection_count()
            node_connection_list.append(NodeConnection(start_node, end_node))
        
        return node_connection_list
                    
            
    def __fromValueListToNodeList(self, array) -> List[Node]:
        """
        Converts value list to list of Nodes
        """
        node_list: List[Node] = list()
        
        for value in array:
            node_list.append(Node(value))

        return node_list
