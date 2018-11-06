from linear import data_collect, perce_trainer, data_ploter


class PerceMain(object):
    def __init__(self, eta=0.01, count=10):
        self.weight = []
        self.trainer_data = []
        self.eta = eta
        self.count = count
        self.collector = data_collect.DataColllect()
        self.trainer = perce_trainer.PerceTrain()
        self.ploter = data_ploter.DataPloter()

    def run(self, train_text):
        # 读训练数据
        train_data, train_label = self.collector.read(train_text)
        # print(self.weight)
        new_weight = perce_trainer.train(train_data, train_label, self.weight, self.eta)
        self.ploter.plot(train_data, train_label, new_weight)
        print("Weight Vector: %s" % new_weight)

if __name__ == '__main__':
    train_text = 'train.txt'

    perce_obj = PerceMain()
    perce_obj.run(train_text)
