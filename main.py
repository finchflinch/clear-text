# aim: to format text copied from wikipedia and pdfs and format them to normal plain texts.

import argparse
import sys
import re

class Texts():
    def __init__(self, filename):
        self.filename = filename
        self.contents = ""
        self.pdf_op = ""
        self.wiki_op = ""

    def read_txt_file(self):
        fs = open("./"+self.filename, 'r')
        self.contents = fs.read()
        return

    #future scope
    def write_txt_file(self):
        pass

    def from_wiki(self):
        if len(self.contents) == 0:
            sys.exit('text file is empty. add some text.')
        else:
            # https://regexr.com great site to experiment RegEx
            self.wiki_op = re.sub(r"(\[.*\])+", "", self.contents)  #regEx for catching all the brackets and the text they hold inside and replace with ""
            print(self.wiki_op)

    def from_pdf(self):
        if len(self.contents) == 0:
            sys.exit('text file is empty. add some text.')
        else:
            counter = self.contents.count("\n")
            self.pdf_op = self.contents.replace('\n', ' ').replace('\r', ' ')
            print(self.pdf_op)

if __name__ == '__main__':

    # creating a parser
    parser = argparse.ArgumentParser(description="process some texts")

    parser.add_argument("-w","--wiki", 
    help="paste text from wikipedia, remove refs",
    action="store_true")

    parser.add_argument("-p","--pdf", 
    help="paste text from pdf, remove newlines",
    action="store_true")

    parser.add_argument("filename", type=str, help="type filename with extension")

    args = parser.parse_args()

    # create Texts object
    my_text = Texts(args.filename)
    # call the method to read file
    my_text.read_txt_file()
    if args.wiki:
        my_text.from_wiki()

    if args.pdf:
        my_text.from_pdf()

    else:
        print('wrong arguements')
