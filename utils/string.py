import os

class StringUtil:

    @staticmethod
    def header(title):
        """ return the title with a underline """
        underline = StringUtil.line(len(title), lineseg='¯')
        return os.linesep.join([ title, underline ])

    @staticmethod
    def line(len, lineseg='-'):
        return lineseg * len
