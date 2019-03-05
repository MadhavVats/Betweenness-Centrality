# Betweenness-Centrality
Given a graph the script reports top-’k’ nodes which have exact largest Standardized Betweenness Centrality score.
If there is a list of nodes sorted in decreasing order according to their Standardized Betweenness Centralities, the first ‘k’ nodes with equal Standardized Betweenness Centrality from this list will be the output. 

For accomplishing this last we can divide the task into sub-tasks:

    1. Creation of the graph

    2. Calculating the Standardized Betweenness Centrality of each of the nodes
        a. Calculating no. of shortest paths between a pair of nodes (say A and B)
            i. For this we will use a modification of the Depth First Search (DFS). 
            ii. First, find any one shortest path between A and B and calculate it’s length (say dist).
            iii. Now, we will find all paths which are at a distance of dist from node A. 
            iv. The paths which end at B will be our required set of paths. Let the no. of these paths be X.

        b. Calculating no. of shortest paths between a pair of nodes passing through the node chosen (say C) for calculating the Standardized Betweenness Centrality
            i. Out of all the shortest paths between A and B, we calculate the number of paths passing through node C. 
            ii. Let the no. of shortest paths passing through C be Y.
            iii. We can easily get the value of X/Y

        c. Repeat steps a and b for each pair of nodes. The summation of all the X/Y will be the Betweenness Centrality of node C. From this we can also calculate the Standardized Betweenness Centrality.

        d. Similarly, repeat steps a,b and c to get the Standardized Betweenness Centrality of all the nodes in the graph.

    3. Producing the output of top-‘k’ nodes
