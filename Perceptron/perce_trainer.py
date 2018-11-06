import copy

import numpy as np

class PerceTrain(object):
    pass


def train(train_data, train_label, weight, eta):
    # print(train_data, train_label)
    copy_data = copy.deepcopy(train_data)
    i = 0
    for data in copy_data:
        if train_label[i] > 0:
            data.append(1.0)
        else:
            data[0] = -data[0]
            data[1] = -data[1]
            data.append(1.0)
        i = i + 1
        # print(data)

    # 权值初始
    for i in range(len(copy_data[0])):
        weight.append(0.1)
    # 2x~ 矩阵
    copy_data = np.mat(copy_data)

    # weight 1x3向量
    # print(weight)

    for data in copy_data:
        if np.matmul(data, np.transpose(weight)) <= 0:
            weight = weight + eta*data
    return weight
