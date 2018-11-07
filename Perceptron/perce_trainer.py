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

    # 2x~ 矩阵
    copy_data = np.mat(copy_data)

    # weight 1x3向量
    # print(weight)

    error_rate = []
    for data in copy_data:
        if np.matmul(data, np.transpose(weight)) <= 0:
            weight = weight + eta*data

        i = 0
        error_time = 0
        for d in train_data:
            if (-weight[0, 2] - weight[0, 0] * d[0]) / weight[0, 1] > d[1] and train_label[i] > 0:
                error_time = error_time + 1
            if (-weight[0, 2] - weight[0, 0] * d[0]) / weight[0, 1] < d[1] and train_label[i] <= 0:
                error_time = error_time + 1
            i = i + 1
        rate = 1 - error_time / len(copy_data)

        error_rate.append(rate)

    return weight, error_rate
