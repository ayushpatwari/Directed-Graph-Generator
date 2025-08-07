class Node:
    """
    This is a class for a node in a graph
    """
    def __init__(self, value):
        self.value = value
    
    
    def change_value(self, new_value):
        """
        Changes value of node
            
        Args:
            new_value(value): new value to insert into node
        
        Returns:
            bool: operation success
        """
        self.value = new_value
        return True
    
    def remove_value(self):
        """
        Removes value from node
        
        Returns:
            bool: operation success
        """
        self.value = None
        
    def __str__(self):
        """
        Expresses node through its value
        
        Returns:
            string: value of node as string
        """
        return str(self.value)