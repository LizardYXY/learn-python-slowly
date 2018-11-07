import numpy as np

from linear import data_collect, perce_trainer, data_ploter, data_provide


class PerceMain(object):
    def __init__(self, eta=0.01, times=1):
        self.weight = []
        self.trainer_data = []
        self.eta = eta
        self.error_rate = []
        self.times = times

        self.data_provieder = data_provide.DataProvide()
        self.collector = data_collect.DataColllect()
        self.trainer = perce_trainer.PerceTrain()
        self.ploter = data_ploter.DataPloter()

    def run(self, train_text):
        self.data_provieder.provide(train_text, 1)
        # 读训练数据
        train_data, train_label = self.collector.read(train_text)
        # print(self.weight)
        # 权值初始
        for i in range(len(train_data[0]) + 1):
            self.weight.append(0.1)
        self.weight = np.mat(self.weight)
        for i in range(self.times):
            self.weight, error_rate = perce_trainer.train(train_data, train_label, self.weight, self.eta)
            self.error_rate.extend(error_rate)
        self.ploter.plot(train_data, train_label, self.weight, self.error_rate)
        print("Weight Vector: %s" % self.weight)


if __name__ == '__main__':
    train_text = 'train.txt'

    perce_obj = PerceMain()
    perce_obj.run(train_text)
