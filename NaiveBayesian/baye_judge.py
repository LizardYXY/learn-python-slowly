import numpy as np


class BayeJudger(object):
    def minmize(self, p, ok):
        '''
        choose
        :param ok: 1 cost 0 post
        :param p: 类别数 x (取样点数 ^ 特征数)
        :return: 取样点数维的list
        '''
        min_p = []
        min_c = []
        if ok == 1:  # 最小代价
            for i in range(len(p[0])):
                # print(p[:, i])
                min_p_ele = min(p[:, i])
                min_c_ele = np.argmin(p[:, i])
                # print(min_c_ele)
                min_p.append(min_p_ele)
                min_c.append(min_c_ele)
        else:
            for i in range(len(p[0])):
                # print(p[:, i])
                min_p_ele = max(p[:, i])
                min_c_ele = np.argmax(p[:, i])
                # print(min_c_ele)
                min_p.append(min_p_ele)
                min_c.append(min_c_ele)

        # print(min_p)
        # print(min_c)

        return np.array(min_p), np.array(min_c)
