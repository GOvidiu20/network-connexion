# network-connexion
The solution is in network-connexion.py file \

1.I chose to represent the network as a set in which each component has a list associated with all his friends. I chose this representation because it is very easy to access a person and his list of friends.\
2.I chose a BFS (Breadth First Search) algorithm. I also consider the DFS (Depth First Search) algorithm because it is also good for finding a node in a graph. The BFS algorithm seemed more efficient to me because I do not search in the depth of each node but I go on each level of each person.\
3. I chose 2 cases, one in which I have a rather complex network and the algorithm had to go through several nodes, I found it relevant because it shows how the algorithm traverses people by levels and saves their parent (dad array) to retain the path. The second network is a network in which there is no path from A to B and I also found it an interesting example because we will not always have people who are connected to each other.
