tree = {'0':['1','2'],
        '1':['3','4'],
        '2':['5','6'],
        '3':['7'],
        '4':['8'],
        '5':[],
        '6':[],
        '7':[],
        '8':[]}

visited = []
stack = []

def dfs(visit,dict1,node,level,levelend):
    while level<levelend:
        level = level + 1
        if node not in visit:
            stack.append(node)
            print("stack", stack)
            temp = stack.pop()
            visit.append(temp)
            for i in dict1[temp]:
                dfs(visit,dict1,i,level,levelend)
for x in range(1,4):
    stack.clear()
    visited.clear()
    print("level - ",x)
    dfs(visited,tree,'0',0,x)
    print("visited: ", visited)
