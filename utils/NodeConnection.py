from Node import Node
class NodeConnection:
    def __init__(self, Node start_node, Node end_node):
        self.start_node = start_node
        self.end_node = end_node

    def change_start_node(Node new_start_node):
        self.start_node = new_start_node
    
    def change_end_node(Node new_end_node):
        self.end_node = new_end_node
    