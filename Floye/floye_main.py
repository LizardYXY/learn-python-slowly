import numpy as np


class FloyeMain(object):
    def __init__(self):
        self.li = []

    def run(self, nodes):
        length = range(nodes.shape[0])
        for row in length:
            for col in length:
                for k in length:
                    # print(nodes[row, col])
                    new_dis = nodes[row, k] + nodes[k, col]
                    if nodes[row, col] > new_dis:
                        nodes[row, col] = new_dis
        self.li = nodes
        print(self.li)

if __name__ == "__main__":
    nodes = np.mat([[0, 1, np.inf, 12, np.inf, np.inf],
                   [1, 0, 9, 3, np.inf, np.inf],
                   [12, 9, 0, 4, 5, np.inf],
                   [np.inf, 3, 4, 0, 13, 15],
                   [np.inf, np.inf, 5, 13, 0, 4],
                   [np.inf, np.inf, np.inf, 15, 4, 0]])

    # print(nodes)
    floye_obj = FloyeMain()
    floye_obj.run(nodes)
