
class HtmlOutputer(object):

    def __init__(self):
        self.data = []

    def collect_data(self, new_data):
        self.data.append(new_data)

    def output_html(self):
        file = open('douban.txt', 'w', encoding='utf-8')

        for arr in self.data:
            for item in arr:
                file.write(item['index'] + '  ' + item['title'])
                file.write('\n')

        file.close()
