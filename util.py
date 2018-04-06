from node import Node
from edge import Edge


def define_nodes(g):
    nodes = {}
    for i in g:
        nodes[i] = Node(i)

    return nodes


def define_affinity(g):
    """We define affinity as how much a person cares about another person. This
    is dependent on how many mutual friends they have.

    Ex: If you're the person I have the most mutual friends with, then you're a 1.
    If I don't have any mutual friends with you, then you're a 1/num_friends.
    """
    edges = {}
    for i in g:
        friends = {}
        for n in g.neighbors(i):
            friends[n] = mutual_friends(g, i, n)
        l = sorted(list(set(friends.values())))

        # Create their score
        scores = {}
        for f in friends:
            scores[f] = (l.index(friends[f]) + 1) * 1.0 / len(l)

        # Create edges
        for f in friends:
            edges[(i, f)] = Edge(scores[f])
            print((i, f), scores[f])

    return edges

def mutual_friends(g, n1, n2):
    nb1 = g.neighbors(n1)
    nb2 = g.neighbors(n2)
    return len(set([i for i in nb1]).intersection([i for i in nb2]))
