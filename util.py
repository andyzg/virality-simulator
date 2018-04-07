from constants import *
from node import Node
from edge import Edge
import math


def define_nodes(g):
    nodes = {}
    for i in g:
        neighbors = [n for n in g.neighbors(i)]
        nodes[i] = Node(i, neighbors)

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

    return edges


def mutual_friends(g, n1, n2):
    """Gets the number of mutual friends between two nodes."""
    nb1 = g.neighbors(n1)
    nb2 = g.neighbors(n2)
    return len(set([i for i in nb1]).intersection([i for i in nb2]))


def probability_share_content(sn, n1, c):
    edge_scores = []
    for n in sn.nodes[n1.node_id].neighbors:
        node = sn.nodes[n]
        edge = sn.edges[(n1.node_id, n)]
        # Preferential attachment
        if c.uuid in node.content or n in c.shared_by:
            edge_scores.append(edge.rank_score)
    distance = n1.interest.distance(c.interest)
    if len(edge_scores) == 0:
        return 0

    n1.impression(c)
    prob = (1 - math.exp(-1 * sum(edge_scores))) * distance  # converge towards 1
    return (1 - (1 - prob) ** (1.0 / TIMESTEPS_TILL_DEAD))


def get_popular_nodes(sn):
    # Order nodes by their number of neighbors
    return list(map(lambda x: x.node_id, sorted(sn.nodes.values())))
