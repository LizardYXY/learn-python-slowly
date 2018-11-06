class TextOutputer(object):
    def __init__(self):
        self.datas = []

    def collect_data(self, data):
        if data is None:
            return
        self.datas.append(data)

    def output_text(self):
        fout = open('output.txt', 'w')

        for data in self.datas:
            fout.write("url:%s title:%s summary:%s" % (data['url'].encode('utf-8'),
                                                       data['title'].encode('utf-8'),
                                                       data['summary'].encode('utf-8')))
            fout.write("\n")
        fout.close()

