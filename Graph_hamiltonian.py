# import matplotlib as plt
import networkx as nx
import argparse
import numpy as np
import random

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--d", default=False, type=str, help="1: Directed, 0: Undirected")
    parser.add_argument("--n", default=5, type=int, help="Number of nodes")
    parser.add_argument("--p", default=0.5, type=float, help="desnity of edges")
    parser.add_argument("--c", default=0, type=int, help="1: Cylic, 0: non Cyclic")
    parser.add_argument("--t", default=1, type=int, help="1: Permute, 0: HK Algorithm")
    parser.add_argument("--src", default=random.randint(0,0), type=int, help="Source Vertex")
    parser.add_argument("--dest", default=random.randint(0,0), type=int, help="Destination Vertex")
    args = parser.parse_args()
    n = args.n
    d = args.d
    p = args.p
    c = args.c
    t = args.t
    src = args.src
    dest = args.dest
    if(c):
        G=nx.cycle_graph(n)
    else:
        G=nx.fast_gnp_random_graph(n,p,seed=3,directed=d)

    # Hamilton paths using checking all simple paths
    # Complexity of O(n*n!) 
    def Hamilton_using_all_permutations(G,src,dest):
        h_path = []
        for path in nx.all_simple_paths(G, source=src, target=dest):
            if(len(path) == n):
                h_path.append(path) 
        return h_path

    # Hamilton paths using Held-Karp Algorithm
    # Complexity of O(n^2*2^n)
    def Hamiltonian_using_HK_algorithm(G,n,src,dest):
        dp = np.zeros([n, 1<<n],dtype=int)
        adj= nx.to_numpy_matrix(G)
        n_path=0
        for i in range(n):
            dp[i][1<<i] = True

        for i in range(1<<n):
            for j in range(n):
                if (i & (1<<j)):
                    for k in range(n):
                        if((i & (1<<k)) and (j!=k) and dp[k][i ^ (1<<j)] and (adj[k,j]==True)):
                            dp[j][i] = True
                            break
        for i in range(n):
            if(dp[i][(1<<n)-1]):
                n_path +=1

        return n_path,dp

    if(t):
        h_path = Hamilton_using_all_permutations(G,src,dest)
    else:
        [n_path,dp] = Hamiltonian_using_HK_algorithm(G,n,src,dest)


