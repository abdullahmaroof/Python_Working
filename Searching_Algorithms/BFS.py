tree = {'A':['B','C'],
        'B':['D','E'],
        'C':['F','G'],
        'D':[],
        'E':[],
        'F':[],
        'G':[]}

visted = []
queue = []

queue.append('A')

while queue:
    print("queue: ",queue)
    temp = queue.pop(0)
    visted.append(temp)
    print("visted: ",visted)
    for i in tree[temp]:
        if i not in visted:
            queue.append(i)