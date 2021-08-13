class DAG:
    """Directed Acyclic Graph"""
    def __init__(self, G):
        self.G = G
        self.visited = []
        self.stack = []

    # helper function for topological sort
    def top_help(self, vert):
        self.visited.append(vert)

        for v in self.G.get(vert, []):
            if v not in self.visited:
                self.top_help(v)
        
        self.stack.insert(0, vert)
    
    # topological sort
    def top_sort(self):
        for v in self.G:
            if v not in self.visited:
                self.top_help(v)
        
        return "".join(self.stack)


def duplets(triplets):
    """Generate a list of 'edges' from the triplets"""
    dups = []
    for tup in triplets:
        for i in [0,1]:
            dup = [tup[i], tup[i+1]]
            if dup not in dups:
                dups.append(dup)
    return dups


def recoverSecret(triplets):
    graph = {}
    for a, b in duplets(triplets):
        graph[a] = graph.get(a, []) + [b]
    G = DAG(graph)
    return G.top_sort()


triplets = [
    ['w','h','i'],
    ['t','u','p'],
    ['h','a','p'],
    ['t','s','u'],
    ['t','i','s'],
    ['a','t','s'],
    ['w','h','s']
]



print(recoverSecret(triplets))