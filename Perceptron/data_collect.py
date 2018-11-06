class DataColllect(object):
    def __init__(self):
        self.datas = []
        self.label = []

    def read(self, train_text):
        fin = open(train_text, 'r')
        for data in fin.readlines():
            self.datas.append([float(data.split(' ')[0]), float(data.split(' ')[1])])
            self.label.append(float(data.split(' ')[2][0]))
        fin.close()
        return self.datas, self.label

