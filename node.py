from interest import Interest


class Node:

    def __init__(self, node_id, neighbors):
        self.node_id = node_id
        self.interest = Interest()
        self.neighbors = neighbors
        self.content = {}
        self.seen = {}

    def seed_content(self, content):
        self.share(content, 0)

    def share(self, content, timestep):
        self.content[content.uuid] = timestep
        content.is_shared(self.node_id)

    def __cmp__(self, other):
        if len(self.neighbors) < len(others.neighbors):
            return -1
        elif len(self.neighbors) > len(others.neighbors):
            return 1
        return 0

    def __lt__(self, other):
        return len(self.neighbors) < len(other.neighbors)

    def __eq__(self, other):
        return len(self.neighbors) == len(other.neighbors)

    def impression(self, content):
        self.seen[content.uuid] = True
