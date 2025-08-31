#!/usr/bin/env python3
"""
Example usage of the Directed Graph Generator.

This file demonstrates how to use the DirectedGraph class to create, visualize,
and analyze directed graphs for discrete mathematics and graph theory applications.
"""

from directed_graph_generator import DirectedGraph

def basic_graph_example():
    """
    Demonstrates basic graph creation and visualization.
    """
    print("=== Basic Graph Example ===")
    
    # Create a simple directed graph
    nodes = [1, 2, 3, 4]
    connections = [(1, 2), (2, 3), (3, 4), (4, 1)]
    
    graph = DirectedGraph(nodes, connections)
    
    print(f"Graph created with {len(graph.nodes())} nodes and {len(graph.connections())} connections")
    print(f"Graph degree: {graph.degree()}")
    
    # Generate and display the graph
    graph.generate_graph()

def connectivity_analysis_example():
    """
    Demonstrates connectivity analysis features.
    """
    print("\n=== Connectivity Analysis Example ===")
    
    # Create a strongly connected graph
    nodes = [1, 2, 3, 4]
    connections = [(1, 2), (2, 3), (3, 4), (4, 1), (2, 4), (4, 2)]
    
    graph = DirectedGraph(nodes, connections)
    
    print("Connectivity Analysis:")
    print(f"  Is connected: {graph.isConnected()}")
    print(f"  Connectivity type: {graph.connectivenessType()}")
    print(f"  Is strongly connected: {graph.isStronlyConnected()}")
    print(f"  Is weakly connected: {graph.isWeaklyConnected()}")
    
    # Generate the graph
    graph.generate_graph()

def eulerian_properties_example():
    """
    Demonstrates Eulerian circuit and trail analysis.
    """
    print("\n=== Eulerian Properties Example ===")
    
    # Create a graph that is an Eulerian circuit
    nodes = [1, 2, 3, 4]
    connections = [(1, 2), (2, 3), (3, 4), (4, 1)]
    
    graph = DirectedGraph(nodes, connections)
    
    print("Eulerian Properties Analysis:")
    print(f"  Is Eulerian circuit: {graph.isEuclideanCircuit()}")
    print(f"  Is Eulerian trail: {graph.isEuclideanTrail()}")
    
    # Generate the graph
    graph.generate_graph()

def graph_modification_example():
    """
    Demonstrates adding and removing nodes and connections.
    """
    print("\n=== Graph Modification Example ===")
    
    # Start with a simple graph
    nodes = [1, 2, 3]
    connections = [(1, 2), (2, 3)]
    
    graph = DirectedGraph(nodes, connections)
    print(f"Initial graph: {len(graph.nodes())} nodes, {len(graph.connections())} connections")
    
    # Add a new node
    success = graph.add_node(4)
    print(f"Added node 4: {success}")
    
    # Add new connections
    success = graph.add_connection(3, 4)
    print(f"Added connection (3, 4): {success}")
    
    success = graph.add_connection(4, 1)
    print(f"Added connection (4, 1): {success}")
    
    print(f"After modifications: {len(graph.nodes())} nodes, {len(graph.connections())} connections")
    
    # Generate the modified graph
    graph.generate_graph()
    
    # Remove a connection
    success = graph.remove_connection(2, 3)
    print(f"Removed connection (2, 3): {success}")
    
    # Remove a node
    success = graph.remove_node(2)
    print(f"Removed node 2: {success}")
    
    print(f"Final graph: {len(graph.nodes())} nodes, {len(graph.connections())} connections")

def complex_graph_example():
    """
    Demonstrates a more complex graph with multiple analysis features.
    """
    print("\n=== Complex Graph Example ===")
    
    # Create a complex directed graph
    nodes = [1, 2, 3, 4, 5, 6]
    connections = [
        (1, 2), (2, 3), (3, 4), (4, 5), (5, 6),
        (6, 1), (2, 4), (4, 6), (1, 3), (3, 5)
    ]
    
    graph = DirectedGraph(nodes, connections)
    
    print("Complex Graph Analysis:")
    print(f"  Number of nodes: {len(graph.nodes())}")
    print(f"  Number of connections: {len(graph.connections())}")
    print(f"  Graph degree: {graph.degree()}")
    print(f"  Is connected: {graph.isConnected()}")
    print(f"  Connectivity type: {graph.connectivenessType()}")
    print(f"  Is strongly connected: {graph.isStronlyConnected()}")
    print(f"  Is weakly connected: {graph.isWeaklyConnected()}")
    print(f"  Is Eulerian circuit: {graph.isEuclideanCircuit()}")
    print(f"  Is Eulerian trail: {graph.isEuclideanTrail()}")
    
    # Generate the complex graph
    graph.generate_graph()

def main():
    """
    Main function to run all examples.
    """
    print("Directed Graph Generator - Example Usage")
    print("=" * 50)
    
    try:
        # Run all examples
        basic_graph_example()
        connectivity_analysis_example()
        eulerian_properties_example()
        graph_modification_example()
        complex_graph_example()
        
        print("\n" + "=" * 50)
        print("All examples completed successfully!")
        
    except Exception as e:
        print(f"Error running examples: {e}")

if __name__ == "__main__":
    main()
