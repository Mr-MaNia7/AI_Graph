from math import sqrt,pow
from TSP.graph import Graph



# used for the depth_first_search as a data stracture
class Stack:
    def __init__(self):
        self._stack = []

    def push(self, node):
        self._stack.append(node)

    def pop(self):
        if len(self._stack) ==0:
            raise Exception("the stack is empty")
        else:
            return self._stack.pop()
   
    def is_empty(self):
        return len(self._stack) == 0


# used for the breadth_first_search as a data structure
class Queue:
    def __init__(self):
        self._queue = []

    def push(self, node):
        self._queue.append(node)

    def pop(self):
        if len(self._queue) ==0:
            raise Exception("the stack is empty")
        else:
            node = self._queue[0]
            self._queue = self._queue[1:]
            return node
    
    def is_empty(self):
        return len(self._queue) ==0

# used for the dijkstra_search and a star search as a data structure
class PriorityQueue:
    def __init__(self):
        self._queue = []

    def push(self, triple):
        item = self._Item(triple[2],[triple[0],triple[1]])
        self._queue.append(item)

    def pop(self):
        self._queue.sort()
        firest = self._queue[0]
        self._queue.remove(firest)
        return firest.data()
    
    def is_empty(self):
        return len(self._queue) == 0


    class _Item:
        def __init__(self, key, comp):
            self.key = key
            self._comp = comp

        def __lt__(self,other):
            return self.key < other.key
        
        def data(self):
            return [self._comp[0],self._comp[1],self.key]

        def __eq__(self, other):
            return self._comp[0] == other._comp[0]
     

# contains 4 search types
class Search:
    def __init__(self):
        pass

    def breadth_first_search(self, node, target):
        frontier = Queue()
        start_node = node
        visted = {}
        if target == node:
            visted[node.data()] =  node
        frontier.push([node, node])
       
        while not frontier.is_empty():
            pair = frontier.pop()
            node = pair[0]
            parent_node = pair[1]
            if node == target:
                visted[node.data()] = parent_node
                break
            if node.data() not in visted:
                visted[node.data()]= parent_node
            for child_node in node.adjacent_nodes():
                if child_node.data() not in visted:
                        frontier.push([child_node,node])

        if target.data() not in visted:
            print("No path found")               
        else:
            return self._compute_path(visted, start_node, target)
           
    
    def depth_first_search(self, node, target):
        frontier = Stack()
        start_node = node
        visted = {}
        if target == node:
            visted[node.data()] =  node
        frontier.push([node, node])
       
        while not frontier.is_empty():
            pair = frontier.pop()
            node = pair[0]
            parent_node = pair[1]
            if node == target:
                visted[node.data()] = parent_node
                break
            if node.data() not in visted:
                visted[node.data()]= parent_node
            for child_node in node.adjacent_nodes():
                if child_node.data() not in visted:
                        frontier.push([child_node,node])

        if target.data() not in visted:
            print("No path found")               
        else:
            return self._compute_path(visted, start_node, target)


    def dijkstra_search(self, node, target):
        frontier = PriorityQueue()
        start_node = node
        visted = {}
        if target == node:
            visted[node.data()] =  node
        frontier.push([node, node, 0])
       
        while not frontier.is_empty():
            triple = frontier.pop()
            node = triple[0]
            parent_node = triple[1]
            parent_node_weight =triple[2]

            if node == target:
                visted[node.data()] = parent_node
                break
            if node.data() not in visted:
                visted[node.data()]= parent_node
            for edge in node.incident_edges():
                for child_node in edge.opposite():
                    if child_node.data() not in visted:
                        value = parent_node_weight +edge.weight()
                        frontier.push([child_node, node, value])

        if target.data() not in visted:
            print("No path found")               
        else:
            return parent_node_weight


    def a_star_search(self, node, target):
        frontier = PriorityQueue()
        start_node = node
        visted = {}
        if target == node:
            visted[node.data()] = node
        frontier.push([node, node, 0])
       
        while not frontier.is_empty():
            triple = frontier.pop()
            node = triple[0]
            parent_node = triple[1]
            parent_node_weight =triple[2]
            
            if node == target:
                visted[node.data()] = parent_node
                break 
            if node.data() not in visted:
                visted[node.data()]= parent_node
            for edge in node.incident_edges():
                for child_node in edge.opposite():
                    if child_node.data() not in visted:
                        value = parent_node_weight + edge.weight()+self._heuristic(child_node, target)
                        frontier.push([child_node, node, value])

        if target.data() not in visted:
            print("No path found")               
        else:
            return parent_node_weight


    # bac trace and find the pathe the search findes 
    def _compute_path(self,visted, start_node, target):
        parent = visted[target.data()]
        path = [target.data(),parent.data()]

        while parent != start_node:
            parent = visted[parent.data()]
            path.append(parent.data())
        path.reverse()

        return path 

    # compute the heuristed value 
    def _heuristic(self,node, target):
        xsqouare = pow(target.latitude - node.latitude, 2)
        ysqouare = pow(target.longitude - node.longitude, 2)
        distance = sqrt(xsqouare+ysqouare)
        return distance
 

# read the text fiele and build the graph.
class BuildGraph():
    def __init__(self, file_name):
        file = open(file_name,'r')
        self._graph= Graph()
        self._file = file
        self._nodes = {}
        self._conection = []
        connection_part = False

        for row in file:
            if row == '\n':
                continue
            row = row.replace('\n', "")
            con= row.split(' ')

            if "CONNECTIONS:" in con:
                connection_part = True
                continue
            if not connection_part:
                node = self._graph.add_node(con[0],float(con[1]),float(con[2]))
                self._nodes[con[0]] = node
            if connection_part:
                self._conection.append(con)
                

    def giveMeGraph(self):
        for con in self._conection:
            self._graph.add_edge(self._nodes[con[0]], self._nodes[con[1]], int(con[2]))
        return self._graph


    


        


