tree = {'A':['B','C'],
        'B':['D','E'],
        'C':['F','G'],
        'D':[],
        'E':[],
        'F':[],
        'G':[]}

visited = []
stack = []

def dfs(visit,dict1,node):
    stack.append(node)
    print("stack", stack)
    if node not in visit:
        temp = stack.pop()
        visit.append(temp)
        print("visited: ",visit)
        for i in dict1[temp]:
            dfs(visit,dict1,i)

dfs(visited,tree,'A')
