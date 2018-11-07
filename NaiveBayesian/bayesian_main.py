
from Bayesian import para_make, baye_cal

class BayMain(object):
    def __init__(self):
        # [ [u, sigma^2],[],[] ]
        self.w = []
        self.pw = [0.9, 0.1]
        self.loss = [[0, 1], [6, 0]]

        self.para_maker = para_make.ParaMaker()
        self.baye_caler = baye_cal.BayeCaler()

    def run(self, w1_file, w2_file, ok):
        w1 = list(self.para_maker.get_para(w1_file))
        w2 = list(self.para_maker.get_para(w2_file))
        self.w = [w1, w2]
        # p(w|x)
        post_p = self.baye_caler.calp(self.w, self.pw)

        cost = post_p
        if ok:
            #
            cost = self.baye_caler.calr(post_p, self.loss)
            # print(cost)

        min_one = self.baye_caler.minmize(cost)
        print("min risk:%s best choice:%s" % (min_one[0], min_one[1]))

if __name__ == '__main__':
    w1_file = 'w1.txt'
    w2_file = 'w2.txt'
    bay_obj = BayMain()
    bay_obj.run(w1_file, w2_file, 1)
