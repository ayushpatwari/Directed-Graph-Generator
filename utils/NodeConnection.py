from Node import Node

class NodeConnection:
    """"
    This is a class for a connection between nodes in a graph
    """
    def __init__(self, start_node: Node, end_node: Node):
        self.start_node = start_node
        self.end_node = end_node

    def change_start_node(self, new_start_node: Node) -> bool:
        """
        Changes start node of the connection
        
        Args:
            new_start_node(Node): new start node
        
        Returns:
            bool: whether the replacement of start node was successful
        """
        self.start_node = new_start_node
        return True
    
    def change_end_node(self, new_end_node: Node) -> bool:
        """"
        Changes end node of the connection
        
        Args:
            new_end_node(Node): new end node
        
        Returns:
            bool: whether the replacement of end node was successful
        """
        self.end_node = new_end_node
        return True

    def __str__(self) -> str:
        """
        Expresses node connection through its node start value and node end value
        
        Returns:
            string: value of node connection
        """
        return f"Start node: {str(self.start_node)} - End Node: {str(self.end_node)}"