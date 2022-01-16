from _collections import defaultdict


class Tree:
    def __init__(self):
        self.tree = defaultdict(list)
        self.amount = 0

    def edges(self,u,v,wights):
        value = (wights,v)
        self.tree[u].append(value)

    def hillclimb(self,start,goal):
        visited = []
        queue = []
        queue.append((0,start))
        while queue:
            item = queue.pop(0)
            currentnode = item[1]
            self.amount += item[0]

            if currentnode == goal:
                visited.append(currentnode)
                print("goal node: ",currentnode," cost: ",self.amount)
                break
            else:
                check = []
                if currentnode not in visited:
                    visited.append(currentnode)
                    print("path node: ", currentnode, " cost: ", self.amount)
                    for i in self.tree[currentnode]:
                        check.append((i[0],i[1]))
                    if not check:
                        break
                    else:
                        if check[0]<check[1]:
                            queue.clear()
                            queue.append(check[1])
                            check.clear()
                        else:
                            queue.clear()
                            queue.append(check[0])
                            check.clear()
            print("visted: ",visited)






t = Tree()
t.edges('A','B',8)
t.edges('A','C',5)
t.edges('B','D',3)
t.edges('B','E',6)
t.edges('C','F',2)
t.edges('C','G',4)

print(t.tree)

t.hillclimb('A','G')