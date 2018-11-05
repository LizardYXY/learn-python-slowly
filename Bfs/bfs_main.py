from Bfs import node


class BfsMain(object):
    def __init__(self):
        self.open_table = []
        self.closed_table = []

    def run(self, graph):
        # 把初始节点放入open表
        self.open_table.append(graph[1].get_num())
        # print(self.open_table)
        if len(self.open_table) == 0:
            return 1
        #
        select_node = self.open_table.pop(0)
        self.closed_table.append(graph[select_node])
        #
        if select_node is graph[5].get_num():
            return 0
        #
        while select_node == 0:
            if len(self.open_table) == 0:
                return 1
            #
            select_node = self.open_table.pop(0)
            print(select_node)
            self.closed_table.append(graph[select_node])
            #
            if select_node is graph[5].get_num():
                return 0

        #
        while select_node != 0:
            # graph[select_node].del_linkby()
            link_ones = graph[select_node].get_link()
            # print(link_ones)
            for link_one in link_ones:
                cost = graph[select_node].get_cost()

                if self.open_table.count(link_one):
                    if cost + 1 < graph[link_one].get_cost():
                        graph[link_one].del_linkby()
                        graph[link_one].linkedby(select_node)
                        graph[link_one].change_cost(cost + 1)

                elif self.closed_table.count(link_one):
                    if cost + 1 < graph[link_one].get_cost():
                        graph[link_one].del_linkby()
                        graph[link_one].linkedby(select_node)
                        graph[link_one].change_cost(cost + 1)

                    self.closed_table.remove(link_one)
                    self.open_table.append(link_one)

                else:
                    graph[link_one].linkedby(select_node)
                    graph[link_one].change_cost(cost + 1)
                    self.open_table.append(link_one)

            if len(self.open_table) == 0:
                return 1
            #
            select_node = self.open_table.pop(0)
            # print(select_node)
            self.closed_table.append(graph[select_node])
            #
            if select_node is graph[5].get_num():
                return 0


if __name__ == "__main__":
    node_1 = node.Node(1, [2, 3])
    node_2 = node.Node(2, [3, 4])
    node_3 = node.Node(3, [5])
    node_4 = node.Node(4)
    node_5 = node.Node(5, [4])

    graph = [0, node_1, node_2, node_3, node_4, node_5]
    # print(graph)
    bfs_obj = BfsMain()
    if bfs_obj.run(graph) == 0:
        print('found')

    for item in graph:
        if item != 0:
            print(item.isLinkedBy, item.get_cost())

    print('--')
    target = graph[5]
    while target != graph[1]:
        print(target.get_num())
        target = graph[target.isLinkedBy]

