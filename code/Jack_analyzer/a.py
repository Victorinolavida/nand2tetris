
    # def compileClass(self):
    #     if self.__tokenized.tokenType() == "KEYWORD" and self.__tokenized.keyword() == "CLASS":
    #         self.appendXML("<class>")
    #         self.__tokenized.advance()
    #         self.__tab += 1
    #         self.appendXML("<keyword> class </keyword>")
    #         self.appendXML(f"<identifier> {self.__tokenized.identifier()} </identifier>")
    #         self.__tokenized.advance()
    #         self.appendXML(f"<symbol> {self.__tokenized.symbol()} </symbol>") #{
    #         self.__tokenized.advance()
            
    #         if self.__tokenized.keyword() in ("STATIC","FIELD"):
    #             self.compileClassVarDec()
    #         if self.__tokenized.keyword() in ("FUNCTION","METHOD"):
    #             self.compileSubroutine()
    #         self.appendXML(f"<symbol> {self.__tokenized.symbol()} </symbol>") #}
    #         self.__tab -= 1
    #         self.appendXML("</class>")

    #     print(self.__xml)

    # def compileClassVarDec(self):
    #     self.appendXML("<classVarDec>")
    #     self.__tab += 1
    #     self.appendXML(f"<keyword> {self.__tokenized.keyword().lower()} </keyword>")
    #     self.__tokenized.advance()
    #     if self.__tokenized.keyword():
    #         self.appendXML(f"<keyword> {self.__tokenized.keyword().lower()} </keyword>")
    #     else:
    #         self.appendXML(f"<identifier> {self.__tokenized.identifier()} </identifier>")
    #     self.__tokenized.advance()
    #     self.appendXML(f"<identifier> {self.__tokenized.identifier()} </identifier>")
    #     self.__tokenized.advance()
    #     if self.__tokenized.symbol() == ",":
    #         while(not self.__tokenized.symbol() == ";"):
    #             self.appendXML(f"<symbol> {self.__tokenized.symbol()} </symbol>")
    #             self.__tokenized.advance()
    #             self.appendXML(f"<identifier> {self.__tokenized.identifier()} </identifier>")
    #             self.__tokenized.advance()

    #     if self.__tokenized.symbol() == ";":
    #         self.appendXML(f"<symbol> {self.__tokenized.symbol()} </symbol>")
    #         self.__tokenized.advance()

    #     self.__tab -= 1
    #     self.appendXML("</classVarDec>")

    # def compileParameterList(self):
    #     self.appendXML("<parameterList>")
    #     if not self.__tokenized.symbol():
    #         self.__tab+=1
    #         print("no empty")
    #         self.__tab-=1
    #     self.appendXML("</parameterList>")

    # def varDec(self):
    #     if self.__tokenized.keyword() == "VAR":
    #         self.appendXML("<varDec>")
    #         self.__tab += 1
    #         self.appendXML(f"<keyword> {self.__tokenized.keyword().lower()} </keyword>")
    #         self.__tokenized.advance()
    #         if self.__tokenized.keyword():
    #             self.appendXML(f"<keyword> {self.__tokenized.keyword().lower()} </keyword>")
    #         else:
    #             self.appendXML(f"<identifier> {self.__tokenized.identifier()} </identifier>")
    #         self.__tokenized.advance()
    #         self.appendXML(f"<identifier> {self.__tokenized.identifier()} </identifier>")
    #         self.__tokenized.advance()
    #         if self.__tokenized.symbol() == ",":
    #             while(not self.__tokenized.symbol() == ";"):
    #                 self.appendXML(f"<symbol> {self.__tokenized.symbol()} </symbol>")
    #                 self.__tokenized.advance()
    #                 self.appendXML(f"<identifier> {self.__tokenized.identifier()} </identifier>")
    #                 self.__tokenized.advance()

    #         if self.__tokenized.symbol() == ";":
    #             self.appendXML(f"<symbol> {self.__tokenized.symbol()} </symbol>")
    #             self.__tokenized.advance()
            
    #         self.__tab -= 1
    #         self.appendXML("</varDec>")

    # def compileSubroutine(self):
    #     self.appendXML(f"<subroutineDec>")
    #     self.__tab += 1
    #     self.appendXML(f"<keyword> {self.__tokenized.keyword().lower()} </keyword>")
    #     self.__tokenized.advance()
    #     self.appendXML(f"<keyword> {self.__tokenized.keyword().lower()} </keyword>")
    #     self.__tokenized.advance()
    #     self.appendXML(f"<identifier> {self.__tokenized.identifier()} </identifier>")
    #     self.__tokenized.advance()
    #     self.appendXML(f"<symbol> {self.__tokenized.symbol()} </symbol>")
    #     # self.__tab -=1
    #     self.__tokenized.advance()
    #     #parameter list
    #     self.compileParameterList()
    #     self.appendXML(f"<symbol> {self.__tokenized.symbol()} </symbol>")
    #     self.__tokenized.advance()
    #     # self.appendXML(f"</subroutineDec>")
    #     self.appendXML("<subroutineBody>")
    #     self.__tab+=1
    #     # {
    #     self.appendXML(f"<symbol> {self.__tokenized.symbol()} </symbol>")
    #     self.__tokenized.advance()
    #     #var declaration
    #     while(self.__tokenized.keyword()=="VAR"):
    #         self.varDec()

    #     self.compileStaments()
    #     self.__tab-=1
    #     self.appendXML("</subroutineBody>")
    #     self.__tab-=1
    #     self.appendXML(f"</subroutineDec>")

    # #TODO:
    # def compileDoStament():
    #     pass
    # def compileIfStament(self):
    #     self.appendXML("<ifStatement>")
    #     self.__tab +=1
    #     self.appendXML(f"<keyword> {self.__tokenized.keyword().lower()} </keyword>")
    #     self.__tokenized.advance()
    #     self.appendXML(f"<symbol> {self.__tokenized.symbol()} </symbol>") #(
    #     self.__tab +=1
    #     self.__tokenized.advance()
    #     self.compileExpression()
    #     self.appendXML(f"<symbol> {self.__tokenized.symbol()} </symbol>") #)
    #     self.__tokenized.advance()
    #     self.appendXML(f"<symbol> {self.__tokenized.symbol()} </symbol>") #{
    #     self.__tokenized.advance()
    #     self.compileStaments()
    
    def appendXML(self,xml):
        self.__xml += "  "*self.__tab + xml + '\n'

    # def compileStaments(self,pre=True):
        
    #     self.appendXML("<statements>")
    #     while(self.__tokenized.getToken()!="}"):
    #     #     if self.__tokenized.keyword() in ("WHILE","LET","IF"):
    #         print(self.__tokenized.getToken())  
    #         if self.__tokenized.keyword() == "LET":
    #             self.compileLetStament()
    #             # self.appendXML(self.__tokenized.getToken()+'adad')

    #         if self.__tokenized.keyword() == "WHILE":
    #             # self.compileWhileStament()
    #             pass
    #         if self.__tokenized.keyword() == "ELSE":
    #             break

    #             self.__tokenized.advance()
    #             # self.compileStaments()
    #     # self.appendXML(self.__tokenized.getToken()+"aa")
            
    #     # self.appendXML(f"<symbol> {self.__tokenized.symbol()} </symbol>") #}
    #         self.__tokenized.advance()
    #     self.appendXML("</statements>")

    # def compileLetStament(self):
    #     while(self.__tokenized.getToken() != ';'):
    #         self.__tab +=1
    #         self.appendXML("<letStatement>")
    #         self.__tab +=1
    #         self.appendXML(f"<keyword> {self.__tokenized.keyword()} </keyword>")
    #         self.__tokenized.advance()
    #         self.appendXML(f"<identifier> {self.__tokenized.identifier()} </identifier>")#
    #         self.__tokenized.advance()

    #         if self.__tokenized.symbol() == "[":
    #             self.appendXML(f"<symbol> {self.__tokenized.symbol()} </symbol>") #[
    #             self.__tokenized.advance()
    #             self.compileExpression()
    #             self.appendXML(f"<symbol> {self.__tokenized.symbol()} </symbol>") #]

    #             self.__tokenized.advance()
    #             self.appendXML(f"<symbol> {self.__tokenized.symbol()} </symbol>") #=
    #             self.__tokenized.advance()
    #             self.compileExpression()
    #             self.appendXML(f"<symbol> {self.__tokenized.symbol()} </symbol>")
    #             self.__tab -=1
    #             self.appendXML("</letStatement>")
    #             self.__tab -=1
    #             self.__tokenized.advance()

    #         else:
    #             self.appendXML(f"<symbol> {self.__tokenized.symbol()} </symbol>")
    #             self.__tokenized.advance()
    #             self.compileExpression()
    #             self.appendXML(f"<symbol> {self.__tokenized.symbol()} </symbol>")
    #             self.__tab -=1
    #             self.appendXML("</letStatement>")
    #             self.__tab -=1
    #             self.__tokenized.advance()
    #     self.appendXML(f"<symbol> {self.__tokenized.symbol()} </symbol>")

    # def compileWhileStament(self):
    #     self.appendXML("<whileStatement>")
    #     self.__tab +=1
    #     self.appendXML(f"<keyword> {self.__tokenized.keyword().lower()} </keyword>")
    #     self.__tokenized.advance()
    #     self.__tab +=1
    #     self.appendXML(f"<symbol> {self.__tokenized.symbol()} </symbol>") #(
    #     self.__tokenized.advance()
    #     self.__tab +=1
    #     self.compileExpression()

    #     self.appendXML(f"<symbol> {self.__tokenized.symbol()} </symbol>") #)
    #     self.__tokenized.advance()
    #     self.appendXML(f"<symbol> {self.__tokenized.symbol()} </symbol>") #{
    #     self.__tokenized.advance()
    #     self.compileStaments()
    #     self.__tab -=1
    #     self.appendXML(f"<symbol> {self.__tokenized.getToken()} </symbol>") #}

    #     self.__tab -=1
    #     self.appendXML("</whileStatement>")
    #     self.__tokenized.advance()

    # def compileExpression(self):
    #     if self.__tokenized.symbol() == "=":
    #         return
    #     self.appendXML("<expression>")
    #     self.__tab +=1
    #     self.compileTerm()

    #     if self.__tokenized.symbol() in self.__op:
    #         self.appendXML(f"<symbol> {self.__tokenized.symbol()} </symbol>")
    #         self.__tokenized.advance()
    #         # self.appendXML(f"<symbol> {self.__tokenized.intVal()} </symbol>")
    #         self.compileTerm()
    #     self.__tab -=1
    #     self.appendXML("</expression>")

    # def compileTerm(self):