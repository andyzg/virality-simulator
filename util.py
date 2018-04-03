from node import Node


def define_nodes(g):
    nodes = {}
    for i in g:
        nodes[i] = Node(i)


def define_affinity(g):
    """We define affinity as how much a person cares about another person. This
    is dependent on how many mutual friends they have."""
    for i in g:
        friends = {}
        for n in g.neighbors(i):
            friends[n] = mutual_friends(g, i, n)
        l = sorted(list(set(friends.values())))

        print(l)



def mutual_friends(g, n1, n2):
    nb1 = g.neighbors(n1)
    nb2 = g.neighbors(n2)
    return len(set([i for i in nb1]).intersection([i for i in nb2]))
