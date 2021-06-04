import os

def LowerDoc():
    for DocName in os.listdir('DocFile'):
        File = open(f'DocFile/{DocName}', 'r', encoding = 'utf8')
        DocString = File.read()
        File.close()
        LowerFile = open(f'LowerDocFile/{DocName}', 'x', encoding = 'utf8')
        LowerFile.write(DocString.lower())
        File.close()

LowerDoc()