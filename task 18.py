from datetime import date

class Parser:
    def __init__(self, filename):
        Filename.saveFilename(self, filename)
        dateOfParse.saveDateOfParse(self)
    
    def parse(self):
        with open(self.filename) as f:
            self.text = ''.join(f.readlines())

class Filename(Parser):
    def __init__(self, filename):
        super().__init__(filename)

    def saveFilename(self, filename):
        self.filename = filename

class dateOfParse(Parser):
    def __init__(self, filename):
        super().__init__(filename)
    
    def saveDateOfParse(self):
        self.date = date.today()

class final(Filename, dateOfParse):
    pass

parser = Parser('text.txt')
parser.parse()
print(parser.filename, parser.date)
print(parser.text)