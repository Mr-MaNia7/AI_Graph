class Graph(object):
    def __init__(self):
        self._nodes= {}
        self._edges = []
        self._adjacent_node=[]
        

    def count_node(self):
        """
        Returns:
            The number of node the graph has
        """
        
        return len(self._nodes)
    

    def adjacent_nodes(self,node):
        """
        Returns:
            The adjacent_nodes of the given node
        """
        if node.data() in self._nodes:
            return node.adjacent_nodes()

    
    def nodes(self):
        """
        Returns:
            The nodes as a python list
        """
        return list(self._nodes.values())


    def count_edge(self):
        """
        Returns:
            The number of edge the graph has
        """
        return len(self._edges)

    
    def edges(self):
        """
        Returns:
            The edges as a python list
        """
        return self._edges


    def get_edge(self, origin, destination):
        """
        Returns:
            The edge between the given node if thare is not edge it will return None
        """

        if (origin, destination) in self._adjacent_node:
            return self._edges[self._adjacent_node.index((origin, destination))] 
        elif (destination, origin) in self._adjacent_node:
            return self._edges[self._adjacent_node.index((destination, origin))]
        else:
            return None
    

    def degree(self,node):
        """
        Returns:
            The dgree of the give node if the node doesn't exsit it will return None
        """
        if node in self._nodes:
            return len(self._nodes[node].incident_edges())
        else:
            return None

    
    def incident_edges(self,node):
        """
        Returns:
            The incident edge of the give node as a list if the node doesn't exsit it will return None
        """
        if node.data() in self._nodes:
            return self._nodes[node.data()].incident_edges()
        else:
            return None

    
    def add_node(self, data,latitude,longitude):
        """
        Add a new node to the graph

        Returns:
             node
        """
        node = Node(data,latitude,longitude)
        if not data in self._nodes:
            self._nodes[data] = node 
        
        return node

    
    def add_edge(self, origin_node, destination_node, weight =1):
        """
        add a new edge between the given nodes  to the graph

        Returns:
             edge
        """
        edge = Edge(origin_node, destination_node,weight)
        self._edges.append(edge)
        
        origin_node.add_incident_edges(edge)
        destination_node.add_incident_edges(edge)
        origin_node.add_adjacent_node(destination_node)
        destination_node.add_adjacent_node(origin_node)
        self._adjacent_node.append((origin_node, destination_node))

        return edge


    def remove_node(self, node):
        """
        remove the given node from the grap
            This method works in O(d(node)) time 

        """
        if node.data() in self._nodes:
            for edge in node.incident_edges():
                self._adjacent_node.remove(edge.opposite())
                self._edges.remove(edge)
            self._nodes.pop(node.data())
        
        

    def Remove_edge(self, edge):
        """
        Remove the given edge from the graph
        
        """
        pair = edge.opposite()
        origin = pair[0]
        destination = pair[1]
        origin.remove_incident_edge(edge)
        destination.remove_incident_edge(edge)
        self._adjacent_node.remove(pair)
        self._edges.remove(edge)

          
    def __str__ (self):
        """
        The string representation of the graph
        
        """
        eges = ','.join([str(i) for i in self._edges])
        node = ','.join([str(key) for key in self._nodes.keys()])
        return "["+ node + "] " + " ,[" + eges + "]"


class Node(object):

    def  __init__(self, data,latitude,longitude):
       self._data = data
       self.latitude = latitude
       self.longitude = longitude
       self._incidents_edges = set()
       self._adjacent_node = set()
 

    def data(self):
        """
        Returns:
             The data associated with the node
        """
        return self._data

    
    def add_incident_edges(self, edge):
        """
        The incident edge of the  node as a list 
        """
        if not edge in self._incidents_edges:
            self._incidents_edges.add(edge)

    def add_adjacent_node(self, node):
    
        if not node in self._adjacent_node:
            self._adjacent_node.add(node)

    
    def remove_incident_edge(self, edge):
        
        if edge in self._incidents_edges:
            self._incidents_edges.remove(edge)

    
    def incident_edges(self):
            """
            Returns:
                The incident edge of the node as a list 
            """
            return self._incidents_edges

    def adjacent_nodes(self):
            """
            Returns:
                The incident edge of the node as a list 
            """
            return self._adjacent_node
             
    
    def postion(self):
        """
        Returns:
             latitude-longitude pairs of the node postion
        """
        return(self.latitude, self.longitude)


    def __str__ (self):
        """
        Returns:
             The string representation of the node
        """
        return str(self._data)

    
    def __eq__(self, node):
        return self._data == node.data()

    def __hash__(self):
        return hash(self._data)

  
class Edge(object):
    def __init__(self,origin, destination, weight):
        self._origin = origin
        self._destination = destination
        self._weight = weight


    def weight(self):
        """
        Returns:
             The weight the edge do
        """
        return self._weight


    def opposite(self):
        """
        Returns:
             The end point of the node
        """
        return (self._origin, self._destination)

    
    def __str__ (self):
        """
        Returns:
             The string representation of the ege
        """
        return "("+ str(self._origin) + "," + str(self._destination) + ")"



    
        


    