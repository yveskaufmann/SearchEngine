__author__ = 's0544768'


class CrawlResult: 
    def __init__(self):
        self.content = [
            ("text, plapla", 1),
            ("waaaaaaaaaat", 2),
            ("text tex2", 3)
        ]

        self.urls = [
            "www.wat.de",
            "www.google.de"
        ]

        self.link_structure = [
            [2,1,4],
            [1,1,2],
            [3,4,5,6]
        ]




class Index: 
    def __init__(self):
        self.terms = {
            "token1": {1,2,3},
            "token2": {2,2,4},
            "waaaat": {5, 6, 7}
        }








