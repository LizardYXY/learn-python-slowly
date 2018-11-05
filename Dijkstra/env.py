class Env(object):
    def __init__(self):
        self.nodes = {}

    def create(self, nodes):
        if nodes is None:
            return
        self.nodes = nodes

    def has_node(self):
        return len(self.nodes) != 0

    def remove_node(self, num):
        if num is None:
            return
        node = self.nodes[num]
        del self.nodes[num]
        return node
