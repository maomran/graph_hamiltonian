# Hamiltonian Path of a Graph 
Finding Hamiltonian Paths of a graph data structure 

## Dependencies 
Get NetworkX from the Python Package Index at [networkx](http://pypi.python.org/pypi/networkx)

or install it with:
```bash
pip install networkx
```

## Usage 
In terminal, run the following:
```bash
python Graph_hamiltonian.py -h 
```
## Algorithms
The code uses two algorithms to find all the Hamiltonian paths of a graph `(if exists)`, these algorithms are 
### Check all perumtations
- Given a start and end node, the algorithm tries to find all possible simple paths between these two nodes, and then compares each one of them if it passes by all the nodes in the graph. 

- Comlexity of this algorith is `O(N*N!)`

### Held–Karp algorithm
- This algorithm uses dynamic programming to check whether a Hamiltonian Path exists in a graph or not.
Starting at the begin vertex, the algorithm keeps looking for a path that pass with all the next nodes, it keeps creating bigger sets till it passes by all nodes. 

- Comlexity of this algorith is `O(N^2*2^N)`

## Referenes
1. [hamiltonian path tutorial](https://www.hackerearth.com/practice/algorithms/graphs/hamiltonian-path/tutorial/)
2. [https://networkx.github.io/documentation/networkx-1.10/overview.html](https://networkx.github.io/documentation/networkx-1.10/overview.html)
