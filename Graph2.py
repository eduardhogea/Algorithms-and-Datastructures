from Vertex import My_Vertex
from Edge import My_Edge
import numpy

class Graph():
    def __init__(self):
        self.vertices = []  # list of vertices in the graph
        self.edges = []     # list of edges in the graph
        self.num_vertices = 0
        self.num_edges = 0
        self.undirected_graph = True

    def double_array_size(self):
        self.vertices = self.vertices.copy() + [My_Vertex()] * len(self.vertices) * 2
        self.edges = self.edges.copy() + [My_Edge()] * len(self.edges) * 2 * (len(self.edges) * 2 -1)

    def get_number_of_vertices(self):
        """return: the number of vertices in the graph
        """
        return self.num_vertices

    def get_number_of_edges(self):
        """return: the number of edges in the graph
        """
        return self.num_edges

    def get_vertices(self):
        """return: array of length get_number_of_vertices() with the vertices in the graph
        """
        temp=[]
        for i in range(0,self.get_number_of_vertices()):
            temp.append(self.vertices[i].name)
        #print(temp)
        return temp

    def get_edges(self):
        """return: array of length get_number_of_edges() with the edges in the graph
        """
        #temp=[]
        #for i in self.edges:
        #    temp.append(i)
        return self.edges

    def insert_vertex(self, vertex):
        """Inserts a new vertex into the graph and returns its index in the vertex array.
	    If the vertex array is already full, then the method double_array_size() shall be called
	    before inserting.
        None parameter is not allowed (ValueError).
        :param vertex: the vertex to be inserted
        :return: index of the new vertex in the vertex array
        :raises: ValueError if any of the parameters is None
        """
        
        if vertex==None:
            raise ValueError
        self.num_vertices+=1
        self.vertices.append(My_Vertex(vertex))
        return self.num_vertices-1

    def has_edge(self, vertex1, vertex2):
        """Returns the edge weight if there is an edge between index vertex1 and vertex2, otherwise -1.
	    In case of unknown or identical vertex indices raise a ValueError.
        :param vertex1: first vertex
        :param vertex2: second vertex
        :return: edge weight of -1 if there is no edge
        :raises: ValueError if any of the parameters is None
        """
        if vertex1==vertex2:
            raise ValueError
        if vertex1==None:
            raise ValueError
        if vertex2==None:
            raise ValueError
        for i in self.edges:
            if i.vertex_in in (vertex1,vertex2) and i.vertex_out in (vertex1,vertex2):
                return i.weight
        return -1

    def insert_edge(self, vertex1, vertex2, weight):
        """Inserts an edge between vertices with index of vertex1 and index of vertex2. False is returned if the edge already exists,
	    True otherwise. A ValueError shall be raised if the vertex indices are unknown (out of range) or
	    if v1 == v2 (loop).
        .
        .
        :param vertex1: first index of vertex
        :param vertex2: second index of vertex
        :param weight: weight of the edge
        :return: True if the edge could be created, False otherwise
        :raises: ValueError if any of the parameters is None any of the vertices is out of range
        """


        if vertex1==vertex2:
            raise ValueError
        if vertex1==None:
            raise ValueError
        if vertex2==None:
            raise ValueError
        if vertex1 > self.get_number_of_vertices()-1 or vertex2 > self.get_number_of_vertices()-1:
            raise ValueError

        for i in self.edges:
            if i.vertex_in in (vertex1,vertex2) and i.vertex_out in (vertex1,vertex2):
                return False
            
        self.num_edges+=1
        a = My_Edge()
        a.vertex_in = vertex1
        a.vertex_out = vertex2
        a.weight= weight
        self.edges.append(a)
        return True
        

    def get_adjacency_matrix(self):
        """Returns an NxN adjacency matrix for the graph, where N = get_number_of_vertices().
        The matrix contains 1 if there is an edge at the corresponding index position, otherwise 0.
        :return: NxN adjacency matrix
        """
        n=self.get_number_of_vertices()
        a = numpy.zeros(shape=(n,n))
        for i in self.edges:
            a[i.vertex_in][i.vertex_out]+=1
            a[i.vertex_out][i.vertex_in]+=1
        return a

    def get_adjacent_vertices(self, vertex):
        """Returns an array of vertices which are adjacent to the vertex with index "vertex".
        :param vertex: The vertex of which adjacent vertices are searched.
        :return: array of adjacent vertices to "vertex".
        :raises: ValueError if the vertex index "vertex" is unknown
        """
        temp=[]
        for i in self.edges:
            if i.vertex_in==vertex:
                temp.append(i.vertex_out)
            if i.vertex_out==vertex:
                temp.append(i.vertex_in)

        return temp
        

    # ------------- """Example 2""" -------------

    def is_connected(self):
        """return: True if the graph is connected, otherwise False.
        """
        visited = [False] * self.get_number_of_vertices()
        self.rec_dfs(visited)
        for visit in visited:
            if visit == False:
                return False

        return True

    def rec_dfs(self, visited, cur_vert_index=0):
        visited[cur_vert_index] = True
        adj_vertices = self.get_adjacent_vertices(cur_vert_index)
        for v_index in adj_vertices:
            if visited[v_index] != True:
                self.rec_dfs(visited, v_index)


    def get_number_of_components(self):
        """return: The number of all (weak) components
        """
        number_of_comp = 0
        visited = [False] * self.get_number_of_vertices()
        for v_index in range(len(visited)):
            if visited[v_index] == False:
                self.rec_dfs(visited, cur_vert_index=v_index)
                number_of_comp+=1
        return number_of_comp


    def print_components(self):
        """Prints the vertices of all components (one line per component).
        E.g.: A graph with 2 components (first with 3 vertices, second with 2 vertices) should look like:
   	 	[vertex1] [vertex2] [vertex3]
   	    [vertex4] [vertex5]
        """
        visited = [False] * self.get_number_of_vertices()
        for v_index in range(len(visited)):
            if visited[v_index] == False:
                self.rec_dfs_print(visited, cur_vert_index=v_index)
                print()

    def rec_dfs_print(self, visited, cur_vert_index=0):
        visited[cur_vert_index] = True
        print("["+str(self.vertices[cur_vert_index].name) +"]",end="")
        adj_vertices = self.get_adjacent_vertices(cur_vert_index)
        for v_index in adj_vertices:
            if visited[v_index] != True:
                self.rec_dfs_print(visited, v_index)

    def is_cyclic(self):
        """return: Returns True if the graphs contains cycles, otherwise False.
        """
        visited = [False] * self.get_number_of_vertices()
        for v_index in range(len(visited)):
            if visited[v_index] == False:
                if self.rec_is_cyclic(visited,v_index, v_index) == True:
                    return True

        return False


    def rec_is_cyclic(self, visited,prev_v_idx, cur_vert_index):
        visited[cur_vert_index] = True
        adj_vertices = self.get_adjacent_vertices(cur_vert_index)
        for adj_v_index in adj_vertices:
            if visited[adj_v_index] != True:
                if self.rec_is_cyclic(visited,cur_vert_index, adj_v_index) == True:
                    return True
            else:
                if prev_v_idx != adj_v_index:
                    return True
        return False
'''
if __name__ == '__main__':
    graph = Graph()

    graph.insert_vertex(My_Vertex("v0"))
    graph.insert_vertex(My_Vertex("v1"))
    graph.insert_vertex(My_Vertex("v2"))
    graph.insert_vertex(My_Vertex("v3"))
    graph.insert_vertex(My_Vertex("v4"))

    graph.insert_vertex(My_Vertex("v5"))
    graph.insert_vertex(My_Vertex("v6"))
    graph.insert_vertex(My_Vertex("v7"))

    graph.insert_edge(0, 1, 1)
    graph.insert_edge(1, 2, 1)
    graph.insert_edge(2, 3, 1)
    graph.insert_edge(3, 4, 1)
    #graph.insert_edge(4, 5, 1)

    graph.insert_edge(5, 6, 1)
    graph.insert_edge(6, 7, 1)
    graph.insert_edge(7, 5, 1)

    a = graph.get_adjacent_vertices(4)
    print(a)
    print(graph.is_connected())

    print(graph.get_number_of_components())

    graph.print_components()

    print(graph.is_cyclic())
'''

