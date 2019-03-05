#!/usr/bin/env python3

import re
import itertools
from math import inf

ROLLNUM_REGEX = "201[0-9]{4}"

class Graph(object):
    name = "madhav"
    email = "madhav18046@iiitd.ac.in"
    roll_num = "2018046"

    def __init__ (self, vertices, edges):
        """
        Initializes object for the class Graph

        Args:
            vertices: List of integers specifying vertices in graph
            edges: List of 2-tuples specifying edges in graph
        """

        self.vertices = vertices
        
        ordered_edges = list(map(lambda x: (min(x), max(x)), edges))
        
        self.edges = ordered_edges
        
        self.validate()

    def validate(self):
        """
        Validates if Graph if valid or not

        Raises:
            Exception if:
                - Name is empty or not a string
                - Email is empty or not a string
                - Roll Number is not in correct format
                - vertices contains duplicates
                - edges contain duplicates
                - any endpoint of an edge is not in vertices
        """

        if (not isinstance(self.name, str)) or self.name == "":
            raise Exception("Name can't be empty")

        if (not isinstance(self.email, str)) or self.email == "":
            raise Exception("Email can't be empty")

        if (not isinstance(self.roll_num, str)) or (not re.match(ROLLNUM_REGEX, self.roll_num)):
            raise Exception("Invalid roll number, roll number must be a string of form 201XXXX. Provided roll number: {}".format(self.roll_num))

        if not all([isinstance(node, int) for node in self.vertices]):
            raise Exception("All vertices should be integers")

        elif len(self.vertices) != len(set(self.vertices)):
            duplicate_vertices = set([node for node in self.vertices if self.vertices.count(node) > 1])

            raise Exception("Vertices contain duplicates.\nVertices: {}\nDuplicate vertices: {}".format(vertices, duplicate_vertices))

        edge_vertices = list(set(itertools.chain(*self.edges)))

        if not all([node in self.vertices for node in edge_vertices]):
            raise Exception("All endpoints of edges must belong in vertices")

        if len(self.edges) != len(set(self.edges)):
            duplicate_edges = set([edge for edge in self.edges if self.edges.count(edge) > 1])

            raise Exception("Edges contain duplicates.\nEdges: {}\nDuplicate vertices: {}".format(edges, duplicate_edges))
    #returns all posible paths from a particular node
    def pospaths(self,start, edges):
        def neif(k, s):
            neighbours = []
            for i in k:
                if i[0] == s:
                    neighbours.append(i[1])
                elif i[1] == s:
                    neighbours.append(i[0])
            return neighbours

        q = [start]
        tree = [[start]]
        branched = []
        count = 0
        while len(q) > 0:
            nei = neif(edges, q[0])
            for i in nei:
                if (i in q) == False and (i in branched) == False:
                    q.append(i)
            node = q.pop(0)
            branched.append(node)
            for i in range(len(tree)):
                if tree[i][-1] in neif(edges, node) and count != 0:
                    tree.append(tree[i] + [node])

            count = count + 1
        return (tree)

    def min_dist(self, start_node, end_node):
        '''
        Finds minimum distance between start_node and end_node

        Args:
            start_node: Vertex to find distance from
            end_node: Vertex to find distance to

        Returns:
            An integer denoting minimum distance between start_node
            and end_node
        '''
        posp=self.pospaths(start_node,edges)
        mdis=inf
        for i in posp:
            if i[0]==start_node and i[-1]==end_node and len(i)<mdis:
                mdis=len(i)
        return mdis-1




        raise NotImplementedError

    def all_shortest_paths(self,start_node, end_node):
        """
        Finds all shortest paths between start_node and end_node

        Args:
            start_node: Starting node for paths
            end_node: Destination node for paths

        Returns:
            A list of path, where each path is a list of integers.
        """
        mind=self.min_dist(start_node,end_node)
        posp=self.pospaths(start_node,edges)
        lis=[]
        for i in posp:
            if i[0]==start_node and i[-1]==end_node and len(i)==mind+1:
                lis.append(i)
        return lis
        raise NotImplementedError

    def all_paths(self,node, destination, dist, path):
        """
        Finds all paths from node to destination with length = dist

        Args:
            node: Node to find path from
            destination: Node to reach
            dist: Allowed distance of path
            path: path already traversed

        Returns:
            List of path, where each path is list ending on destination

            Returns None if there no paths
        """
        def neif(k, s):
            neighbours = []
            for i in k:
                if i[0] == s:
                    neighbours.append(i[1])
                elif i[1] == s:
                    neighbours.append(i[0])
            return neighbours
        def endnodes(n):
            lis=[]
            for i in n:
                lis.append(i[-1])
            return lis
        k=["l"]
        newnodes=[]
        flag=0
        flag1=0
        lenbt=[]
        while flag<10000 and flag1<10000:
            bt=[[node]]
            k=[]

            k.extend(neif(edges,node))
            for i in newnodes:

                k.extend(neif(edges,i))
            for i in range(len(k)):
                for j in range(len(bt)):
                    yo=endnodes(bt)[j]
                    if yo in neif(edges,k[i]) and (k[i] in bt[j])==False:
                        ios=bt[j]+[k[i]]
                        if (ios in bt)==False:
                            newnodes.append(ios[-1])
                            bt.append(ios)
                        else:
                            flag=flag+1
                    if yo in neif(edges,k[len(k)-i-1]) and (k[len(k)-i-1] in bt[j])==False:
                        ios = bt[j] + [k[len(k)-i-1]]
                        if (ios in bt)==False:
                            newnodes.append(ios[-1])
                            bt.append(ios)
                        else:
                            flag1=flag1+1
        kp = []
        flag = 0
        for i in bt:
            if i[0] == node and i[-1] == destination and len(i) == dist + 1:
                kp.append(i)
                flag = 1
        if flag == 0:
            return None
        return kp











        raise NotImplementedError

    def betweenness_centrality(self, node):
        """
        Find betweenness centrality of the given node

        Args:
            node: Node to find betweenness centrality of.

        Returns:
            Single floating point number, denoting betweenness centrality
            of the given node
        """
        bet=0
        lll=[]
        for i in vertices:
            if i==node:
                continue
            posp = self.pospaths(i,edges)

            for k in posp:
                if ({k[0],k[-1]} in lll)==False and k[0]!=node and k[-1]!=node and k[0]!=k[-1]:
                    lll.append({k[0],k[-1]})


        for i in lll:
            py=0
            i=list(i)
            minp=self.all_shortest_paths(i[0],i[1])
            for k in minp:
                if node in k:
                    py=py+1
            bet=bet+(float(py)/float(len(minp)))

        return bet


        raise NotImplementedError

    def top_k_betweenness_centrality(self):
        """
        Find top k nodes based on highest equal betweenness centrality.

        
        Returns:
            List a integer, denoting top k nodes based on betweenness
            centrality.
        """
        finaldici={}
        ak=float(len(vertices)-1)*float(len(vertices)-2)
        ak=ak/2
        for i in vertices:

            finaldici[i]=self.betweenness_centrality(i)/ak
        m=max(list(finaldici.values()))
        flis=[]
        for i in finaldici:
            if finaldici[i]==m:
                flis.append(i)


        return flis

        raise NotImplementedError


if __name__ == "__main__":
    vertices = [1, 2, 3, 4, 5, 6]
    edges    = [(1, 2), (1, 5), (2, 3), (2, 5), (3, 4), (4, 5), (4, 6),(3,6)]
    #edges = [(1, 2), (1, 6), (6, 7), (7, 10), (4, 10), (3, 4), (3, 5), (2, 3), (5, 10), (3, 7), (6, 8), (8, 9), (9, 10),(6,11),(2,11)]
    #vertices = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10,11]
    graph = Graph(vertices, edges)
    print(graph.all_shortest_paths(1,6))
    print(graph.betweenness_centrality(3))
    print(graph.top_k_betweenness_centrality())
    print(graph.min_dist(1,6))
    print(graph.all_paths(1,6,3,0))

