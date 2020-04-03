from nltk.tokenize import TweetTokenizer
from mtranslate import translate
import csv

# Change Emoticon to text
def emoticon(text, *argv):
    
    tokens = TweetTokenizer().tokenize(text)
    result = []
    fileName = "emoticon/emoticons.csv"
    
    for w in tokens:
        with open(fileName, encoding="UTF-8") as myCSVfile:
            dataFromFile = csv.reader(myCSVfile, delimiter="\t")
        
            for row in dataFromFile:
                if w == row[1].strip():
                    w = row[2]
                    if argv:
                        lang = ([arg for arg in argv][0])
                        w = translate(w, lang)
            result.append(w)
            
    final = ' '.join(result)
    return final

# Change text to emoticon
def demoticon(text):
    
    tokens = TweetTokenizer().tokenize(text)
    result = []
    fileName = "emoticon/emoticons.csv"
    
    for w in tokens:
        with open(fileName, encoding="UTF-8") as myCSVfile:
            dataFromFile = csv.reader(myCSVfile, delimiter="\t")
            c = translate(w.capitalize(), 'en')
            for row in dataFromFile:
                if c == row[2].strip():
                    w = row[1]
            result.append(w)
            
    final = ' '.join(result)
    return final