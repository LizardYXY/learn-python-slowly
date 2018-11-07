from scipy.stats import norm
import numpy as np
from math import sqrt

class BayeCaler(object):
    def __init__(self):
        # conditional P
        self.condp = []

        self.tempp = []
        # posterior P
        self.postp = []

    def calp(self, w, pw):
        # print(pw)
        for para in w:
            # print(para)
            # p(x|w)
            self.condp.append(norm.pdf(para[0], sqrt(para[1])))
        i = 0
        for cp in self.condp:
            # print(cp)
            # p(x|w)p(w)
            self.tempp.append(cp * pw[i])
            i = i + 1
        # sum(p(x|w)p(w))
        sump = 0
        for tp in self.tempp:
            sump = sump + tp

        # p(w|x)
        for tp in self.tempp:
            self.postp.append(tp/sump)

        return self.postp

    def calr(self, post_p, loss):
        return np.matmul(loss, np.transpose(post_p))

    def minmize(self, cost):
        min_one = cost[0]
        min_class = 0
        i = 0
        for c in cost:
            if c < min_one:
                min_one = c
                min_class = i
            i = i + 1
        return [min_one, min_class]

