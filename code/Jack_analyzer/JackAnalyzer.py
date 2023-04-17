
import os
import sys


class JackTokenizer:

    def __init__(self,jackCode) -> None:
        self.__jackCode = jackCode
        self.index = 0

    def hasMoreTokens(self):
        try:
            self.__jackcode[self.index]
            
            #self.index = self.index + 1
            return True
        except:
            print("aa")
            return False
        
    
    def advance():
        pass

    def tokenType():
        pass

    def tokenizerLine(self):
        line = self.__jackCode[self.index]
        
        print(self.hasMoreTokens())
        
        while(self.hasMoreTokens()):
            if self.cleanLine(line):
                line = self.__jackCode[self.index]
                print(line)
            

    def cleanLine(self,line):
 
        line = line.strip()

        if line.startswith("//"):
            return None
        
        if line.startswith("/**"):
            openComment = True
            return None
        
        if line.endswith("*/") and openComment:
            openComment = False
            return None
        
        if not openComment:
            if line:
                return line

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

    tokenizer.tokenizerLine()
    

main()