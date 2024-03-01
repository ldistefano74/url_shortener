import string
from collections import Counter


class Storage:
    """Core class that may abstract from persistence"""

    __URLS = {}

    def process_url(self, url):
        next_id = self._get_next_id()

        self.__URLS[next_id] = Site(url, "")
        return next_id

    def get_statistics(self):
        stats = Counter(url.url for url in self.__URLS.values())
        return sorted(stats.items(), key=lambda x: x[1], reverse=True)[:100]

    def get_redirect_url(self, id):
        ret = None
        site = self.__URLS.get(id)
        if site:
            print("Redirect: ", site.url)
            ret = site.url

        return ret

    def _get_next_id(self):
        if len(self.__URLS):
            last = max(self.__URLS.keys())
        else:
            last = ""
        new = ""

        if not last or last[-1] == string.ascii_lowercase[-1]:
            new = last + string.ascii_lowercase[0]
        else:
            pos = string.ascii_lowercase.find(last[-1])
            new = last[:-1] + string.ascii_lowercase[pos + 1]

        return new


class Site:
    url: str = None
    title: ""

    def __init__(self, url, title):
        self.url = url
        self.title = title

