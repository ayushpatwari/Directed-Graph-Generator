class Node:
    """
    This is a class for a node in a graph
    """
    def __init__(self, value):
        self.value = value
        self.connection_count = 0
    
    
    def change_value(self, new_value) -> bool:
        """
        Changes value of node
            
        Args:
            new_value(value): new value to insert into node
        
        Returns:
            bool: whether the replacement of value was successful
        """
        self.value = new_value
        return True
    
    def remove_value(self) -> bool:
        """
        Removes value from node
        
        Returns:
            bool: whether removing the value was successful
        """
        self.value = None
    
    def add_connection_count(self) -> bool:
        self.connection_count += 1
        return True

    def __str__(self) -> str:
        """
        Expresses node through its value
        
        Returns:
            string: value of node
        """
        return str(self.value)