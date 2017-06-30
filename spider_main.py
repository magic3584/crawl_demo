from douban_spider import html_downloader, html_parser, html_outputer
from bs4 import BeautifulSoup
class SpiderMain(object):
    def __init__(self):
        self.downloader = html_downloader.HtmlDownloader()
        self.parser = html_parser.HtmlParser()
        self.outputer = html_outputer.HtmlOutputer()

    def crawl(self, new_url):
        html_cont = self.downloader.download(new_url)
        new_data = self.parser.parse_data(html_cont)
        self.outputer.collect_data(new_data)


if __name__ == "__main__":
    obj_spider = SpiderMain()
    for i in range(0, 10):
        url = 'https://movie.douban.com/top250?start=%d&filter=' % (i * 25)
        obj_spider.crawl(url)
        print('index %d, url: %s' % (i, url))
    obj_spider.outputer.output_html()
