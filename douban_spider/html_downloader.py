import urllib.request


class HtmlDownloader(object):
    @staticmethod
    def download(new_url):
        if new_url is None:
            return None
        response = urllib.request.urlopen(new_url)
        print(response.getcode())
        if response.getcode() != 200:
            return None
        return response.read()
