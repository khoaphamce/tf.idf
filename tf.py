import os
import time
from math import log2

start_time = time.time()

CountList = {}

def Print2DArray(Array):
    for i in range(0,len(Array)):
        for j in range(0,len(Array[i])):
            print(Array[i][j], end = '')
            print(' ', end = '')
        print('')

# DocNo = 1
WordNumber = 0
AvoidChar = ['và', 'thì', 'với', 'nhưng', 'do', 'tại', 'ngày', 'bộ', 'bởi', 'thường', 'người', 'các', 'những',
             'mà', 'có', 'được', 'không', 'trong', 'rất', 'là', 'của', 'từ', 'cho', 'một', 'đến', 'tới', 'anh',
             'mấy', 'ông', 'em', 'tôi', 'cô', 'dì', 'chú', 'bác', 'con'
            ]
# AvoidChar = []

def WordDict(InputString, WordList, WordNo):
    Word = ''
    for i in range(0, len(InputString)):
        AsciiNumber = ord(InputString[i])
        if (AsciiNumber >= 0 and AsciiNumber <= 64) or (AsciiNumber >= 91 and AsciiNumber <= 96) or (AsciiNumber >= 123 and AsciiNumber <= 127):
            if (len(Word) > 1) and (Word not in AvoidChar):
                if Word not in WordList:
                    WordDictListReverse.append(Word)
                    WordList[Word] = WordNo
                    WordNo = WordNo + 1
            Word = ''
        else:
            Word = Word + InputString[i]
    return WordList, WordNo


# MAKE DICTIONARY OF WORDS
WordDictListReverse = []
WordDictList = {}
WordFreq = []
TempFrequency = []

for DocName in os.listdir('LowerDocFile'):
        File = open(f'LowerDocFile/{DocName}', 'r', encoding = 'utf8')
        DocString = File.read()
        WordDictList, WordNumber = WordDict(DocString, WordDictList, WordNumber)
        File.close()

# MAKE WORDS FREQUENCY (AND PART OF TIME ITS APPEARANCE IN DOCUMENT)
SetupAppearCheck = False
AppearCheck = []
TimeAppear = []
for DocName in os.listdir('LowerDocFile'):
    TempFrequency = []
    for i in range(0, len(WordDictList)):
        TempFrequency.append(0)
        if SetupAppearCheck == False:
            TimeAppear.append(0)
            AppearCheck.append(False)
    SetupAppearCheck = True

    WordFreq.append(TempFrequency)


def TermFrequency(InputString, DocNo):
    Queue = []
    Word = ''
    Max = 0
    MaxWord = ''
    count = 0
    for i in range(0, len(InputString)):
        AsciiNumber = ord(InputString[i])
        if (AsciiNumber >= 0 and AsciiNumber <= 64) or (AsciiNumber >= 91 and AsciiNumber <= 96) or (AsciiNumber >= 123 and AsciiNumber <= 127):

            if (len(Word) > 1) and (Word not in AvoidChar):
                Index = WordDictList[Word]
                count = int(WordFreq[DocNo][Index]) + 1
                WordFreq[DocNo][Index] = count

                if WordFreq[DocNo][Index] > Max:
                    Max = WordFreq[DocNo][Index]
                    MaxWord = Word

                if AppearCheck[Index] == False:
                    TimeAppear[Index] = TimeAppear[Index] + 1
                    AppearCheck[Index] = True
                    Queue.append(Index)

            Word = ''
        else:
            Word = Word + InputString[i]

    for i in range(0, len(WordFreq[DocNo])):
        if (WordFreq[DocNo][i] > 0):
            WordFreq[DocNo][i] = WordFreq[DocNo][i] / Max
        else:
            WordFreq[DocNo][i] = 0
    return Queue


def ResetAppearCheck(QueueCheck):
    while len(QueueCheck) > 0:
        AppearCheck[QueueCheck[0]] = False
        QueueCheck.pop(0)


DocNumber = 0
for DocName in os.listdir('LowerDocFile'):
    File = open(f'LowerDocFile/{DocName}', 'r', encoding = 'utf8')
    DocString = File.read()
    QueueMain = TermFrequency(DocString, DocNumber)
    ResetAppearCheck(QueueMain)
    DocNumber = DocNumber + 1
    File.close() 



# TF.IDF

def MaxElements(N):
    Visited = [] 
    ResultList = ['','',''] 
    for z in range(0, N):  
        MaxDef = -1
        for j in range(0, len(TfidfVector[i])):
            LargerCheck = TfidfVector[i][j] > MaxDef
            if LargerCheck == True and TfidfVector[i][j] not in Visited: 
                MaxDef = TfidfVector[i][j]
                ResultList[z] = WordDictListReverse[j] 
        Visited.append(MaxDef)
    return ResultList 

TfidfVector = []
TempVector = []
NumberOfDoc = len(os.listdir('LowerDocFile'))
MaxOfDoc = [0,0,0]
WordMaxOfDoc = ['','','']
Result = 0

for i in range(0,NumberOfDoc):
    ResultWordMax = ''
    Max = -1
    TempVector = []
    MaxOfDoc = [-1,-1,-1]
    WordMaxOfDoc = ['','','']
    for Word in WordDictList:
        Index = WordDictList[Word]
        Idf = log2(NumberOfDoc/TimeAppear[Index])
        Result = WordFreq[i][Index]*Idf
        TempVector.append(WordFreq[i][Index]*Idf)

    TfidfVector.append(TempVector)

    # FIND 3 HIGHGEST
    Visited = [] 
    ResultList = ['','',''] 
    for z in range(0, 3):  
        MaxDef = -1
        for j in range(0, len(TfidfVector[i])):
            if TfidfVector[i][j] > MaxDef and j not in Visited: 
                MaxDef = TfidfVector[i][j]
                pos = j
                ResultList[z] = WordDictListReverse[j] 
        Visited.append(pos)
    WordMaxOfDoc = ResultList

    print(os.listdir('LowerDocFile')[i],': ', end = '')
    for num in range(0, len(WordMaxOfDoc)):
        print(WordMaxOfDoc[num], ' ', end = '')
    print('')

print('')
print("--- %s seconds ---" % (time.time() - start_time))
print('')

