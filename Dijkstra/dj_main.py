import random

from Dijkstra import env, visitor


class DjMain(object):
    def __init__(self):
        self.env = env.Env()
        self.visitor = visitor.Visitor()

    def go(self, nodes):
        # 写节点
        self.env.create(nodes)
        start = random.randint(1, len(nodes))
        print(str(start))

        remove_node = self.env.remove_node(start)
        self.visitor.update(start, remove_node)
        while self.env.has_node():
            number = self.visitor.choose_node()
            print(str(number))
            remove_node = self.env.remove_node(number)
            self.visitor.update(number, remove_node)


if __name__ == "__main__":
    # 节点的描述
    nodes = {
        1: {2: 1, 3: 12},
        2: {1: 1, 3: 9, 4: 3},
        3: {1: 12, 2: 9, 4: 4, 5: 5},
        4: {2: 3, 3: 4, 5: 13, 6: 15},
        5: {3: 5, 4: 13, 6: 4},
        6: {4: 15, 5: 4}
    }
    obj_dj = DjMain()
    obj_dj.go(nodes)
