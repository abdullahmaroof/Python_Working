from _collections import defaultdict

class Tree:
    def __init__(self):
        self.tree = defaultdict(list)
        self.amount = 0
        self.distance = {}

    def edges(self,u,v,wieght):
        value = (wieght,v)
        self.tree[u].append(value)

    def goaldistance(self,node,hd):
        self.distance.update({node:hd})

    def localbeam(self,cn,g):
        visited = []
        queue = []
        queue.append((0,cn))

        while queue:
            check = []
            item = queue[0]
            currentnode = item[1]
            self.amount += item[0]

            if currentnode == g:
                print("goal node: ",currentnode," amount: ",self.amount)
                visited.append(cn)
                queue.clear()
            else:
                if currentnode not in visited:
                    print("current node: ",currentnode," amount: ",self.amount)
                    visited.append(currentnode)
                    for i in self.tree[currentnode]:
                        check.append((i[0],i[1]))
                    print(check)
                    if not check:
                        break
                    else:
                        item1 = check[0]
                        item2 = check[1]
                        if self.distance[item1[1]]<self.distance[item2[1]]:
                            queue.clear()
                            queue.append(item1)
                            del item1
                            del item2
                            check.clear()
                        else:
                            queue.clear()
                            queue.append(item2)
                            del item1
                            del item2
                            check.clear()

        print("visited: ",visited)





g = Tree()
g.tree = defaultdict(list)
g.edges('A','B',2)
g.edges('A','C',3)
g.edges('B','D',3)
g.edges('B','E',4)
g.edges('C','F',2)
g.edges('C','G',1)
print("tree: ",g.tree)
g.goaldistance('A',42)
g.goaldistance('B',38)
g.goaldistance('C',40)
g.goaldistance('D',12)
g.goaldistance('E',34)
g.goaldistance('F',15)
g.goaldistance('G',0)
print("hue distance from goal node: ",g.distance)
g.localbeam('A','G')