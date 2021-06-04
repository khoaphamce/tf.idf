import json

def ArticleList(FileName):
    with open(f'{FileName}.json') as FileIn:
        JsonArr = json.load(FileIn)
    return JsonArr

def CreateDoc(ListOfArticle):
    count = 0
    for Content in ListOfArticle:
        count = count + 1
        DocFile = open(f'DocFile/Doc_{count}.txt', "x", encoding="utf-8")
        DocFile.close()
        if(len(Content['content']) >= 2):
            for i in range (0, len(Content['content'])):
                DocFile = open(f'DocFile/Doc_{count}.txt', "a", encoding="utf-8")
                DocFile.write(' ')
                DocFile.write(Content['content'][i])
                DocFile.close()  

def main():
    ContentArr = ArticleList('vnexpress')
    CreateDoc(ContentArr)                  

main()