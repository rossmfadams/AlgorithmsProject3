#  prim.py
#  Prim's algorithm finds a minimum spanning tree
#  Source: https://programmingpraxis.com/2010/04/09/minimum-spanning-tree-prims-algorithm/
#  Contributed by: Ross Adams

from collections import defaultdict
from heapq import *
 
def prim( nodes, edges ):
    conn = defaultdict( list )
    for n1,n2,c in edges:
        conn[ n1 ].append( (c, n1, n2) )
        conn[ n2 ].append( (c, n2, n1) )
 
    mst = []
    used = set( [nodes[ 0 ]] )
    usable_edges = conn[ nodes[0] ][:]
    heapify( usable_edges )
 
    while usable_edges:
        cost, n1, n2 = heappop( usable_edges )
        if n2 not in used:
            used.add( n2 )
            mst.append( ( n1, n2, cost ) )
 
            for e in conn[ n2 ]:
                if e[ 2 ] not in used:
                    heappush( usable_edges, e )
    return mst
