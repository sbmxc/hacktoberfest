graph = {
    'F':['B','G'],
    'B':['A','D'],
    'G':['I'],
    'A':[],
    'D':['C','E'],
    'I':['H'],
    'C':[],
    'E':[],
    'H':[]
}
root = 'F'
target = 'E'
print('Using DFS:')

def rec(node,target):
    print(node, end=' ')
    if(node==target):
        return True
    elif len(graph[node])!=0:
        t = False
        for i in graph[node]:
            t = t or rec(i,target)
        return t
    else:
        return False
if (rec(root,target)):
    print()
    print("Target reached!")
else:
    print()
    print("Target not found!")
