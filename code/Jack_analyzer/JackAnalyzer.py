
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
            return "INT_CONST"
        return "IDENTIFIER"


    def keyword(self):
        if self.tokenType() == "KEYWORD":
            return self.__currentToken.upper()

    def symbol(self):
        if self.tokenType() == "SYMBOL":
            return self.__currentToken

    def intVal(self):
        if self.tokenType() == "INT_CONST":
            return int(self.__currentToken)

    def stringVal(self):
        if self.tokenType() == "STRING_CONST":
            return str(self.__currentToken)

    def identifier(self):
        if self.tokenType()=="IDENTIFIER":
            return str(self.__currentToken)

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

class CompileEngine:
    def __init__(self,code) -> None:
        self.__tokenized = code
        self.__xml = ""
        self.__tab = 0
        self.__op = ("+","-","*",'/','&',"|",'<','>','=')
        self.__keywordConstant = ("true","false","this","null")
        self.__unaryOp = ("-","~")

    def __str__(self) -> str:
        return self.__xml

    def getXML(self):
        return self.__xml

    def compileClass(self):
        self.appendXML("<class>")
        self.__tab += 1
        self.appendXML(f"<keyword> {self.__tokenized.keyword().lower()} </keyword>")
        self.__tokenized.advance()
        self.appendXML(f"<identifier> {self.__tokenized.identifier()} </identifier>")#

        # self.appendXML(f"<keyword> {self.__tokenized.keyword().lower()} </keyword>")
        self.__tokenized.advance()
        self.appendXML(f"<symbol> {self.__tokenized.symbol()} </symbol>") #{
        #TODO:  variables declaration
        self.__tokenized.advance()
        self.compileClassVarDec()
        while self.__tokenized.symbol() != "}":
            if self.__tokenized.keyword() in ("METHOD",'FUNCTION','CONSTRUCTOR'):
                self.compileSubroutine()
            self.__tokenized.advance()
    
        self.appendXML(f"<symbol> {self.__tokenized.symbol()} </symbol>") #}
        self.__tab -=1

        self.appendXML("</class>")

        print(self.__xml)

    def compileSubroutine(self):
        self.appendXML(f"<subroutineDec>")
        self.__tab += 1
        self.appendXML(f"<keyword> {self.__tokenized.keyword().lower()} </keyword>")
        self.__tokenized.advance()
        self.appendXML(f"<keyword> {self.__tokenized.keyword().lower()} </keyword>")
        self.__tokenized.advance()
        self.appendXML(f"<identifier> {self.__tokenized.identifier()} </identifier>")
        self.__tokenized.advance()
        self.appendXML(f"<symbol> {self.__tokenized.symbol()} </symbol>") #{
        # self.__tab -=1
        self.__tokenized.advance()
        #parameter list
        self.compileParameterList()
        self.appendXML(f"<symbol> {self.__tokenized.symbol()} </symbol>") #}
        self.__tokenized.advance()
        self.appendXML("<subroutineBody>")
        self.__tab+=1
        # {
        self.appendXML(f"<symbol> {self.__tokenized.symbol()} </symbol>")
        self.__tokenized.advance()

        while self.__tokenized.keyword() == "VAR":
            self.compileVarDec()

        self.compileStaments()

        self.__tab-=1
        self.__tokenized.advance()
        self.appendXML("</subroutineBody>")
        self.__tab-=1
        self.appendXML(f"</subroutineDec>")

    def compileStaments(self):
        self.appendXML("<statements>")
        self.__tab +=1
        while self.__tokenized.keyword() != "RETURN":
            if self.__tokenized.symbol() == '}':
                break
            self.compileStament()
            self.__tokenized.advance()
        
        if self.__tokenized.keyword() == "RETURN":
            self.appendXML("<returnStatement>")
            self.__tab +=1
            self.appendXML(f"<keyword> {self.__tokenized.keyword().lower()} </keyword>")
            self.__tokenized.advance()
            self.appendXML(f"<symbol> {self.__tokenized.symbol()} </symbol>")
            self.__tab -=1
            self.appendXML("</returnStatement>")
            self.__tab -=1
            self.appendXML("</statements>")
            self.appendXML("<symbol> } </symbol>")

        else:
            self.__tab -=1
            self.appendXML("</statements>")
            self.appendXML(f"<symbol> {self.__tokenized.symbol()} </symbol>")

    def compileStament(self):
        if self.__tokenized.keyword() == "WHILE":
            self.compileWhileStament()
        if self.__tokenized.keyword() == "LET":
            self.compileLetStament()
        if self.__tokenized.keyword() == "IF":
            self.compileIfStament()
        # if self.__tokenized.keyword() == "ELSE":
        #     self.compileElseStament()
        if self.__tokenized.keyword() == "DO":
            self.compileDoStament()

    def printToken(self):
        self.appendXML(self.__tokenized.getToken())

    def compileParameterList(self):
        self.appendXML("<parameterList>")
        if not self.__tokenized.symbol():
            self.__tab+=1
            print("no empty")
            self.__tab-=1
        self.appendXML("</parameterList>")

    def compileIfStament(self):
        self.appendXML("<ifStatement>")
        self.__tab += 1
        self.appendXML(f"<keyword> {self.__tokenized.keyword().lower()} </keyword>")
        self.__tokenized.advance()
        self.appendXML(f"<symbol> {self.__tokenized.symbol()} </symbol>") #(
        self.__tokenized.advance()
        if self.__tokenized.symbol() != ")":
            self.compileExpression()
        self.appendXML(f"<symbol> {self.__tokenized.symbol()} </symbol>") #)
        self.__tokenized.advance()
        self.appendXML(f"<symbol> {self.__tokenized.symbol()} </symbol>") #{
        self.__tokenized.advance()

        self.compileStaments()
        self.__tokenized.advance()
        if self.__tokenized.keyword() == "ELSE":
            self.appendXML(f"<keyword> {self.__tokenized.keyword().lower()} </keyword>")
            self.__tokenized.advance()
            self.appendXML(f"<symbol> {self.__tokenized.symbol()} </symbol>") #{
            self.compileStaments()
            self.appendXML(self.__tokenized.getToken() + "<-----")

            
        self.__tab -= 1
        self.appendXML("</ifStatement>")


    def appendXML(self,xml):
        self.__xml += "  "*self.__tab + xml + '\n'

    def compileVarDec(self):
        if self.__tokenized.keyword() == "VAR":
            self.appendXML("<varDec>")
            self.__tab += 1
            self.appendXML(f"<keyword> {self.__tokenized.keyword().lower()} </keyword>")
            self.__tokenized.advance()
            if self.__tokenized.keyword():
                self.appendXML(f"<keyword> {self.__tokenized.keyword().lower()} </keyword>")
            else:
                self.appendXML(f"<identifier> {self.__tokenized.identifier()} </identifier>")
            self.__tokenized.advance()
            self.appendXML(f"<identifier> {self.__tokenized.identifier()} </identifier>")
            self.__tokenized.advance()
            if self.__tokenized.symbol() == ",":
                while(not self.__tokenized.symbol() == ";"):
                    self.appendXML(f"<symbol> {self.__tokenized.symbol()} </symbol>")
                    self.__tokenized.advance()
                    self.appendXML(f"<identifier> {self.__tokenized.identifier()} </identifier>")
                    self.__tokenized.advance()

            if self.__tokenized.symbol() == ";":
                self.appendXML(f"<symbol> {self.__tokenized.symbol()} </symbol>")
                self.__tokenized.advance()
            
            self.__tab -= 1
            self.appendXML("</varDec>")

    def compileClassVarDec(self):
        self.appendXML("<classVarDec>")
        self.__tab += 1
        self.appendXML(f"<keyword> {self.__tokenized.keyword().lower()} </keyword>")
        self.__tokenized.advance()
        if self.__tokenized.keyword():
            self.appendXML(f"<keyword> {self.__tokenized.keyword().lower()} </keyword>")
        else:
            self.appendXML(f"<identifier> {self.__tokenized.identifier()} </identifier>")
        self.__tokenized.advance()
        self.appendXML(f"<identifier> {self.__tokenized.identifier()} </identifier>")
        self.__tokenized.advance()
        if self.__tokenized.symbol() == ",":
            while(not self.__tokenized.symbol() == ";"):
                self.appendXML(f"<symbol> {self.__tokenized.symbol()} </symbol>")
                self.__tokenized.advance()
                self.appendXML(f"<identifier> {self.__tokenized.identifier()} </identifier>")
                self.__tokenized.advance()

        if self.__tokenized.symbol() == ";":
            self.appendXML(f"<symbol> {self.__tokenized.symbol()} </symbol>")
            self.__tokenized.advance()

        self.__tab -= 1
        self.appendXML("</classVarDec>")

    def compileLetStament(self):
            self.appendXML("<letStatement>")
            self.__tab +=1
            self.appendXML(f"<keyword> {self.__tokenized.keyword().lower()} </keyword>")

            self.__tokenized.advance()

            if self.__tokenized.identifier():
                self.appendXML(f"<identifier> {self.__tokenized.identifier()} </identifier>")
                self.__tokenized.advance()

                if self.__tokenized.symbol() == "[":
                    self.appendXML(f"<symbol> {self.__tokenized.symbol()} </symbol>") #[
                    self.__tokenized.advance()
                    self.compileExpression()
                    self.appendXML(f"<symbol> {self.__tokenized.symbol()} </symbol>") #]
                    self.__tokenized.advance()
                    self.appendXML(f"<symbol> {self.__tokenized.symbol()} </symbol>") #]
                    self.__tokenized.advance() #=
                    self.compileExpression()
                    # self.appendXML(f"<symbol> {self.__tokenized.symbol()} </symbol>") #;
                else:
                    self.appendXML(f"<symbol> {self.__tokenized.symbol()} </symbol>") #;
                    self.__tokenized.advance()
                    self.compileExpression()

            self.appendXML(f"<symbol> {self.__tokenized.symbol()} </symbol>") #;
            self.__tab -= 1
            self.appendXML("</letStatement>")


    def compileWhileStament(self):
        self.appendXML("<whileStatement>")
        self.__tab +=1
        self.appendXML(f"<keyword> {self.__tokenized.keyword().lower()} </keyword>")
        self.__tokenized.advance()
        self.appendXML(f"<symbol> {self.__tokenized.symbol()} </symbol>") #(
        self.__tokenized.advance()
        self.compileExpression()

        self.appendXML(f"<symbol> {self.__tokenized.symbol()} </symbol>") #)
        self.__tokenized.advance()
        self.appendXML(f"<symbol> {self.__tokenized.symbol()} </symbol>") #{
        self.__tokenized.advance()

        self.compileStaments()

        self.__tab -=1
        self.appendXML("</whileStatement>")
        self.__tokenized.advance()

    def compileExpression(self):
        if self.__tokenized.symbol() == "=":
            return
        self.appendXML("<expression>")
        self.__tab +=1
        self.compileTerm()

        if self.__tokenized.symbol() in self.__op:
            self.appendXML(f"<symbol> {self.__tokenized.symbol()} </symbol>")
            self.__tokenized.advance()
            # self.appendXML(f"<symbol> {self.__tokenized.intVal()} </symbol>")
            self.compileTerm()
        self.__tab -=1
        self.appendXML("</expression>")

    def compileTerm(self):
        if self.__tokenized.symbol() == "=":
            return

        self.appendXML("<term>")
        self.__tab +=1

        if self.__tokenized.tokenType()=="IDENTIFIER":
            self.appendXML(f"<identifier> {self.__tokenized.identifier()} </identifier>")
            self.__tokenized.advance()
            if self.__tokenized.symbol()==".":
                self.appendXML(f"<symbol> {self.__tokenized.symbol()} </symbol>")
                self.__tokenized.advance()
                self.appendXML(f"<identifier> {self.__tokenized.identifier()} </identifier>")
                self.__tokenized.advance()
                self.appendXML(f"<symbol> {self.__tokenized.symbol()} </symbol>")
                self.appendXML("<expressionList>")
                self.__tab += 1
                self.__tokenized.advance()
                self.compileExpression()
                self.__tab -= 1
                self.appendXML("</expressionList>")
                self.appendXML(f"<symbol> {self.__tokenized.symbol()} </symbol>")
                self.__tokenized.advance()

        if self.__tokenized.symbol() == "[":
            self.appendXML(f"<symbol> {self.__tokenized.symbol()} </symbol>")
            self.__tokenized.advance()
            self.compileExpression()
            self.appendXML(f"<symbol> {self.__tokenized.symbol()} </symbol>")
            self.__tokenized.advance()


        if self.__tokenized.tokenType()=="INT_CONST":
            self.appendXML(f"<integerConstant> {self.__tokenized.intVal()} </integerConstant>")
            self.__tokenized.advance()

        if self.__tokenized.tokenType() == "KEYWORD" and self.__tokenized.keyword().lower() in self.__keywordConstant :
            # self.appendXML(self.__tokenized.getToken()+'adad')
            self.appendXML(f"<keyword> {self.__tokenized.keyword().lower()} </keyword>")
            self.__tokenized.advance()

        if self.__tokenized.tokenType() == 'STRING_CONST':
            self.appendXML(f"<stringConstant> {self.__tokenized.stringVal()} </stringConstant>")
            self.__tokenized.advance()
        
        self.__tab -=1
        self.appendXML("</term>")
    
    def compileDoStament(self):
        self.appendXML("<doStatement>")
        self.__tab += 1
        self.appendXML(f"<keyword> {self.__tokenized.keyword().lower()} </keyword>") #do
        self.__tokenized.advance()
        self.appendXML(f"<identifier> {self.__tokenized.identifier()} </identifier>")
        self.__tokenized.advance()
        self.appendXML(f"<symbol> {self.__tokenized.symbol()} </symbol>") #.
        self.__tokenized.advance()
        self.appendXML(f"<identifier> {self.__tokenized.identifier()} </identifier>")
        self.__tokenized.advance()
        self.appendXML(f"<symbol> {self.__tokenized.symbol()} </symbol>") #.
        self.appendXML("<expressionList>")
        self.__tokenized.advance()
        if self.__tokenized.symbol() != ")":
            self.__tab += 1
            self.compileExpression()
            self.__tab -= 1

        self.appendXML("</expressionList>")
        self.appendXML(f"<symbol> {self.__tokenized.symbol()} </symbol>") #)
        self.__tokenized.advance()
        self.appendXML(f"<symbol> {self.__tokenized.symbol()} </symbol>") #;

        self.__tab -=1
        self.appendXML("</doStatement>")

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

    def save_xml(self,text):
        with open("test.xml","w") as file:
            file.write(text.replace('"',''))
        file.close()

def main():
    path = sys.argv[1]
    
    analyzer = JackAnalyzer(path)

    analyzer.open()

    jackCode = analyzer.getCode()

    tokenizer = JackTokenizer(jackCode)
    tokenizer.cleanLines()

    print(tokenizer.getCode())
    tokenizer.advance()
    test=""
    # for i in range(100):
    while(tokenizer.hasMoreTokens()):
        # print(tokenizer.hasMoreTokens())

        if tokenizer.getToken() == "class":
        # if tokenizer.getToken() in ("function","method",'constructor'):
            test = CompileEngine(tokenizer)
            test.compileClass()

        tokenizer.advance()

    analyzer.save_xml(test.getXML())

main()