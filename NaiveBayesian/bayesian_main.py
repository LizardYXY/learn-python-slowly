import numpy as np

from bayes import para_make, baye_cal, graph_plot, baye_judge

class BayMain(object):
    def __init__(self):
        # [ [u, sigma^2],[],[] ]
        self.w = []
        self.pw = [0.9, 0.1]
        self.loss = [[0, 1], [6, 0]]

        self.para_maker = para_make.ParaMaker()
        self.baye_caler = baye_cal.BayeCaler()
        self.baye_jugder = baye_judge.BayeJudger()
        self.graph_ploter = graph_plot.GraphPlot()

    def run(self, x, w1_file, w2_file):
        w1 = list(self.para_maker.get_para(w1_file))
        w2 = list(self.para_maker.get_para(w2_file))

        self.w = [[w1],
                  [w2]
                  ]

        post_p, prior_p = self.baye_caler.calp(x, self.w, self.pw)
        cost_p = self.baye_caler.calr(post_p, self.loss)

        ok = 1
        if ok:
            min_p, min_c = self.baye_jugder.minmize(cost_p, ok)
        else:
            min_p, min_c = self.baye_jugder.minmize(post_p, ok)

        self.graph_ploter.plot_p(x, len(self.w[0]), prior_p, post_p, cost_p)

class Bay2Main(object):
    def __init__(self):
        self.baye_jugder = baye_judge.BayeJudger()
        self.baye_caler = baye_cal.BayeCaler()
        self.graph_ploter = graph_plot.GraphPlot()
        self.pw = [0.2, 0.3, 0.5]
        self.loss = [
            [0, 1, 2],
            [1000, 0, 3],
            [1000, 1, 0]
        ]


    def run(self, para, x):
        #
        post_p, prior_p = self.baye_caler.calp(x, para, self.pw)
        cost_p = self.baye_caler.calr(post_p, self.loss)

        ok = 1
        if ok:
            min_p, min_c = self.baye_jugder.minmize(cost_p, ok)
        else:
            min_p, min_c = self.baye_jugder.minmize(post_p, ok)

        # self.graph_ploter.plot_p(x, len(para[0]), prior_p, post_p, cost_p)
        self.graph_ploter.plot_m(x, len(para[0]), para, min_c)
        # print(min_c)


if __name__ == '__main__':
    two_dimension = 2
    if two_dimension == 2:
        para = [[[1.1, 0.5], [1.2, 0.5]],
                [[1.5, 0.6], [-1.5, 0.7]],
                [[-1.4, 0.3], [-1.2, 0.5]]
                ]
        x = np.arange(-4, 4, 0.1)
        bay2_obj = Bay2Main()
        bay2_obj.run(para, x)
    else:
        w1_file = 'w1.txt'
        w2_file = 'w2.txt'
        x = np.arange(-5, 5, 0.1)
        y = 1
        bay_obj = BayMain()
        bay_obj.run(x, w1_file, w2_file)
