class Node:
    def __init__(self, value):
        self.value = value
        
    def change_value(self, new_value):
        self.value = new_value
    
    def remove_value(self):
        self.value = None
    
    @staticmethod
    def create_node(value):
        return Node(value)    

    def __str__(self):
        return str(self.value)