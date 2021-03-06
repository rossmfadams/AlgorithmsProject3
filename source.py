## Source.py

## Authors: Ross Adams, Longtin Hang, Riley Williams


import networkx as nx
import matplotlib.pyplot as plt
import bfs_path
import dfs_path


# main function


def main():
    # Tasks 1 and 2
    # Create a graph
    B = nx.Graph()
    G = nx.Graph()
    D = nx.Graph()

    # Add nodes from a list
    G.add_nodes_from("ABCDE")
    B.add_nodes_from("ABCDEFGHIJKLMNOP")
    B2 = B
    DFS = B
    DFS2 = B

    # Add edges from a list
    G.add_edges_from([('A','B'),('A','C'),('B','C'),('B','D'),('B','E'),('C','B'),\
        ('C','D'),('C','E'),('D','B'),('D','C'),('D','E'),('E','B'),('E','C'),('E','D')])
    
    B.add_edges_from([('A','B'),('A','F'),('A','E'),('B','C'),('B','F'),('C','D'),('C','G'), \
                       ('D','G'),('E','F'),('E','I'),('F','I'),('G','J'),('H','K'),('H','L'), \
                       ('I','J'),('I','M'),('K','L'),('K','O'),('L','P'),('M','N')])
    # DFS
    print('\n\nDFS\n')

    # DFS Path from A to G
    print('\nDFS Path from A to G')
    print(dfs_path.dfs_path(DFS,'A','G'))

    # DFS trees
    DFS = nx.dfs_tree(DFS,'A')
    DFS2 = nx.dfs_tree(DFS2,'H')
    plt.subplot(121)
    nx.draw_planar(DFS, with_labels=True, font_weights='bold')
    plt.subplot(122)
    nx.draw_planar(DFS2, with_labels=True, font_weights='bold')
    plt.show()

    # DFS Tree Printout
    print('\nDFS Tree from A')
    print(nx.dfs_successors(DFS,'A'))
    print('\nDFS Tree from H')
    print(nx.dfs_successors(DFS2,'H'))

    # BFS
    print('\n\nBFS\n')

    # BFS Path from A to G
    print('\nBFS Path from A to G')
    print(bfs_path.bfs_path(B,'A','G'))

    # BFS trees
    B = nx.bfs_tree(B,'A')
    B2 = nx.bfs_tree(B2,'H')
    plt.subplot(121)
    nx.draw_planar(B, with_labels=True, font_weights='bold')
    plt.subplot(122)
    nx.draw_planar(B2, with_labels=True, font_weights='bold')
    plt.show()

    # BFS Tree Printout
    print('\nBFS Tree from A')
    print(nx.dfs_successors(B,'A'))
    print('\nBFS Tree from H')
    print(nx.dfs_successors(B2,'H'))


    # Task 3
    print('\nDiGraph\n')
    Di = nx.DiGraph()

    Di.add_nodes_from(range(1,13))

    Di.add_edges_from([(1,3),(2,1),(3,2),(3,5),(4,1),(4,2),(4,12),(5,6),(5,8),
                       (6,8),(6,7),(6,10),(7,10),(8,9),(8,10),(9,5),(9,11),
                       (10,9),(10,11),(11,12)])

    #pos = nx.planar_layout(Di)
    nx.draw_spring(Di, arrows=True,with_labels=True, font_weight='bold')
    plt.show()
    # Counting the number of SCC in the Digraph
    print("\nNumber of Strongly Connected Components: ")
    print(nx.number_strongly_connected_components(Di))

    # Display SCC
    print("\nStrongly Connect Components: ")
    comp = nx.strongly_connected_components(Di)
    for c in comp:
        print(c,'\n')

    # Find the DAG of a graph
    A = nx.DiGraph()
    A = nx.condensation(Di)
    
    # Display resulting DAG
    print('\nDAG: ')
    print(A.nodes(data=True))
    
    nx.draw_spring(A, with_labels=True, font_weight='bold' )
    plt.show()
    

    # Verify that new 'meta graph' is a DAG
    print("\nDigraph is now a DAG: ")
    print(nx.is_directed_acyclic_graph(A))

    # Topological sort of DAG nodes
    print("\nTopological Order: ")
    print(list(list(nx.topological_sort(A))))

    #  Task 4

    # DijkstraAlgo

    # Build Graph from Dijkstra and Kruskal
    D.add_nodes_from("ABCDEFGHI")

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

    # Dijkstra's Algorithm
    print('\n\nDijkstra\'s Algorithm')
    pred, dist = nx.dijkstra_predecessor_and_distance(D, 'A')
    print('\nDijkstra\'s Algorithm Graph')
    print(sorted(pred.items()))
    print('\nDijkstra\'s Algorithm Distance')
    print(sorted(dist.items()))
    print('\nDijkstra\'s Algorithm shortest path from source node to target node')
    print(nx.dijkstra_path(D, 'A', 'I'))


    # kruskal's Algorithm
    print('\n\nKruskal\'s Algorithm')
    print('\nMinimum Spanning Tree')
    T = nx.minimum_spanning_tree(D, algorithm='kruskal')
    nx.draw_spring(T, with_labels=True, font_weights='bold')
    plt.show()
    print(sorted(T.edges(data=True)))

if __name__ == "__main__":
    main()
