# Directed Graph Generator API Documentation

## Overview

The Directed Graph Generator provides a comprehensive set of tools for creating, visualizing, and analyzing directed graphs. This document provides detailed information about the API, including all classes, methods, and their usage.

## Table of Contents

1. [DirectedGraph Class](#directedgraph-class)
2. [Node Class](#node-class)
3. [NodeConnection Class](#nodeconnection-class)
4. [Usage Examples](#usage-examples)
5. [Error Handling](#error-handling)

## DirectedGraph Class

The main class for creating and manipulating directed graphs.

### Constructor

```python
DirectedGraph(nodes: List[int], connections: List[tuple[int, int]])
```

**Parameters:**
- `nodes` (List[int]): List of integer values representing node identifiers
- `connections` (List[tuple[int, int]]): List of tuples representing directed edges (start_node, end_node)

**Example:**
```python
nodes = [1, 2, 3, 4]
connections = [(1, 2), (2, 3), (3, 4), (4, 1)]
graph = DirectedGraph(nodes, connections)
```

### Methods

#### Visualization Methods

##### `generate_graph()`
Creates and displays a visual representation of the directed graph.

**Returns:** None

**Description:**
- Creates a matplotlib figure showing the graph with nodes arranged in a circular layout
- Nodes are displayed as white circles with black borders and bold labels
- Directed edges are shown as black arrows with curved connections
- The graph is displayed with the title "Discrete Mathematics: Directed Graph"

**Example:**
```python
graph.generate_graph()
```

#### Analysis Methods

##### `degree() -> int`
Returns the total degree of the graph.

**Returns:** int - The total degree of the graph (sum of all connections)

**Description:**
The degree of a graph is the sum of all connections (edges) in the graph. For a directed graph, this includes both incoming and outgoing connections.

**Example:**
```python
total_degree = graph.degree()
print(f"Graph degree: {total_degree}")
```

##### `isConnected() -> bool`
Returns whether the graph is connected in any way.

**Returns:** bool - True if the graph is connected (strongly or weakly), False otherwise

**Description:**
A graph is considered connected if there exists a path between any two nodes, either in the original direction or in the reverse direction.

**Example:**
```python
if graph.isConnected():
    print("The graph is connected")
else:
    print("The graph is not connected")
```

##### `connectivenessType() -> str`
Returns the type of connectivity of the graph.

**Returns:** str - The connectivity type ("strong", "weak", or "None")

**Description:**
Determines whether the graph is strongly connected, weakly connected, or not connected:
- **Strongly connected**: Every node can reach every other node following directed edges
- **Weakly connected**: The underlying undirected graph is connected
- **Not connected**: The graph has disconnected components

**Example:**
```python
connectivity = graph.connectivenessType()
print(f"Connectivity type: {connectivity}")
```

##### `isStronlyConnected() -> bool`
Returns whether the graph is strongly connected.

**Returns:** bool - True if the graph is strongly connected, False otherwise

**Description:**
A graph is strongly connected if for every pair of nodes (u, v), there exists a directed path from u to v and from v to u.

**Example:**
```python
if graph.isStronlyConnected():
    print("The graph is strongly connected")
```

##### `isWeaklyConnected() -> bool`
Returns whether the graph is weakly connected.

**Returns:** bool - True if the graph is weakly connected, False otherwise

**Description:**
A graph is weakly connected if the underlying undirected graph (ignoring edge directions) is connected.

**Example:**
```python
if graph.isWeaklyConnected():
    print("The graph is weakly connected")
```

##### `isEuclideanCircuit() -> bool`
Returns whether the graph is an Eulerian circuit.

**Returns:** bool - True if the graph is an Eulerian circuit, False otherwise

**Description:**
An Eulerian circuit is a circuit that visits every edge exactly once and returns to the starting node. For a directed graph to be an Eulerian circuit:
1. The graph must be strongly connected
2. Every node must have equal in-degree and out-degree

**Example:**
```python
if graph.isEuclideanCircuit():
    print("The graph is an Eulerian circuit")
```

##### `isEuclideanTrail() -> bool`
Returns whether the graph is an Eulerian trail.

**Returns:** bool - True if the graph is an Eulerian trail, False otherwise

**Description:**
An Eulerian trail is a trail that visits every edge exactly once. For a directed graph to be an Eulerian trail:
1. The graph must be strongly connected
2. At most two nodes can have odd degree (in-degree ≠ out-degree)

**Example:**
```python
if graph.isEuclideanTrail():
    print("The graph is an Eulerian trail")
```

#### Graph Modification Methods

##### `add_node(value: int) -> bool`
Adds a new node to the graph.

**Parameters:**
- `value` (int): The integer value representing the new node

**Returns:** bool - True if the node was successfully added, False if the value already exists

**Description:**
Checks for duplicate values before adding the node to ensure each node value is unique in the graph.

**Example:**
```python
success = graph.add_node(5)
if success:
    print("Node 5 added successfully")
else:
    print("Node 5 already exists")
```

##### `add_connection(start_node_value: int, end_node_value: int) -> bool`
Adds a new directed connection between two nodes.

**Parameters:**
- `start_node_value` (int): The value of the starting node
- `end_node_value` (int): The value of the ending node

**Returns:** bool - True if the connection was successfully added, False if it already exists

**Raises:** StopIteration - If either node value is not found in the graph

**Description:**
Finds the Node objects corresponding to the given values and creates a connection between them. Checks for duplicate connections.

**Example:**
```python
try:
    success = graph.add_connection(1, 5)
    if success:
        print("Connection (1, 5) added successfully")
    else:
        print("Connection (1, 5) already exists")
except StopIteration:
    print("One or both nodes not found in the graph")
```

##### `remove_node(value: int) -> bool`
Removes a node from the graph by its value.

**Parameters:**
- `value` (int): The value of the node to be removed

**Returns:** bool - True if the node was successfully removed, False if the value was not found

**Description:**
Finds the node with the specified value and removes it along with all its associated connections.

**Example:**
```python
success = graph.remove_node(3)
if success:
    print("Node 3 removed successfully")
else:
    print("Node 3 not found in the graph")
```

##### `remove_connection(start_node_value: int, end_node_value: int) -> bool`
Removes a specific connection from the graph.

**Parameters:**
- `start_node_value` (int): The value of the starting node of the connection
- `end_node_value` (int): The value of the ending node of the connection

**Returns:** bool - True if the connection was successfully removed, False if it was not found

**Description:**
Finds and removes the connection between the specified start and end nodes. Checks for the existence of the connection before attempting removal.

**Example:**
```python
success = graph.remove_connection(1, 2)
if success:
    print("Connection (1, 2) removed successfully")
else:
    print("Connection (1, 2) not found in the graph")
```

#### Accessor Methods

##### `nodes() -> List[Node]`
Returns the list of nodes in the graph.

**Returns:** List[Node] - List of all Node objects in the graph

**Example:**
```python
node_list = graph.nodes()
print(f"Graph has {len(node_list)} nodes")
```

##### `connections() -> List[NodeConnection]`
Returns the list of connections in the graph.

**Returns:** List[NodeConnection] - List of all NodeConnection objects in the graph

**Example:**
```python
connection_list = graph.connections()
print(f"Graph has {len(connection_list)} connections")
```

## Node Class

Represents a node (vertex) in a directed graph.

### Constructor

```python
Node(value)
```

**Parameters:**
- `value`: The value to assign to this node

### Attributes

- `value`: The unique identifier or value of the node
- `connection_count` (int): The number of connections (edges) associated with this node

### Methods

#### `change_value(new_value) -> bool`
Changes the value of the node to a new value.

**Parameters:**
- `new_value`: The new value to assign to the node

**Returns:** bool - True if the value was successfully changed

#### `remove_value() -> bool`
Removes the value from the node by setting it to None.

**Returns:** bool - True if the value was successfully removed

#### `add_connection_count() -> bool`
Increments the connection count for this node.

**Returns:** bool - True if the connection count was successfully incremented

**Description:**
This method is called when a new connection is added that involves this node, either as a starting or ending point of an edge.

#### `__str__() -> str`
Returns a string representation of the node.

**Returns:** str - String representation of the node's value

## NodeConnection Class

Represents a directed connection (edge) between two nodes in a graph.

### Constructor

```python
NodeConnection(start_node: Node, end_node: Node)
```

**Parameters:**
- `start_node` (Node): The Node object representing the start of the connection
- `end_node` (Node): The Node object representing the end of the connection

### Attributes

- `start_node` (Node): The starting node of the directed connection
- `end_node` (Node): The ending node of the directed connection

### Methods

#### `change_start_node(new_start_node: Node) -> bool`
Changes the starting node of the connection.

**Parameters:**
- `new_start_node` (Node): The new Node object to be the start of the connection

**Returns:** bool - True if the starting node was successfully changed

#### `change_end_node(new_end_node: Node) -> bool`
Changes the ending node of the connection.

**Parameters:**
- `new_end_node` (Node): The new Node object to be the end of the connection

**Returns:** bool - True if the ending node was successfully changed

#### `__str__() -> str`
Returns a string representation of the node connection.

**Returns:** str - String representation showing the start and end nodes of the connection

## Usage Examples

### Basic Graph Creation and Analysis

```python
from directed_graph_generator import DirectedGraph

# Create a directed graph
nodes = [1, 2, 3, 4]
connections = [(1, 2), (2, 3), (3, 4), (4, 1)]

graph = DirectedGraph(nodes, connections)

# Analyze the graph
print(f"Graph degree: {graph.degree()}")
print(f"Is connected: {graph.isConnected()}")
print(f"Connectivity type: {graph.connectivenessType()}")

# Visualize the graph
graph.generate_graph()
```

### Graph Modification

```python
# Add a new node
graph.add_node(5)

# Add new connections
graph.add_connection(4, 5)
graph.add_connection(5, 1)

# Remove a connection
graph.remove_connection(2, 3)

# Remove a node
graph.remove_node(3)
```

### Eulerian Properties Analysis

```python
# Check for Eulerian properties
if graph.isEuclideanCircuit():
    print("The graph is an Eulerian circuit")
elif graph.isEuclideanTrail():
    print("The graph is an Eulerian trail")
else:
    print("The graph is neither an Eulerian circuit nor trail")
```

## Error Handling

The Directed Graph Generator includes several error handling mechanisms:

### Common Exceptions

1. **StopIteration**: Raised when trying to add a connection between nodes that don't exist in the graph
2. **ValueError**: May be raised for invalid input parameters
3. **IndexError**: May be raised when accessing nodes or connections that don't exist

### Best Practices

1. **Check for node existence** before adding connections
2. **Handle exceptions** when adding connections between non-existent nodes
3. **Validate input** before creating graphs
4. **Use try-catch blocks** for operations that may fail

### Example Error Handling

```python
try:
    graph.add_connection(1, 10)  # Node 10 doesn't exist
except StopIteration:
    print("Cannot add connection: one or both nodes don't exist")

try:
    graph.remove_node(100)  # Node 100 doesn't exist
except ValueError:
    print("Cannot remove node: node doesn't exist")
```
