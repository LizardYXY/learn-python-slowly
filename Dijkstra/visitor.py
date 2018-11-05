class Visitor(object):
    def __init__(self):
        self.old = {}

    def update(self, number, node):
        if node is None or number is None:
            return
        new_node = {number: node}
        self.old.update(new_node)

    def choose_node(self):
        mi = 999
        for key in self.old.keys():
            temp = self.old[key]
            for ak in temp.keys():
                if ak not in self.old.keys():
                    if temp[ak] < mi:
                        mi = temp[ak]
                        number = ak
        return number

