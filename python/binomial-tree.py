class BinomialTree:
    def __init__(self, key):
        self.key = key
        self.children = []
        self.order = 0
 
    def add_at_end(self, t):
        self.children.append(t)
        self.order = self.order + 1
 
 
trees = []
 
print('Menu')
print('create <key>')
print('combine <index1> <index2>')
print('quit')
 
while True:
    do = input('What would you like to do? ').split()
 
    operation = do[0].strip().lower()
    if operation == 'create':
        key = int(do[1])
        btree = BinomialTree(key)
        trees.append(btree)
        print('Binomial tree created.')
    elif operation == 'combine':
        index1 = int(do[1])
        index2 = int(do[2])
        if trees[index1].order == trees[index2].order:
            trees[index1].add_at_end(trees[index2])
            del trees[index2]
            print('Binomial trees combined.')
        else:
            print('Orders of the trees need to be the same.')
 
    elif operation == 'quit':
        break
 
    print('{:>8}{:>12}{:>8}'.format('Index', 'Root key', 'Order'))
    for index, t in enumerate(trees):
        print('{:8d}{:12d}{:8d}'.format(index, t.key, t.order))
