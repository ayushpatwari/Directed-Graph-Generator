class Node:
    """
    Represents a node (vertex) in a directed graph.

    A node is a fundamental component of a graph that can be connected to other nodes
    through directed edges. Each node has a unique value and maintains a count of
    its connections for graph analysis purposes.

    Attributes:
        value: The unique identifier or value of the node.
        connection_count (int): The number of connections (edges) associated with this node.

    Args:
        value: The value to assign to this node.

    Methods:
        change_value(new_value): Changes the value of the node.
        remove_value(): Removes the value from the node (sets to None).
        add_connection_count(): Increments the connection count.
        __str__(): Returns a string representation of the node.
    """

    def __init__(self, value):
        """
        Initializes a Node object.

        Args:
            value: The value to assign to this node.
        """
        self.value = value
        self.connection_count = 0
    
    
    def change_value(self, new_value) -> bool:
        """
        Changes the value of the node to a new value.
            
        Args:
            new_value: The new value to assign to the node.
        
        Returns:
            bool: True if the value was successfully changed.
        """
        self.value = new_value
        return True
    
    def remove_value(self) -> bool:
        """
        Removes the value from the node by setting it to None.
        
        Returns:
            bool: True if the value was successfully removed.
        """
        self.value = None
    
    def add_connection_count(self) -> bool:
        """
        Increments the connection count for this node.

        This method is called when a new connection is added that involves this node,
        either as a starting or ending point of an edge.

        Returns:
            bool: True if the connection count was successfully incremented.
        """
        self.connection_count += 1
        return True

    def __str__(self) -> str:
        """
        Returns a string representation of the node.

        Returns:
            str: String representation of the node's value.
        """
        return str(self.value)