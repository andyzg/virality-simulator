import networkx as nx
from socialnetwork import SocialNetwork
from content import Content

from collections import defaultdict
import random
from constants import *
import util
import render


def main():
    g = nx.barabasi_albert_graph(NODE_COUNT, M_PARAM, 5)
    nodes = util.define_nodes(g)
    edges = util.define_affinity(g)
    # sn = SocialNetwork(g, nodes, edges)
    # bar = defaultdict(int)
    # for i in range(0, 500):
    #     bar[share_content(sn)] += 1
    # render.draw_bar(bar)


def share_content(sn):
    nodes = util.get_popular_nodes(sn)
    content = Content()
    sn.nodes[nodes[0]].seed_content(content)

    timestep = 1
    count = 0
    while not content.is_dead:
        # print("**************")
        # print("Timestep: ", timestep)
        probs = {}
        for i in sn.nodes:
            if content.uuid not in sn.nodes[i].content or i not in content.shared_by:
                probs[i] = util.probability_share_content(sn, sn.nodes[i], content)

        for i in probs:
            if random.random() < probs[i]:
                sn.nodes[i].share(content, timestep)
                # print(i, " shared the content at timestep")
                count += 1

        content.timestep()
        # print("Content score: ", content.score)
        timestep += 1
        # print("\n")

    print(count, " / ", NODE_COUNT, timestep)
    return count


if __name__ == '__main__':
    main()
