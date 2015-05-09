import os

class Pages:
    data = []
    @staticmethod
    def get():
        return Pages.data

class Page:

    def __init__(self):
        self.title = ""
        self.content = ""
        self.url = ""
        self.out_links = []

    def __str__(self):
        """
        Create the required string representation of a 
        page. For a example of a possible output please
        see docs/results/docs.txt.
        """

        headline = '-' * 75
        page_str = os.linesep.join([
            headline,
            self.title,
            headline,
            self.content 
        ])

        return page_str

class Index: 
    def __init__(self):
        self.__terms = {}
        
    def register_Token(self, token, document):
        """
        Register a Token which was found in a specific document.
        """

        term = self.__get_term_if_exists_or_create_one(token)
        if document not in term['postings']: 
            term['postings'][document] = {'times': 0}
            term['frequence'] += 1    
        
        term['postings'][document]['times'] += 1 

    def __get_term_if_exists_or_create_one(self, token):
        """
        Return registered token or create a new one 
        if the specified token isn't already registered
        """

        if token in self.__terms:
            return self.__terms[token]
        
        self.__terms[token] = {
            'postings': dict(),
            'score': 0,
            'frequence': 0 
        } 

        return self.__terms[token]

    def __str__(self):
        """
        Create the required string representation of an 
        index for more details see docs/results/index.txt

        For example a possible output could be:

        index.txt
        ¯¯¯¯¯¯¯¯¯
        (advance, df:1) -> [('d04', 1)]
        (algorithm, df:1) -> [('d07', 1)]
        (documents, df:3) -> [('d04', 1), ('d07', 1), ('d05', 1)]
        ...
        """

        output = []
        
        title = 'index.txt'
        output.append(title)
        output.append('¯' * len(title))

        for token, term in sorted(self.__terms.items()):

            list_of_postings = [self.__render_postings(id, doc) for id, doc in term['postings'].items()]
            list_of_postings = ', '.join(list_of_postings) 

            newLine = "({0}, df:{1}) -> [{2}]".format(token, term['frequence'], list_of_postings)
            output.append(newLine)

        return os.linesep.join(output)

    def __render_postings(self, id, doc):
        return "('{0}', {1})".format(id, doc['times'])








        















