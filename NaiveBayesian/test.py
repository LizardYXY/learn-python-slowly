import numpy as np
t = np.arange(6).reshape((3, 2))

tmp = 1
for i in range(len(t[0])):  # 对于特征个数
    for v in t[:, i]:  # 对于每个特征向量
        pass