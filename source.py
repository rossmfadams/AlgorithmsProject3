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
    D = nx.Graph()

    # Add nodes from a list
    G.add_nodes_from("ABCDE")

    # Add edges from a list
    G.add_edges_from([('A','B'),('A','C'),('B','C'),('B','D'),('B','E'),('C','B'),\
        ('C','D'),('C','E'),('D','B'),('D','C'),('D','E'),('E','B'),('E','C'),('E','D')])

    # DijkstraAlgo
    D.add_nodes_from("ABCDEFGHI")

    D.add_edges_from([('A', 'B'), ('A', 'C'), ('A', 'D'),
                      ('B', 'H'), ('B', 'F'), ('B', 'C'), ('B', 'A'),
                      ('C', 'A'), ('C', 'D'), ('C', 'E'), ('C', 'F'), ('C', 'B'),
                      ('D', 'A'), ('D', 'C'), ('D', 'E'), ('D', 'I'),
                      ('E', 'C'), ('E', 'D'), ('E', 'F'), ('E', 'G'),
                      ('F', 'B'), ('F', 'C'), ('F', 'E'), ('F', 'G'), ('F', 'H'),
                      ('G', 'E'), ('G', 'F'), ('G', 'H'), ('G', 'I'),
                      ('H', 'B'), ('H', 'F'), ('H', 'G'), ('H', 'I'),
                      ('I', 'D'), ('I', 'G'), ('I', 'H')
                      ])

    D.add_weighted_edges_from([('A', 'B', 22), ('A', 'C', 9), ('A', 'D', 12),
                               ('B', 'H', 34), ('B', 'F', 36), ('B', 'C', 35), ('B', 'A', 22),
                               ('C', 'A', 9), ('C', 'D', 4), ('C', 'E', 65), ('C', 'F', 42), ('C', 'B', 35),
                               ('D', 'A', 12), ('D', 'C', 4), ('D', 'E', 33), ('D', 'I', 30),
                               ('E', 'C', 65), ('E', 'D', 33), ('E', 'F', 18), ('E', 'G', 23),
                               ('F', 'B', 36), ('F', 'C', 42), ('F', 'E', 18), ('F', 'G', 39), ('F', 'H', 24),
                               ('G', 'E', 23), ('G', 'F', 39), ('G', 'H', 25), ('G', 'I', 21),
                               ('H', 'B', 34), ('H', 'F', 24), ('H', 'G', 35), ('H', 'I', 19),
                               ('I', 'D', 30), ('I', 'G', 21), ('I', 'H', 19)
                               ])

    print('\n\nDijkstra\'s Algorithm\n')
    pred, dist = nx.dijkstra_predecessor_and_distance(D, 'A')
    print(sorted(pred.items()))
    print(sorted(dist.items()))
    print(nx.dijkstra_path(D, 'A', 'I'))
    print('\n\nBellman-Ford\'s Algorithm\n')
    # Bellman-Ford
    pred, dist = nx.bellman_ford_predecessor_and_distance(D, 'A')
    print(sorted(pred.items()))
    print(sorted(dist.items()))
    print(nx.bellman_ford_path(D, 'A', 'I'))

    print('\n\nTest Graph\n')
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
    nx.draw(D, with_labels=True, font_weight='bold')
    plt.show()


if __name__ == "__main__":
    main()
