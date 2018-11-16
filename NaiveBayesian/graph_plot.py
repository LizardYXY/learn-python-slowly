import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import axes3d
import numpy as np


class GraphPlot(object):

    def plot_p(self, x, d, post_p, prior_p, cost_p):
        '''
        原来理解错了，prior_p是条件概率
        :param x: 取样点数
        :param post_p: 类别数 x (取样点数 ^ 特征数)
        :param prior_p: 类别数 x (取样点数 ^ 特征数)
        :param cost_p: 类别数 x (取样点数 ^ 特征数)
        :return:
        '''
        if d == 1:
            plt.figure(num=1)
            plt.ylabel('conditional probability')
            i = 0
            for prior_ele in prior_p:
                i = i + 1
                plt.plot(x, prior_ele, linewidth=1, label='$P(X|w' + str(i) + ')$')
                plt.legend()

            plt.figure(num=2)
            plt.ylabel('post probability')
            i = 0
            for post_ele in post_p:
                i = i + 1
                plt.plot(x, post_ele, linewidth=1, label='$P(w' + str(i) + "|X)$")
                plt.legend()

            plt.figure(num=3)
            plt.ylabel('cost')
            i = 0
            for cost_ele in cost_p:
                i = i + 1
                plt.plot(x, cost_ele, linewidth=1, label='$R(a' + str(i) + "|X)$")
                plt.legend()

            plt.show()

        elif d == 2:
            fig = plt.figure(num=1)

            ax = fig.add_subplot(111, projection='3d')
            X, Y = np.meshgrid(x, x)
            dm = int(pow(prior_p[0].size, 1/d))
            rm = [len(prior_p)]
            for j in range(d):
                rm.append(dm)
            prior_p = prior_p.reshape(rm)
            for prior_ele in prior_p:
                # 画图代码
                ax.plot_surface(X, Y, prior_ele, rstride=2, cstride=2, alpha=0.5)
            ax.set_xlabel('X1')
            ax.set_ylabel('X2')
            plt.show()

            fig = plt.figure(num=2)
            ax = fig.add_subplot(111, projection='3d')
            X, Y = np.meshgrid(x, x)
            dm = int(pow(post_p[0].size, 1 / d))
            rm = [len(post_p)]
            for j in range(d):
                rm.append(dm)
            post_p = post_p.reshape(rm)
            for post_ele in post_p:
                # 画图代码
                ax.plot_surface(X, Y, post_ele, rstride=2, cstride=2, alpha=0.5)
            ax.set_xlabel('X1')
            ax.set_ylabel('X2')
            plt.show()

            X, Y = np.meshgrid(x, x)
            dm = int(pow(cost_p[0].size, 1 / d))
            rm = [len(cost_p)]
            for j in range(d):
                rm.append(dm)
            cost_p = cost_p.reshape(rm)
            for cost_ele in cost_p:
                # 画图代码
                fig = plt.figure()
                ax = fig.add_subplot(111, projection='3d')
                ax.plot_surface(X, Y, cost_ele, rstride=1, cstride=1, alpha=0.8)
                ax.set_xlabel('X1')
                ax.set_ylabel('X2')
                plt.show()

    def plot_m(self, x, d, para, min_c):
        dm = int(pow(len(min_c), 1 / d))
        rm = []
        for j in range(d):
            rm.append(dm)
        min_c = min_c.reshape(rm)
        X, Y = np.meshgrid(x, x)
        plt.figure(num=1)
        plt.contourf(X, Y, min_c, 10, alpha=0.6)

        data = []
        # para [p(x1|wi),p(x2|wi)...,p(xj|wi)]
        for para in para:
            for p in para:
                data.append(np.random.normal(p[0], p[1], 20))
        for i in range(int(len(data)/2)):
            plt.scatter(data[2*i+1], data[2*i], label='1')

        plt.ylabel('X2')
        plt.xlabel('X1')

        plt.show()
