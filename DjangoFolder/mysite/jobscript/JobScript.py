import string
import nltk
import string
import re

from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
tokenizer = nltk.data.load('tokenizers/punkt/PY3/english.pickle')


#J48 pruned tree

#------------------

#Home = 0
#|   TX = 0
#|   |   passionate = 0
#|   |   |   secure = 0
#|   |   |   |   growing = 0
#|   |   |   |   |   participate = 0: 0 (8654.0/506.0)
#|   |   |   |   |   participate = 1
#|   |   |   |   |   |   000 = 0: 0 (312.0/6.0)
#|   |   |   |   |   |   000 = 1
#|   |   |   |   |   |   |   – = 0: 1 (63.0/11.0)
#|   |   |   |   |   |   |   – = 1: 0 (4.0)
#|   |   |   |   growing = 1: 0 (2983.0/32.0)
#|   |   |   secure = 1: 0 (1569.0/2.0)
#|   |   passionate = 1: 0 (2650.0/5.0)
#|   TX = 1
#|   |   000 = 0: 0 (911.0/67.0)
#|   |   000 = 1
#|   |   |   fun = 0
#|   |   |   |   digital = 0
#|   |   |   |   |   – = 0
#|   |   |   |   |   |   entry = 0: 1 (81.0/10.0)
#|   |   |   |   |   |   entry = 1
#|   |   |   |   |   |   |   web = 0: 0 (2.0)
#|   |   |   |   |   |   |   web = 1: 1 (2.0)
#|   |   |   |   |   – = 1: 0 (19.0/2.0)
#|   |   |   |   digital = 1: 0 (3.0)
#|   |   |   fun = 1: 0 (7.0)
#Home = 1
#|   entry = 0: 0 (521.0/52.0)
#|   entry = 1
#|   |   fun = 0
#|   |   |   team = 0: 1 (67.0)
#|   |   |   team = 1: 0 (18.0/2.0)
#|   |   fun = 1: 0 (14.0)JJ

class JobScriptAnalyzer:



    def loadText(text):

        return (text)











    def main(self,text):

        def removePunct(text):
            translator = str.maketrans('', '', string.punctuation)
            return text.translate(translator)

        def remove_whitespace(text):
            return " ".join(text.split())

        def remove_stopwords(text):
            stop_words = set(stopwords.words("english"))
            word_tokens = word_tokenize(text)
            filtered_text = [word for word in word_tokens if word not in stop_words]
            return filtered_text

        def j48Tree(text):
            fraud = False
            if 'Home' not in text:
                print(1)
                if 'TX' not in text:
                    print(2)
                    if 'passionate' not in text:
                        print(3)
                        if 'secure' not in text:
                            print(4)
                            if 'growing' not in text:
                                print(5)
                                if 'participate' not in text:
                                    fraud = False
                                    print(6)
                                else:
                                    if '000' not in text:
                                        fraud = False
                                        print(7)
                                    else:
                                        if '–' not in text:
                                            fraud = True
                                            print(8)
                                        else:
                                            fraud = False
                                            print(9)
                            else:
                                fraud = False
                                print(10)
                        else:
                            fraud = False
                            print(11)
                    else:
                        fraud = False
                        print(12)
                else:
                    if '000' not in text:
                        fraud = False
                        print(13)
                    else:
                        if 'fun' not in text:
                            print(14)
                            if 'digital' not in text:
                                print(15)
                                if '–' not in text:
                                    print(16)
                                    if 'entry' not in text:
                                        fraud = True
                                        print(17)
                                    else:
                                        if 'web' not in text:
                                            fraud = False
                                            print(18)
                                        else:
                                            fraud = True
                                            print(19)
                                else:
                                    fraud = False
                                    print(20)
                            else:
                                fraud = False
                                print(21)
                        else:
                            fraud = True
                            print(22)
            else:
                if 'entry' not in text:
                    fraud = False
                    print(23)
                else:
                    if 'fun' not in text:
                        print(24)
                        if 'team' not in text:
                            fraud = True
                            print(25)
                        else:
                            fraud = False
                            print(26)
                    else:
                        fraud = False
                        print(27)

            return fraud



        userText = text



        userTextSplit = re.split(r'([\.,!\? ])', userText)

        print(userTextSplit)


        #userText_noPun = removePunct(userTextSplit)
        #print(userText_noPun)

        #userText_noPun_noSpace = remove_whitespace(userText_noPun)

        #userText_noPun_noSpace_remStop = remove_stopwords(userText_noPun_noSpace)

        finalClass = j48Tree(userText)

        return(finalClass)
    #main("","")