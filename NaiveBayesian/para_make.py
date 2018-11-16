from math import sqrt


class ParaMaker(object):

    def data_collect(self, w_file):
        '''
        open fine and handle data form
        :param w_file: filename
        :return: data (list)
        '''
        datas = []
        fin = open(w_file, 'r')
        for line in fin.readlines():
            f = float(line.split('\n')[0])
            datas.append(f)
        fin.close()

        return datas

    def get_para(self, w_file):
        '''
        get parameter
        :param w_file: filename
        :return: average u and sigma's square
        '''
        datas = self.data_collect(w_file)
        tot = 0
        for data in datas:
            tot = tot + data
        average = tot/len(datas)
        tot = 0
        for data in datas:
            tot = tot + (data - average)*(data - average)
        sigma_square = tot/len(datas)
        # print(average, sigma_square)

        return average, sqrt(sigma_square)
