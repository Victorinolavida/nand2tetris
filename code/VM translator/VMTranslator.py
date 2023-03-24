
#!/usr/bin/python3

import sys

import re
import os


file_path = sys.argv[1]

split = file_path.split("/")
name = split[-1].replace(".vm","")

MEMORY_SEGMENTS = {
    "SP":"0",
    "LCL":"1",
    "ARG":"2",
    "THIS":"3",
    "THAT":"4",
    "TEMP":"5",

}


class Main():
    def __init__(self, file):
        self.__file = self.read_file(file)
        self.__path = file
        self.get_names()

    def get_names(self):
        self.__new_path = self.__path.replace(".vm",".asm")

    def read_file(self,file):

        with open(file,"r") as vm_code:
            return vm_code.readlines()

    def parser(self):
        self.__asm_code = ""
        for index, row in enumerate(self.__file):
            if not row.startswith('//') and row and not row=="\n":
                # print(Operation(row).get_asm_code())
                code = Operation(row,index,name=name).get_asm_code()
                code = os.linesep.join([s for s in code.splitlines() if s]) 
                self.__asm_code += code + "\n" + "\n"
    def save(self):

        self.parser()
        with open(f'{self.__new_path}', 'w') as file:
           file.write(self.__asm_code)

class Operation():

    def __init__(self, operation,index=0,name='') -> None:
        self.__operation = operation
        self.__name = name
        self.__id = index
        self.__segment = self.get_segment()

    def get_segment(self):
        if "local" in self.__operation:
            return 'LCL'
        elif "argument" in self.__operation:
            return 'ARG'
        elif "this" in self.__operation:
            return 'THIS'
        elif "that" in self.__operation:
            return 'THAT'
        elif "constant" in self.__operation:
            return 'constant'
        elif "static" in self.__operation:
            return 'static'
        elif "temp" in self.__operation:
            return 'TEMP'
        elif "pointer" in self.__operation:
            number = int(re.findall(r'\d+', self.__operation)[0])
            if number== 0:
                return "THIS"
            elif number==1:
                return "THAT"

    def push_constant(self):

        number = re.findall(r'\d+', self.__operation)

        return f"""
            // {self.__operation}
            @{number[0]}
            D=A

            @{MEMORY_SEGMENTS["SP"]}
            A=M
            M=D
            A=A+1
            @{MEMORY_SEGMENTS["SP"]}
            M=M+1
        """

    def push(self):
        number = re.findall(r'\d+', self.__operation)
        add = self.__segment

        if 'temp' in self.__operation:
            return f"""
            //{self.__operation}

            @{MEMORY_SEGMENTS[add]}
            D=A
            @{number[0]}
            A=D+A
            D=M
            @{MEMORY_SEGMENTS['SP']}
            A=M
            M=D
            @{MEMORY_SEGMENTS['SP']}
            M=M+1
            
            """

    

        return f"""
        //{self.__operation}
        @{number[0]}
        D=A
        @{MEMORY_SEGMENTS[add]}
        A=D+M
        D=M
        @{MEMORY_SEGMENTS['SP']}
        A=M
        M=D
        @{MEMORY_SEGMENTS['SP']}
        M=M+1
        """


    def pop(self):
        number = re.findall(r'\d+', self.__operation)
        add = self.__segment
        
        instruccion = 'D=D+M'
        if 'temp' in self.__operation:
            instruccion = 'D=D+A'

        return f"""
            //{self.__operation}
            @{number[0]}
            D=A
            @{MEMORY_SEGMENTS[add]}
            {instruccion}
            @R13
            M=D

            //0--
            @{MEMORY_SEGMENTS['SP']}
            M=M-1

            // *addr=*SP
            A=M
            D=M
            @R13
            A=M
            M=D
            """


    def add(self):
        return f"""
        //{self.__operation}

        @{MEMORY_SEGMENTS['SP']}
        M=M-1
        A=M
        D=M
        A=A-1
        M=M+D
        """

    def sub(self):
        return f"""
        //{self.__operation}
        @{MEMORY_SEGMENTS['SP']}
        M=M-1
        A=M
        D=M
        A=A-1
        M=M-D
        """    

    def equal(self):
        return f"""
        //{self.__operation}
        @{MEMORY_SEGMENTS['SP']}
        M=M-1
        A=M
        D=M
        A=A-1
        D=M-D

        M=-1
        @JUMP.equal.{self.__id}

        D;JEQ


        @{MEMORY_SEGMENTS['SP']}
        A=M-1
        M=0

        (JUMP.equal.{self.__id})
        """
    
    def less(self):
        return f"""
        //{self.__operation}
        @{MEMORY_SEGMENTS['SP']}
        M=M-1
        A=M
        D=M
        A=A-1
        D=D-M
        M=-1
        @JUMP.less.{self.__id}
        D;JGT
        @{MEMORY_SEGMENTS['SP']}
        A=M
        A=A-1
        M=0
        (JUMP.less.{self.__id})
        """

    def grater(self):
        return f"""
        //{self.__operation}
        @{MEMORY_SEGMENTS['SP']}
        M=M-1
        A=M
        D=M
        A=A-1
        D=M-D
        M=-1
        @JUMP.gt.{self.__id}
        D;JGT
        @{MEMORY_SEGMENTS['SP']}
        A=M
        A=A-1
        M=0
        (JUMP.gt.{self.__id})
        """
    
    def not_op(self):
        return f"""
        //{self.__operation}
        @{MEMORY_SEGMENTS['SP']}
        A=M-1
        M=!M
        """

    def neg(self):
        return f"""
        //{self.__operation}
        @{MEMORY_SEGMENTS['SP']}
        A=M-1
        M=-M
        """

    def and_op(self):
        return f"""
        //{self.__operation}

        @{MEMORY_SEGMENTS['SP']}
        M=M-1
        A=M
        D=M
        A=A-1
        M=M&D
        """
    
    def or_op(self):
        return f"""
        //{self.__operation}
        @{MEMORY_SEGMENTS['SP']}
        M=M-1
        A=M
        D=M
        A=A-1
        M=M|D
        """

    def pointer(self):
        add = self.__segment
        
        if "push" in self.__operation:
            return f"""
                //{self.__operation}
                @{MEMORY_SEGMENTS[add]}
                D=M
                @{MEMORY_SEGMENTS['SP']}
                A=M
                M=D
                @{MEMORY_SEGMENTS['SP']}
                M=M+1
            """
        elif "pop" in self.__operation:
            return f"""
                //{self.__operation}
                @{MEMORY_SEGMENTS['SP']}
                M=M-1
                A=M
                D=M
                @{MEMORY_SEGMENTS[add]}
                M=D
            """

    def static(self):
        number = re.findall(r'\d+', self.__operation)

        if "pop" in self.__operation:
            return f"""
                @{self.__name}.{number[0]}
                    D=A
                    @R13
                    M=D

                    // SP--
                    @{MEMORY_SEGMENTS['SP']}
                    M=M-1

                    // *addr=*SP
                    A=M
                    D=M
                    @R13
                    A=M
                    M=D
            """
        elif "push" in self.__operation:
            return f"""
                @{self.__name}.{number[0]}
                D=M

                // *SP=*addr
                @{MEMORY_SEGMENTS['SP']}
                A=M
                M=D

                // SP++
                @{MEMORY_SEGMENTS['SP']}
                M=M+1
            """
    def get_asm_code(self):
        asm=''
        if "constant" in self.__operation:
            asm=self.push_constant()
        elif "argument" in self.__operation or "this" in self.__operation or "temp" in self.__operation:
            if "push" in self.__operation:
                asm=self.push()
            elif "pop" in self.__operation:
                asm=self.pop()
        elif  "that" in self.__operation or "local" in self.__operation:
            if "push" in self.__operation:
                asm=self.push()
            elif "pop" in self.__operation:
                asm=self.pop()
        elif "static" in self.__operation:
            asm = self.static()
        elif "add" in self.__operation:
            asm=self.add()
        elif "sub" in self.__operation:
            asm=self.sub()
        elif 'eq' in self.__operation:
            asm=self.equal()
        elif 'lt' in self.__operation:
            asm=self.less()
        elif 'gt' in self.__operation:
            asm=self.grater()
        elif 'not' in self.__operation:
            asm=self.not_op()
        elif 'neg' in self.__operation:
            asm=self.neg()
        elif 'and' in self.__operation:
            asm=self.and_op()
        elif 'or' in self.__operation:
            asm=self.or_op()
        elif "pointer" in self.__operation:
            asm = self.pointer()
        try:
            return asm.replace('  ','')
        except:
            print(self.__operation)






if ".vm" in file_path:

    file = Main(file_path).save()
else:
    print("error de archivo")