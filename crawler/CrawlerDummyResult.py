__author__ = 'pascal'
import os
from model.model import CrawlResult

def crawler_dummy_result():
    crawl_result = CrawlResult()
    crawl_result.content = [
        ("Given a character sequence and a defined document unit, \n"
         "tokenization is the task of chopping it up into pieces, called tokens, \n"
         "perhaps at the same time throwing away certain characters, \n"
         "such as punctuation.", 0),
        ("Token normalization is the process of canonicalizing \n"
         "tokens so that matches occur despite superficial \n"
         "differences in the character sequences of the tokens.", 1),
        ("For English, an alternative to making every token lowercase \n"
         "is to just make some tokens lowercase. The simplest heuristic \n"
         "is to convert to lowercase words at the beginning of a \n"
         "sentence and all words occurring in a title that is all \n"
         "uppercase or in which most or all words are capitalized.", 2),
        ("To gain the speed benefits of indexing at retrieval time, \n"
         "we have to build the index in advance. The major steps \n"
         "in this are: Collect the documents to be indexed, \n"
         "tokenize the text, turning each document into a \n"
         "list of tokens, do linguistic preprocessing, \n"
         "producing a list of normalized tokens, \n"
         "which are the indexing term.", 3),
        ("Index the documents that each term occurs in by \n"
         "creating an inverted index, consisting of a \n"
         "dictionary and postings.", 4),
        ("In text classification, we are given a description \n"
         "of a document and a fixed set of classes.", 5),
        ("Using a supervised learning method or learning algorithm, "
         "we wish to learn a classifier or classification function "
         "that maps documents to classes.", 6),
        ("s is a spam page. \n"
         "tokens \n"
         "stopwords \n"
         "index \n"
         "postings \n"
         "classification \n"
         "supervised \n"
         "tokens \n"
         "stopwords \n"
         "index \n"
         "postings \n"
         "classification \n"
         "supervised \n"
         "tokens \n"
         "stopwords \n"
         "index \n"
         "postings \n"
         "classification \n"
         "supervised \n"
         "tokens \n"
         "stopwords \n"
         "index \n"
         "postings \n"
         "classification \n"
         "supervised", 7)
    ]

    material_dir = os.path.join(os.getcwd(), os.pardir, "unterlagen/material")
    crawl_result.urls = [
        os.path.join(material_dir, "d01.html"),
        os.path.join(material_dir, "d02.html"),
        os.path.join(material_dir, "d03.html"),
        os.path.join(material_dir, "d04.html"),
        os.path.join(material_dir, "d05.html"),
        os.path.join(material_dir, "d06.html"),
        os.path.join(material_dir, "d07.html"),
        os.path.join(material_dir, "d08.html")
    ]
    crawl_result.link_structure = [
        [1, 2, 3],
        [2, 3, 0, 4],
        [3, 0, 1, 5],
        [0, 1, 2, 4],
        [3],
        [6],
        [5],
        []
    ]
    return crawl_result

