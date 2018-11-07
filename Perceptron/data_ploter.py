import matplotlib.pyplot as plt
import numpy as np


class DataPloter(object):

    def plot(self, train_data, train_label, weight, error_rate):
        # print(train_data)
        plt.figure(num=1)
        plt.xlabel("x1")
        plt.ylabel("x2")

        # weight: np.mat()
        x = np.linspace(0, 99, 50)
        # print(weight[0, 0])
        # weight[0, 0]*x + weight[0, 1]*y + weight[0, 2] = 0
        y = (-weight[0, 2] - weight[0, 0] * x) / weight[0, 1]
        plt.plot(x, y, color='blue', linewidth=1.0, linestyle='--', label='wTx=0')

        i = 0

        for data in train_data:
            if train_label[i] > 0:
                plt.scatter(data[0], data[1], s=10, color='red')
            else:
                plt.scatter(data[0], data[1], s=10, color='black')
            i = i + 1

        plt.figure(num=2)
        plt.xlabel("iter times")
        plt.ylabel("error rate")
        plt.plot(error_rate, linewidth=0.5)
        plt.show()
