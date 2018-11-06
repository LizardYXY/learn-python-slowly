import re
import urllib.request
from bs4 import BeautifulSoup

class HtmlParser(object):

    def parse(self, page_url, html_cont):
        if page_url is None or html_cont is None:
            return

        soup = BeautifulSoup(html_cont, 'html.parser', from_encoding='utf-8')
        new_urls = self._get_new_urls(page_url, soup)
        new_data = self._get_new_data(page_url, soup)

        return new_urls, new_data

    def _get_new_data(self, page_url, soup):
        res_data = {}
        # <span property="v:itemreviewed">无双 無雙</span>
        title_node = soup.find('span', property='v:itemreviewed')
        # print(title_node)
        res_data['title'] = title_node.get_text()
        #<span property="v:summary" class="">
        #                        　　《无双》讲述了以代号“画家”（周润发 饰）为首的犯罪团伙，掌握了制造伪钞技术，难辨真伪，并在全球进行交易获取利益，引起警方高度重视。然而“画家”和其他成员的身份一直成谜，警方的破案进度遭受到了前所未有的挑战。在关键时刻，擅长绘画的李问（郭富城 饰）打开了破案的突破口，而“画家”的真实身份却让众人意想不到……
        #                </span>
        summary_node = soup.find('span', property='v:summary')
        # print(summary_node)
        res_data['summary'] = summary_node.get_text()
        res_data['url'] = page_url

        return res_data

    def _get_new_urls(self, page_url, soup):
        new_urls = set()
        links = soup.find_all('a', href=re.compile(r"https://movie.douban.com/subject/\d+/\?from=subject-page"))
        for link in links:
            new_url = link['href']
            new_urls.add(new_url)

        return new_urls


