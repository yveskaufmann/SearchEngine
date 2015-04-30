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


class Page:

    def __init__(self):
        self.title = ""
        self.content = ""
        self.url = ""
        self.out_links = []


import os

class Index: 
    def __init__(self):

        self.terms = {}

    def add_Token_from_docment(self, token, document):
        """
            Register a Token which was found in a specific document.

        """
        term = self.__get_term_if_not_exists_create_one(token)
        if document not in term['occurences']: 
            term['occurences'][document] = {'times' : 0}
            term['frequence'] += 1    
        
        term['occurences'][document]['times'] += 1 

    
    def __get_term_if_not_exists_create_one(self, token):
        
        """
            Return registered token or create a new one 
            if the specified token isn't already registered
        """
        
        if token in self.terms:
            return self.terms[token]
        

        self.terms[token] = {
            'occurences': dict(),
            'score' : 0,
            'frequence' : 0
        } 

        return self.terms[token]

    def __str__(self):

        """
            Create the required string representation of an 
            index for more details see unterlagen/results/index.txt
        """
        
        output = []
        # (advance, df:1) -> [('d04', 1)]
        for token, term in self.terms.items():

            list_of_occurences = [ "('{0}', {1})".format(doc, doc_data['times']) for doc, doc_data in term['occurences'].items() ]

            newLine = "({0}, df:{1}) -> [{2}]".format(token, term['frequence'], ', '.join(list_of_occurences) )
            output.append(newLine)

        return os.linesep.join(output)






        















