import re
import urllib.parse

from bs4 import BeautifulSoup


root_url = "http://dept3.buaa.edu.cn/sylm/xygg.htm"
test_doc = """
<li>
<a href="xygg/28.htm" class="Next">下页</a>
<a href="xygg/1.htm" class="Next">尾页</a>
<a href="27.htm" class="Next">下页</a>
</li>
"""
data = {}
test_soup = BeautifulSoup(test_doc, 'html.parser', from_encoding='utf-8')
title_node = test_soup.find_all('a', href=re.compile(r"\d+.htm"))
print(title_node)