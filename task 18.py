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

parser = Parser('C:\\Users\\chill\\Documents\\Stuff on SSD\\Coding Projects\\Python\\ИТМО\\Технологии прогр\\11.11\\task 18.11\\text.txt')
parser.parse()
print(parser.filename, parser.date)
print(parser.text)