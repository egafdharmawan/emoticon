from nltk.tokenize import TweetTokenizer
from mtranslate import translate
import csv

def emoticon(text, *argv):
    
    tokens = TweetTokenizer().tokenize(text)
    result = []
    fileName = "emoticon/emoticon.csv"

    for w in tokens:
        with open(fileName, encoding="UTF-8") as myCSVfile:
            dataFromFile = csv.reader(myCSVfile, delimiter="\t")
        
            for row in dataFromFile:
                if w == row[0].strip():
                    w = row[1]
                    if argv:
                        lang = ([arg for arg in argv][0])
                        w = translate(w, lang)
            result.append(w)
            
    hasil = ' '.join(result)
    return hasil