from Graph2 import Graph

class Roadmap(Graph):
    def __init__(self):
        super().__init__()

    def get_index(self, list, vertex):
        i = 0
        for v in list:
            if v[0] == vertex:
                return i
            i+=1

    def print_shortest_distance(self, from_station: int, to_station: int):
        """This method determines and prints the shortest path between two stations (= vertex indices) "from_station" and "to_station",
       	 using the dijkstra algorithm. The shortest distance is returned.
       	 @param from_station
       	 	vertex index of the start station
       	 @param to_station
       	 	vertex index of the destination station
       	 @return
       	    The path with the already covered distance is returned as List of tuples. This list contains sequentially
       	    each station's name along the shortest path, together with the already covered distance.
       	    (see example on the assignment sheet)
    	 """
        start = self.vertices[from_station]
        end  = self.vertices[to_station]
        path = [(start.name, 0)]
        visitedNodes = set()
        V = [[start, 0]] + [ [x, float('Inf')] for x in self.vertices if x != start]

        idx = 0

        while V[idx][0]!=end:
            visitedNodes.add(V[idx][0])
            nextVertices = self.get_adjacent_vertices(self.vertices.index(V[idx][0]))

            for vertex in nextVertices:
                if vertex in visitedNodes:
                    continue
                vertex = self.vertices[vertex]
                if self.has_edge(V[idx][0], vertex) + V[idx][1] < V[self.get_index(V,vertex)][1]:
                    V[self.get_index(V, vertex)][1] = self.has_edge(V[idx][0], vertex) + V[idx][1]
            idx += 1
            if idx >= len(V):
                raise ValueError("The destination node can't be reached")


        currentNode = start
        visitedNodes = set()
        while currentNode != end and len(self.get_adjacent_vertices(self.vertices.index(currentNode)))!=0:
            visitedNodes.add(self.vertices.index(currentNode))
            nextNodesIdx = [self.get_index(V, self.vertices[x]) for x in self.get_adjacent_vertices(self.vertices.index(currentNode)) if x not in visitedNodes ]
            if len(nextNodesIdx) == 0:
                break
            minNodeIdx = min(nextNodesIdx, key=lambda i: V[i][1])
            path.append((V[minNodeIdx][0].name, V[minNodeIdx][1]))
            currentNode = V[minNodeIdx][0]
        return path

    def print_shortest_distances(self, from_station: int):
        """This method determines and prints the shortest path from station (= vertex index) "from_station" to all other stations
       	 using the dijkstra algorithm, and returns them in a list.
       	 @param from_station
       	 	vertex index of the start station
       	 @return:
       	 	the results in form of a list of integers, where the indices correspond to the indices of the stations.
       	    (see example on the assignment sheet)
        """
        result = []
        for i in range(len(self.vertices)):
            result.append(self.print_shortest_distance(from_station, i)[-1][1])
        return result



            
