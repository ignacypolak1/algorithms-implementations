from __future__ import annotations
from os import get_terminal_size

class Node:
    """
    A class for representing graph node

    Nodes are fundamental parts of a graph structure (e.g., in graph theory or network routing).
    Each node has a name, can have multiple neighbours with associated costs, and can be designated as a root node.
    
    :ivar name: Unique name of the node
    :type name: str

    :ivar isRoot: True if the node has no parent, False otherwise. Automatically determined.
    :type isRoot: bool

    :ivar neighbours: List of tuples containing neighbours and the cost to reach them.
    :type neighbours: list(Node)
    
    :ivar level: The level or depth of the node in the graph. Root nodes are at level 0.
    :type level: int

    :param name: Name of the node
    :type name: str

    :param neighbour: Neighbour/Parent of the node
    :type neighbour: Node

    :param cost: Cost of path between the node and given neighbour node
    :type cost: int

    :return: 
    :rtype: None
    """
    name: str
    isRoot: bool
    neighbours: list(('Node', int))
    level: int

    def __init__(self, name: str, neighbour: Node | None = None, cost: int | None = None) -> None: 
        self.name = name
        self.neighbours = []

        if neighbour is not None and cost is not None:
            self.isRoot = False
            self.neighbours.append((neighbour, cost))
            neighbour.neighbours.append((self, cost))
            self.level = neighbour.level + 1
        else:
            self.isRoot = True
            self.level = 0

    def __repr__(self):
        return f"Node({self.name})"

    def __str__(self):
        return f"Node:{self.name}"

    def __eq__(self, node: 'Node'):
        return self.name == node.name and self.parent == node.parent

class Graph:
    """Graph class for storing object of class :class:`structures.graph.Node`.
    
    :ivar nodes: Dictionary for storing existing nodes inside.
    :type nodes: dict[str, Node]

    :param: No parameters
    """
    nodes: dict(Node)

    def __init__(self):
        """Constructor method     
        """
        self.nodes = dict()

    def create_node(self, name: str, neighbour: str | None = None, cost: int | None = None) -> None:
        """Create node and put it in graph

        :param name: Name of the node
        :type name: str

        :param neighbour: Neighbour/Parent of the node
        :type neighbour: Node

        :param cost: Cost of path between the node and given neighbour node
        :type cost: int

        :return: None
        :rtype: None
        """
        if len(self.nodes) == 0:
            neighbour = None
            node = Node(name)
        else:
            if neighbour is None:
                print("You need to specify neighbour!")
                return
            else:
                neighbour = self.nodes[neighbour]
                node = Node(name, neighbour, cost)
        self.nodes[name] = node

    def print_nodes(self) -> None:
        """Method for printing nodes
           
           * TODO
           * Should use self.print_batch method for printing nodes with specific level
        """
        pass
        

    def print_batch(self, min: int, max: int, nodes: list(Node)) -> None:
        """Method for printing single batch of nodes ie. all nodes with given level

        :param min: Minimal cursor column position
        :type min: int

        :param max: Maximal cursor column position
        :type max: int

        :param nodes: List of nodes to print in single line
        :type nodes: list(Node)

        :return: None
        :rtype: None
        """
        fragment_length = max - min
        single_separator = '*' * int((fragment_length - len(nodes)) / ( len(nodes) + 1 ))
        print("*"*min, end="", sep="")
        padding = fragment_length - len(nodes) - ((len(nodes)+1) * len(single_separator))
        print("*"*padding, sep="", end="")
        print(single_separator, end="", sep="")
        for node in nodes:
            print("#", single_separator, end="", sep="")
