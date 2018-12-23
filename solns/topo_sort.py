class Graph:
    def __init__(self):
        self.graph = {}

    def add_node(self, a):
        self.graph[a] = []

    def add_edge(self, a, b):
        if a not in self.graph:
            self.add_node(a)
        self.graph[a].append(b)

    # use deque to get true linear time
    # NAIVE -> returns a topological sorting for graphs with cycles
    # if a graph has cycles, then we should throw an exception
    # def topo_sort(self):
    #     res = []
    #     visited = set()
    #     for node in self.graph:
    #         if node not in visited:
    #             self.visit(node, visited, res)
    #     return res

    # def visit(self, node, visited, res):
    #     visited.add(node)
    #     for neighbor in self.graph[node]:
    #         if neighbor not in visited:
    #             self.visit(neighbor, visited, res)
    #     res.insert(0, node)

    #depth first search can run on cycles  -> maintain visited set 
    #topo sort is a specialized type of dfs
    #can use dfs to check cycles by checking call stack

    def topo_sort(self):
        res = []
        visited = set()
        path = set()
        for node in self.graph:
            if node not in visited:
                self.visit(node, visited, res, path)
        return res

    def visit(self, node, visited, res, path):
        visited.add(node)
        path.add(node)
        for neighbor in self.graph[node]:
            if neighbor in path:
                raise ValueError("Graph has a cycle -> cannot return a topological sort!")
            if neighbor not in visited:
                self.visit(neighbor, visited, res, path)
        path.remove(node)
        res.insert(0, node)





test = Graph()
# test.add_edge(5, 11)
# test.add_edge(11, 2)
# test.add_edge(7, 11)
# test.add_edge(7, 8)
# test.add_edge(8, 9)
# test.add_edge(11, 9)
# test.add_edge(3, 8)
# test.add_edge(3, 10)
# test.add_edge(11, 10)
# test.add_node(17)
# test.add_node(35)

test.add_edge(1, 2)
test.add_edge(2, 3)
test.add_edge(3, 1)

print(test.topo_sort())