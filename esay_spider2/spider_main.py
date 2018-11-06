from douban_spider import url_manager, html_downloader, html_parser, text_outputer, html_outputer


class SpiderMain(object):
    def __init__(self):
        #
        self.urls = url_manager.UrlManager()
        self.downloader = html_downloader.HtmlDownLoader()
        self.parser = html_parser.HtmlParser()
        # self.outputer = text_outputer.TextOutputer()
        self.outputer = html_outputer.HtmlOutputer()

    def crawl(self, root_url):
        #
        count = 0

        self.urls.add_new_url(root_url)
        while self.urls.has_new_url():
            try:
                print()
                new_url = self.urls.get_new_url()
                print('Crawl %d:%s' % (count, new_url))
                html_cont = self.downloader.download(new_url)
                new_urls, new_data = self.parser.parse(new_url, html_cont)
                self.urls.add_new_urls(new_urls)
                self.outputer.collect_data(new_data)

                count = count + 1
                if count >= 1000:
                    break
            except:
                print('fail')
        self.outputer.output_text()

if __name__ == '__main__':
    root_url = "https://movie.douban.com/subject/26425063/"
    obj_spider = SpiderMain()
    obj_spider.crawl(root_url)
