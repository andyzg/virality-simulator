import networkx as nx

from constants import *
import util


def main():
    g = nx.barabasi_albert_graph(50, 5, 5)
    nodes = util.define_nodes(g)
    edges = util.define_affinity(g)
    print(util.mutual_friends(g, 1, 2))
    print(nodes, edges)


if __name__ == '__main__':
    main()
