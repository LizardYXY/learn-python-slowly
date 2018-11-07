
class ParaMaker(object):
    def __init__(self):
        self.w_data = []

    def data_collect(self, w_file):
        fin = open(w_file, 'r')
        for line in fin.readlines():
            f = float(line.split('\n')[0])
            self.w_data.append(f)
        fin.close()

    def get_para(self, w_file):
        self.data_collect(w_file)
        tot = 0
        for data in self.w_data:
            tot = tot + data
        average = tot/len(self.w_data)
        tot = 0
        for data in self.w_data:
            tot = tot + (data - average)*(data - average)
        sigma_square = tot/len(self.w_data)
        return average, sigma_square
