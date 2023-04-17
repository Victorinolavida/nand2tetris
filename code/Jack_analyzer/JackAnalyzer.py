
import os
import sys
import re


class JackTokenizer:

    def __init__(self,jackCode) -> None:
        self.__jackCode = jackCode

        self.__keywords = ['class' , 'constructor' , 'function' ,
                        'method' , 'field' , 'static' , 'var' , 'int' ,
                        'char' , 'boolean' , 'void' , 'true' , 'false' ,
                        'null' , 'this' , 'let' , 'do' , 'if' , 'else' ,
                        'while' , 'return']
        self.__symbolds  = ['{','}','(',')','[',']','.',',',';','+','-','*',
                            '/','&','|','<','>','=','~']
        self.__identifyer = r"_?([A-Za-z])\w+"
        self.__numConst = r"(\d){1,5}"
        self.__strConst = r"(\"\w.*\")"
        self.__currentToken = None

    def hasMoreTokens(self):
        if not self.__jackCode:

            return False

        for keyword in self.__keywords:
            if re.search(keyword,self.__jackCode):
                return True
        for symbol in self.__symbolds:
            if re.search(symbol,self.__jackCode):
                return True
        if re.search(self.__identifyer,self.__jackCode):
            return True
        if re.search(self.__numConst,self.__jackCode):
            return True
        if re.search(self.__strConst,self.__jackCode):
            return True
        return False

    def advance(self):
        #firstWord = self.__jackCode.split(" ")[0]
        #rest = self.__jackCode.split(" ")[1:]

        #wordFind = re.search(r"(\w+)",firstWord)
        #symbolFind = re.search(r"[{}()\[\].,;+\-*/&|<>=~']",firstWord)
        #string = re.search(r'\"\w.*\"',firstWord)
        #number = re.search(r"[0-9]{1,5}",firstWord)
        self.__currentToken = ""
        cut = 0
        special = False
        for index,letter in enumerate(self.__jackCode):
            self.__currentToken += letter

            if letter == '"':
                special = True

            if len(self.__currentToken) >=1 and letter == " " and not special:
                cut = index
                special=False
                break

            if letter in self.__symbolds and len(self.__currentToken)==1:
                self.__currentToken = letter
                cut = index + 1
                break
            
            if letter in self.__symbolds:

                if len(self.__currentToken) > 1:
                    # print(self.__currentToken)
                    self.__currentToken = self.__currentToken[:-1]
                    cut = index
                    break
                else:
                    cut = index + 1
                    break
            if self.__currentToken in self.__keywords:
                cut = index + 1
                break

            

        self.__currentToken = self.__currentToken.strip()
        self.__jackCode = self.__jackCode[cut:].strip()


    def tokenType(self):
        if self.__currentToken in self.__keywords:
            return "KEYWORD"
        if self.__currentToken in self.__symbolds:
            return "SYMBOL"
        if re.search(self.__strConst,self.__currentToken):
            return "STRING_CONST"
        if re.search(self.__numConst,self.__currentToken):
            return "NUMBER_CONST"
        if re.search(self.__identifyer,self.__currentToken):
            return True

    def setToken(self):
        self.__currentToken = "class"

    def getToken(self):
        return self.__currentToken

    def getCode(self):
        return self.__jackCode


    def cleanLines(self):
        codeClean = ""
        openComment = False
        for line in self.__jackCode:
            line = line.strip()
            if line.startswith("//"):
                continue
            if line.startswith("/**"):
                openComment = True
                continue
            if "*/" in line:
                openComment = False
                continue
            if openComment:
                continue
            if not line:
                continue
            codeClean += line
        self.__jackCode = codeClean

class compileEngine:
    pass

class JackAnalyzer:
    
    def __init__(self,path) -> None:
        self.__path = path
    

    def open(self):
        #check if the passed path is a file or a directory
        isDirectory = os.path.isdir(self.__path)
        isFile = os.path.isfile(self.__path)
        #if path correspond to a directory
        if isDirectory:
            self.directory()


        #print(os.path.join(os.getcwd(),self.__path))
        #if path is a file
        if isFile:
            self.file()

    def file(self):

        with open(self.__path) as codeJack:
            self.__jackCode = codeJack.readlines()

    def directory(self):
        jackFiles = os.listdir(os.path.join(self.__path))
        self.__jackCode = list()

        for file in jackFiles:
            if ".jack" in file:
                path = os.path.join(self.__path, file)
                with open(path) as code:
                    self.__jackCode.append(code.readlines())
                    code.close()
    def getCode(self):
        return self.__jackCode


def main():
    path = sys.argv[1]
    
    analyzer = JackAnalyzer(path)

    analyzer.open()

    jackCode = analyzer.getCode()


    tokenizer = JackTokenizer(jackCode)
    tokenizer.cleanLines()

    tokenizer.advance()
    # for i in range(100):
    while(tokenizer.hasMoreTokens()):
        # print(tokenizer.hasMoreTokens())
        print(tokenizer.getToken())

        tokenizer.advance()
    print(tokenizer.getToken())

main()