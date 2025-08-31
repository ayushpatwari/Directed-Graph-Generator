from typing import List
import networkx as nx
import matplotlib.pyplot as plt
from utils.Node import Node
from utils.NodeConnection import NodeConnection

class DirectedGraph:
    """
    Represents a directed graph for discrete mathematics and graph theory analysis.

    A directed graph consists of nodes (vertices) connected by directed edges (arcs).
    This class provides functionality to create, visualize, and analyze directed graphs,
    including connectivity analysis, Eulerian properties, and graph manipulation.

    Attributes:
        nodes (List[Node]): List of Node objects representing the graph vertices.
        connections (List[NodeConnection]): List of NodeConnection objects representing directed edges.
        graph (nx.DiGraph): NetworkX directed graph object for visualization and analysis.

    Args:
        nodes (List[int]): List of integer values representing node identifiers.
        connections (List[tuple[int, int]]): List of tuples representing directed edges (start_node, end_node).

    Methods:
        generate_graph(): Creates and displays a visual representation of the graph.
        degree(): Returns the total degree (sum of all connections) of the graph.
        isConnected(): Checks if the graph is connected in any way.
        connectivenessType(): Returns the type of connectivity ("strong", "weak", or "None").
        isStronlyConnected(): Checks if the graph is strongly connected.
        isWeaklyConnected(): Checks if the graph is weakly connected.
        isEuclideanCircuit(): Checks if the graph is an Eulerian circuit.
        isEuclideanTrail(): Checks if the graph is an Eulerian trail.
        add_node(value): Adds a new node to the graph.
        add_connection(start_node_value, end_node_value): Adds a new directed connection.
        remove_node(value): Removes a node and all its associated connections.
        remove_connection(start_node_value, end_node_value): Removes a specific connection.
        nodes(): Returns the list of nodes in the graph.
        connections(): Returns the list of connections in the graph.
    """
    def __init__(self, nodes: List[int], connections: List[tuple[int, int]]):
        """
        Initializes a DirectedGraph object.

        Args:
            nodes (List[int]): List of integer values representing node identifiers.
            connections (List[tuple[int, int]]): List of tuples representing directed edges (start_node, end_node).
        """
        self.nodes = self.__fromValueListToNodeList(nodes)
        self.connections = self.__fromValueListToNodeConnectionList(connections)
        self.graph = nx.DiGraph()
    
    def generate_graph(self):
        """
        Generates and displays a visual representation of the directed graph.

        Creates a matplotlib figure showing the graph with nodes arranged in a circular layout.
        Nodes are displayed as white circles with black borders, and directed edges are shown
        as black arrows with curved connections to avoid overlap.

        The graph is displayed with:
        - Nodes: White circles with black borders and bold labels
        - Edges: Black arrows with curved connections
        - Title: "Discrete Mathematics: Directed Graph"
        - Layout: Circular arrangement for optimal visualization
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
        Returns the total degree of the graph.

        The degree of a graph is the sum of all connections (edges) in the graph.
        For a directed graph, this includes both incoming and outgoing connections.

        Returns:
            int: The total degree of the graph (sum of all connections).
        """
        degree: int = 0

        for node in self.nodes:
            degree += node.connection_count
        
        return degree

    def isConnected(self) -> bool:
        """
        Returns whether the graph is connected in any way.

        A graph is considered connected if there exists a path between any two nodes,
        either in the original direction or in the reverse direction.

        Returns:
            bool: True if the graph is connected (strongly or weakly), False otherwise.
        """
        return self.__isNormalConnected() or self.__isTransposeConnected()
    
    def connectivenessType(self) -> str:
        """
        Returns the type of connectivity of the graph.

        Determines whether the graph is strongly connected, weakly connected, or not connected.
        - Strongly connected: Every node can reach every other node following directed edges.
        - Weakly connected: The underlying undirected graph is connected.
        - Not connected: The graph has disconnected components.

        Returns:
            str: The connectivity type ("strong", "weak", or "None").
        """
        if (self.isStronlyConnected()):
            return "strong"
        elif (self.isWeaklyConnected()):
            return "weak"
        
        return "None"

    def isStronlyConnected(self) -> bool:
        """
        Returns whether the graph is strongly connected.

        A graph is strongly connected if for every pair of nodes (u, v), there exists
        a directed path from u to v and from v to u.

        Returns:
            bool: True if the graph is strongly connected, False otherwise.
        """
        return self.__isNormalConnected() and self.__isTransposeConnected()
    
    def isWeaklyConnected(self) -> bool:
        """
        Returns whether the graph is weakly connected.

        A graph is weakly connected if the underlying undirected graph (ignoring edge directions)
        is connected.

        Returns:
            bool: True if the graph is weakly connected, False otherwise.
        """
        return self.__isNormalConnected() and (not self.__isTransposeConnected())

    def isEuclideanCircuit(self) -> bool:
        """
        Returns whether the graph is an Eulerian circuit.

        An Eulerian circuit is a circuit that visits every edge exactly once and
        returns to the starting node. For a directed graph to be an Eulerian circuit:
        1. The graph must be strongly connected.
        2. Every node must have equal in-degree and out-degree.

        Returns:
            bool: True if the graph is an Eulerian circuit, False otherwise.
        """
        for node in self.nodes:
            if node.degree % 2 != 0:
                return False
        
        return self.isStronlyConnected()
    
    def isEuclideanTrail(self) -> bool:
        """
        Returns whether the graph is an Eulerian trail.

        An Eulerian trail is a trail that visits every edge exactly once.
        For a directed graph to be an Eulerian trail:
        1. The graph must be strongly connected.
        2. At most two nodes can have odd degree (in-degree ≠ out-degree).

        Returns:
            bool: True if the graph is an Eulerian trail, False otherwise.
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
        Returns whether the normal graph is connected.

        Performs a depth-first search starting from the first node to determine
        if all nodes can be reached following the directed edges.

        Returns:
            bool: True if all nodes are reachable from the first node, False otherwise.
        """
        visited = set()
        self.__DFS(self.nodes[0], visited, self.connections)

        return len(visited) == len(self.nodes)

    def __isTransposeConnected(self) -> bool:
        """
        Returns whether the transpose graph is connected.
        
        Creates a transpose of the graph (reverses all edge directions) and performs
        a depth-first search to determine connectivity in the reverse direction.

        Returns:
            bool: True if all nodes are reachable in the transposed graph, False otherwise.
        """
        visited = set()
        reverse_connections: List[NodeConnection] = self.__transpose_graph()
        self.__DFS(self.nodes[0], visited, reverse_connections)
        
        return len(visited) == len(self.nodes)
    
    def __DFS(self, node: Node, visited: set, connections: List[NodeConnection]):
        """
        Performs depth-first search to explore the graph connectivity.
        
        Recursively visits all nodes reachable from the starting node by following
        the directed connections.

        Args:
            node (Node): The current node being visited.
            visited (set): Set of nodes that have been visited.
            connections (List[NodeConnection]): List of all connections in the graph.
        """
        visited.add(node)
        for connection in connections:
            if (connection.start_node == node):
                if (connection.end_node not in visited):
                    self.__DFS(connection.end_node, visited, connections)

    def __transpose_graph(self) -> List[NodeConnection]:
        """
        Creates a transpose of the graph by reversing all edge directions.

        The transpose of a directed graph is obtained by reversing the direction
        of all edges while keeping the same nodes.

        Returns:
            List[NodeConnection]: List of connections with reversed directions.
        """
        new_connections: List[NodeConnection] = []

        for connection in self.connections:
            new_connections.append(NodeConnection(connection.end_node, connection.start_node))
        
        return new_connections
        
    def __addAllEdges(self) -> bool:
        """
        Adds all connections as edges to the NetworkX graph object.

        Converts internal NodeConnection objects to NetworkX edges for visualization
        and analysis purposes.

        Returns:
            bool: True if all edges were successfully added, False otherwise.
        """
        for connection in self.connections:
            self.graph.add_edge(connection.start_node, connection.end_node)

        return True

    def nodes(self) -> List[Node]:
        """
        Returns the list of nodes in the graph.
        
        Returns:
            List[Node]: List of all Node objects in the graph.
        """
        return self.nodes
    
    def connections(self) -> List[NodeConnection]:
        """
        Returns the list of connections in the graph.
        
        Returns:
            List[NodeConnection]: List of all NodeConnection objects in the graph.
        """
        return self.connections
    
    def __add_node(self, node: Node) -> bool:
        """
        Private method that adds a node to the internal nodes list.

        Args:
            node (Node): The Node object to be added to the graph.
        
        Returns:
            bool: True if the node was successfully added, False otherwise.
        """
        self.nodes.append(node)

        return True
        
    def add_node(self, value: int) -> bool:
        """
        Adds a new node to the graph.

        Checks for duplicate values before adding the node to ensure
        each node value is unique in the graph.

        Args:
            value (int): The integer value representing the new node.

        Returns:
            bool: True if the node was successfully added, False if the value already exists.
        """
        if value not in [node.value for node in self.nodes]:  
            return self.__add_node(Node(value))

        return False
    
    def __add_connection(self, start_node: Node, end_node: Node) -> bool:
        """
        Private method that adds a connection between two nodes.

        Checks for duplicate connections and updates the connection counts
        for both nodes.

        Args:
            start_node (Node): The starting node of the connection.
            end_node (Node): The ending node of the connection.
        
        Returns:
            bool: True if the connection was successfully added, False if it already exists.
        """
        if not any(connection.start_node == start_node and connection.end_node == end_node for connection in self.connections):
            self.connections.append(NodeConnection(start_node, end_node))
            start_node.add_connection_count()
            end_node.add_connection_count()
            return True

        return False
    
    def add_connection(self, start_node_value: int, end_node_value: int) -> bool:
        """
        Adds a new directed connection between two nodes.

        Finds the Node objects corresponding to the given values and creates
        a connection between them. Checks for duplicate connections.

        Args:
            start_node_value (int): The value of the starting node.
            end_node_value (int): The value of the ending node.

        Returns:
            bool: True if the connection was successfully added, False if it already exists.

        Raises:
            StopIteration: If either node value is not found in the graph.
        """
        start_node = next(node for node in self.nodes if node.value == start_node_value)
        end_node = next(node for node in self.nodes if node.value == end_node_value)

        return self.__add_connection(start_node, end_node)

    def __remove_node(self, node: Node) -> bool:
        """
        Private method that removes a node and all its associated connections.

        Removes the node from the nodes list and all connections that involve
        this node (either as start or end node).

        Args:
            node (Node): The Node object to be removed from the graph.
        
        Returns:
            bool: True if the node was successfully removed, False if no connections were found.
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
        Removes a node from the graph by its value.

        Finds the node with the specified value and removes it along with
        all its associated connections.

        Args:
            value (int): The value of the node to be removed.
        
        Returns:
            bool: True if the node was successfully removed, False if the value was not found.
        """
        for node in self.nodes:
            if node.value == value:
                self.__remove_node(node)
                return True
        
        return False
    
    def __remove_connection(self, node_connection: NodeConnection) -> bool:
        """
        Private method that removes a connection from the connections list.

        Args:
            node_connection (NodeConnection): The connection object to be removed.
        
        Returns:
            bool: True if the connection was successfully removed, False otherwise.
        """
        self.connections.remove(node_connection)
        return True

    def remove_connection(self, start_node_value: int, end_node_value: int) -> bool:
        """
        Removes a specific connection from the graph.

        Finds and removes the connection between the specified start and end nodes.
        Checks for the existence of the connection before attempting removal.

        Args:
            start_node_value (int): The value of the starting node of the connection.
            end_node_value (int): The value of the ending node of the connection.
        
        Returns:
            bool: True if the connection was successfully removed, False if it was not found.
        """
        for connection in self.connections:
            if connection.start_node.value == start_node_value and connection.end_node.value == end_node_value:
                self.__remove_connection(connection)
                return True
            
        return False

    def __fromNodeListToValueList(self) -> List[int]:
        """
        Converts the list of Node objects to a list of integer values.

        Extracts the value attribute from each Node object in the nodes list.

        Returns:
            List[int]: List of integer values representing the nodes.
        """
        array: List[int] = list()
        
        for node in self.nodes:
            array.append(node.value)
            
        return array
            
    def __fromValueListToNodeListOfTuple(self, array: List[tuple[int, int]]) -> List[tuple[Node, Node]]:
        """
        Converts a list of value tuples to a list of Node tuples.

        Finds the corresponding Node objects for each start and end value
        in the input array and creates tuples of Node objects.

        Args:
            array (List[tuple[int, int]]): List of tuples containing (start_value, end_value) pairs.

        Returns:
            List[tuple[Node, Node]]: List of tuples containing (start_node, end_node) pairs.

        Raises:
            StopIteration: If any node value is not found in the graph.
        """
        node_list: List[tuple[Node, Node]] = []
        
        for start_val, end_val in array:
            start_node = next(node for node in self.nodes if node.value == start_val)
            end_node = next(node for node in self.nodes if node.value == end_val)
            node_list.append((start_node, end_node))
        
        return node_list

    def __fromValueListToNodeConnectionList(self, array: List[tuple[int, int]]) -> List[NodeConnection]:
        """
        Converts a list of value tuples to a list of NodeConnection objects.

        Creates NodeConnection objects from the input array of (start_value, end_value) tuples.
        Updates the connection count for each node involved in the connections.

        Args:
            array (List[tuple[int, int]]): List of tuples containing (start_value, end_value) pairs.

        Returns:
            List[NodeConnection]: List of NodeConnection objects representing the graph edges.
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
        Converts a list of integer values to a list of Node objects.

        Creates Node objects from the input array of integer values.

        Args:
            array: List of integer values representing node identifiers.

        Returns:
            List[Node]: List of Node objects created from the input values.
        """
        node_list: List[Node] = list()
        
        for value in array:
            node_list.append(Node(value))

        return node_list
