import os
import urllib

class HtmlOutputer(object):

    def __init__(self):
        self.data = []

    def collect_data(self, new_data):
        self.data.append(new_data)

    def output(self):
        file = open('douban.txt', 'w', encoding='utf-8')

        for arr in self.data:
            for item in arr:
                self.save_text(file, item)
                self.save_images(item)

        file.close()

        print('Done~')


    def save_text(self, file, item):

        file.write(item['index'] + '  ' + item['title'])
        file.write('\n')

    def save_images(self, item):
        if os.path.exists('pics') == False:
            print('mkdir pics')
            os.mkdir('pics')

        filename = item['index'] + "-" + item['title'] + os.path.splitext(item['pic'])[1]
        resource = urllib.request.urlopen(item['pic'])
        data = open('pics/%s' % filename, 'wb')
        data.write(resource.read())
        data.close()
        print('Saved %s' % filename)

