import random

class DataProvide(object):

    def provide(self, train_text, ok):
        if ok:
            fout = open(train_text, 'w')
            for i in range(500):
                x = random.uniform(0.0, 99.0)
                y = random.uniform(0.0, 99.0)
                # line y = 1.1x + 1.2
                fout.write(str(x) + ' ')
                fout.write(str(y) + ' ')
                if 1.1*x + 1.2 < y + 2:
                    fout.write(str(0) + '\n')
                else:
                    fout.write(str(1) + '\n')
            fout.close()
