#!/usr/bin/env python
# encoding: utf-8
import sys
import gzip
import chardet
# HTML Processing tools:
import justext
from bs4 import BeautifulSoup

'''
Author: Joao Palotti <joaopalotti@gmail.com>
'''

class byeHTML:

    def __init__(self, htmlText, isInputFile=False, preprocesshtml="bs4", forcePeriod=False):
        """
            byeHTML(htmlText, isInputFile=False, preprocesshtml = "justext", forcePeriod = False).

            Case you want to extract a content from a file, use isInputFile=True and htmlText is the
            path to a document.

            The current available options for HTML preprocessor are:

                - justext ---- recommended.
                - bs4 (beautifulsoup4) ---- might result in encoding problems

            In case forcePeriod is active, a period mark will be added to every sentence
            extracted by the preprocessing html method employed.
        """
        try:
            if isInputFile:
                htmlText = self.__extract_content(htmlText)

            self.text = self.preprocess_html(htmlText, preprocesshtml, forcePeriod)

        except Exception as e:
            print(("Error %s -- %s" % (type(e), e)))
            self.text = ""

    def get_text(self):
        return self.text

    def repr(self):
        return self.text

    def __find_encoding(self, doc_full_path):
        # http://chardet.readthedocs.io/en/latest/usage.html
        # This method uses the traditional chardet to find out the encoding used in a file
        if doc_full_path.endswith(".gz"):
            f = gzip.open(doc_full_path, mode="rb")
        else:
            f = open(doc_full_path, mode="rb")

        rawdata = f.read()
        return chardet.detect(rawdata)["encoding"]

    def __get_content(self, filename):
        encoding = self.__find_encoding(filename)

        if filename.endswith(".gz"):
            with gzip.open(filename, mode="rt", encoding=encoding, errors="surrogateescape") as f:
                content = str(f.read()) # Explicitly convert from bytes to str
        else:
            with open(filename, encoding=encoding, errors="surrogateescape", mode="r") as f:
                content = f.read()
        return content


    def preprocess_html(self, text, preprocessor, forcePeriod):
        """
            Options:
            preprocessor: justext, bs4, None
            continuous: True, False.

            Use continuous to set if you want to force end of sentences.
        """

        if not preprocessor or type(text) != str or len(text.strip()) == 0:
            return text

        elif preprocessor == "bs4":
            soup = BeautifulSoup(text, "html.parser")
            # This html text has no body!
            if soup.find("body") is None:
                return text

            tags_to_remove = ["script"]
            for tag in tags_to_remove:
                for x in soup.body(tag):
                    x.decompose()
            if forcePeriod:
                return soup.body.get_text().replace("\n", ".\n")
            else:
                return soup.body.get_text()

        elif preprocessor == "justext":
            paragraphs = justext.justext(text, justext.get_stoplist('English'))
            text = "\n"
            for paragraph in paragraphs:
                if not paragraph.is_boilerplate: # and not paragraph.is_header:
                    if forcePeriod:
                        text = text + paragraph.text + ".\n"
                    else:
                        text = text + paragraph.text + "\n"
            return text

        # At the moment that this code was updated, boilerpipe was not available for download via pip.
        #elif preprocessor == "boilerpipe":
        #    extractor = Extractor(extractor='ArticleExtractor', html=content)
        #    return extractor.getText()

        else:
            print("PRE PROCESSING OPTION %s NOT FOUND. IGNORING PRE PROCESSING.")
            return text


if __name__ == "__main__":
    if len(sys.argv) == 1:
        print("USAGE: python byeHTML.py <TEXT>")
        sys.exit(0)

    text = ' '.join(sys.argv[1:])
    bye = byeHTML(text)
    print(bye.get_text())
