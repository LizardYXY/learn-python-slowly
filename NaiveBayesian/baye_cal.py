from scipy.stats import norm
import numpy as np

class BayeCaler(object):

    def calp(self, x, w, pw):
        '''
        for two-dimension
        :param x: input of the main (np.array)
        :param w: parameter of P(X|w)
        :param pw: P(w)
        :return: post P(w|X) and prior P(X|w)  类别数 x (取样点数 ^ 特征数)
        '''
        # print(p(w))
        # 计算先验概率
        prior_p = []
        # para [p(x1|wi),p(x2|wi)...,p(xj|wi)]
        for para in w:
            t = []
            for p in para:
                t.append(norm.pdf(x, p[0], p[1]))
            prior_p.append(t)
        prior_p = np.array(prior_p)
        # print(prior_p)
        r_p = []
        for p in prior_p:
            tmp = 1
            for i in range(len(p)):
                if i == 0:
                    tmp = tmp * np.mat(p[i])
                else:
                    tmp = np.matmul(tmp, np.mat(p[i]))
                tmp = tmp.reshape(tmp.size, 1)
            r_p.append(tmp)
        temp_p = np.array(r_p).reshape(len(r_p), r_p[0].size)
        # 3 x 64
        # temp_p 才是处理后返回的先验概率

        # sum[p(x1|w1)p(x2|w1)...,p(xj|w1)p(w1) + ...... + p(x1|wi)p(x2|wi)...,p(xj|wi)p(wi)]
        sum_p = []
        # print(sum_p)
        # print(temp_p)
        for temp in temp_p:
            # print(temp)
            temp_sum = 0
            for temp_ele in temp:
                temp_sum = temp_sum + temp_ele
            sum_p.append(temp_sum)
        sum_p = np.array(sum_p)
        sum_p = sum_p.reshape(len(sum_p), 1)
        # print(sum_p)

        # p(w|x)
        # Post p
        post_p = temp_p/sum_p
        # print(post_p)

        return post_p, temp_p

    def calr(self, post_p, loss):
        '''
        use np
        :param post_p:
        :param loss: loss of error judge
        :return: 类别数 x (取样点数 ^ 特征数)
        '''
        # print(post_p)
        loss = np.array(loss)
        price = np.matmul(loss, post_p)
        # 3x64
        # print(price)
        # print(price[0])
        return price



