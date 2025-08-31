from utils.Node import Node

class NodeConnection:
    """
    Represents a directed connection (edge) between two nodes in a graph.

    A NodeConnection represents a directed edge from a start node to an end node.
    This class is used to model the relationships between nodes in a directed graph
    and provides methods to modify the connection endpoints.

    Attributes:
        start_node (Node): The starting node of the directed connection.
        end_node (Node): The ending node of the directed connection.

    Args:
        start_node (Node): The Node object representing the start of the connection.
        end_node (Node): The Node object representing the end of the connection.

    Methods:
        change_start_node(new_start_node): Changes the starting node of the connection.
        change_end_node(new_end_node): Changes the ending node of the connection.
        __str__(): Returns a string representation of the connection.
    """

    def __init__(self, start_node: Node, end_node: Node):
        """
        Initializes a NodeConnection object.

        Args:
            start_node (Node): The Node object representing the start of the connection.
            end_node (Node): The Node object representing the end of the connection.
        """
        self.start_node = start_node
        self.end_node = end_node

    def change_start_node(self, new_start_node: Node) -> bool:
        """
        Changes the starting node of the connection.
        
        Args:
            new_start_node (Node): The new Node object to be the start of the connection.
        
        Returns:
            bool: True if the starting node was successfully changed.
        """
        self.start_node = new_start_node
        return True
    
    def change_end_node(self, new_end_node: Node) -> bool:
        """
        Changes the ending node of the connection.
        
        Args:
            new_end_node (Node): The new Node object to be the end of the connection.
        
        Returns:
            bool: True if the ending node was successfully changed.
        """
        self.end_node = new_end_node
        return True

    def __str__(self) -> str:
        """
        Returns a string representation of the node connection.

        Returns:
            str: String representation showing the start and end nodes of the connection.
        """
        return f"Start node: {str(self.start_node)} - End Node: {str(self.end_node)}"