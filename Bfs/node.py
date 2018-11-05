class Node(object):
    def __init__(self, nodenum, canLink=[]):
        # 0代表没有被link
        self.cost = 0
        self.node_num = nodenum
        self.isLinkedBy = 0
        self.canLink = []
        for item in canLink:
            self.canLink.append(item)
        # print(self.canLink)

    def linkedby(self, master):
        self.isLinkedBy = master

    def del_linkby(self):
        self.isLinkedBy = 0

    def get_link(self):
        return self.canLink

    def get_num(self):
        return self.node_num

    def get_cost(self):
        return self.cost

    def change_cost(self, cost):
        self.cost = cost


