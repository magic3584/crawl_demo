
from bs4 import BeautifulSoup


class HtmlParser(object):

    @staticmethod
    def parse_data(html_cont):
        soup = BeautifulSoup(html_cont, 'html.parser', from_encoding='utf-8')

        data = []

        for li in soup.find('ol', class_='grid_view').findAll('li'):
            index = li.find('em').get_text()
            title = li.find(class_='title').get_text()
            picUrl = li.find('img').get('src')
            dic = {'index': index, 'title': title, 'pic': picUrl}
            data.append(dic)
        return data























