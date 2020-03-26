## Source.py

## Authors: Ross Adams, Longtin Hang, Riley Williams


import networkx as nx
import matplotlib.pyplot as plt
import bfs
import bfs_path
import prim

# main function
def main():
    
    # Create a graph
    G = nx.Graph()

    # Add nodes from a list
    G.add_nodes_from("ABCDE")

    # Add edges from a list
    G.add_edges_from([('A','B'),('A','C'),('B','C'),('B','D'),('B','E'),('C','B'),\
        ('C','D'),('C','E'),('D','B'),('D','C'),('D','E'),('E','B'),('E','C'),('E','D')])

    # Print number of nodes
    print(G.number_of_nodes())

    # Print number of edges
    print(G.number_of_edges())

    # List nodes in graph
    print(list(G.nodes))

    # List edges in graph
    print(list(G.edges))

    # Draw graph
    plt.subplot(121)
    nx.draw(G, with_labels=True, font_weight='bold')
    plt.show()


if __name__ == "__main__":
    main()