from _collections import defaultdict
from queue import PriorityQueue

class Graph:
    def __init__(self,direction):
        self.direct = direction
        self.graph = defaultdict(list)
        self.amount = 0

    def edges(self,u,v,wieght):
        if self.direct:
            value = (wieght,v)
            self.graph[u].append(value)

        else:
            value = (wieght, v)
            self.graph[u].append(value)
            value = (wieght, u)
            self.graph[v].append(value)

    def ucs(self,startnode,goalnode):
        visited = []
        queue = PriorityQueue()
        queue.put((0,startnode))

        while queue:
            item = queue.get()
            currentnode = item[1]
            self.amount += item[0]

            if currentnode == goalnode:
                visited.append(currentnode)
                print("goal node", goalnode,"  cost: ",self.amount)
                break
            else:
                if currentnode not in visited:
                    visited.append(currentnode)
                    print("path node", currentnode, "  cost: ", self.amount)
                    for x in self.graph[currentnode]:
                        queue.put((x[0],x[1]))
        print("visted path: ",visited)



g = Graph(False)
g.graph = defaultdict(list)
g.edges('S','A',3)
g.edges('S','B',6)
g.edges('S','C',2)
g.edges('A','D',3)
g.edges('B','D',4)
g.edges('B','G',9)
g.edges('B','E',2)
g.edges('C','E',1)
g.edges('D','F',5)
g.edges('E','F',6)
g.edges('E','H',5)
g.edges('H','G',8)
g.edges('F','G',5)

print(g.graph)

g.ucs('S','G')