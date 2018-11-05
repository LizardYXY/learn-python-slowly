class HtmlOutputer(object):
    def __init__(self):
        self.datas = []

    def collect_data(self, data):
        if data is None:
            return
        self.datas.append(data)

    def output_html(self):
        fout = open('output.html', 'w', encoding='utf-8')

        fout.write("<html>")
        fout.write("<body>")
        fout.write("<table>")

        for data in self.datas:
            fout.write("<str>")
            fout.write("<td>%s</td>" % data['url'].encode('utf-8'))
            for item in data['title']:
                fout.write("<td>%s</td>" % item.encode('utf-8'))
            fout.write("</str>")
        fout.write("</table>")
        fout.write("</body>")
        fout.write("</html>")

        fout.close()
