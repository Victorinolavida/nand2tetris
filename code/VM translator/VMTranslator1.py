
#!/usr/bin/python3

import sys
import re
import os


file_path = sys.argv[1]
# file_path = "test.vm"



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
        self.__path = file
        self.set_name()
        self.__code = ""
        self.__file = self.read_file(file)

    def is_dir(self):
        return os.path.isdir(self.__path)

    def set_name(self):
        self.__new_path = self.__path.replace(".vm",".asm")
        split_path = self.__path.split("/")
        self.__name=split_path[-1].replace(".asm",'')

    def read_file(self,file):
        if self.is_dir():
            if file[-1] == "/":
                file = file[:-1]
            name_dir = file.split("/")
            self.__name_dir = name_dir[-1]
            self.__new_path = os.path.join(file,f"{self.__name_dir}.asm")
            print(self.__new_path,"new path")

            try:
                a = []
                for name in os.listdir(file):
                    if ".vm" in name:
                        a.append(os.path.join(file,name))
                self.__files = a
            except:
                print("Sys.vm not found")
        else:
            try:
                with open(file,"r") as vm_code:
                    return vm_code.readlines()
            except:
                print(f"{file} not found")

    def parser(self):
        code = list()
        # print(self.__file)
        for  row in self.__file:
            if not row.startswith('//') and row and not row=="\n":
                line = row.replace('\n','').replace("\t",'')
                comment = re.search("//",line)

                if comment:
                    index = comment.start()
                    line = line[:index]

                code.append(line.replace("  ","").strip())
        
        for i,a in enumerate(code):
            asm_code = Operation(a,i,name=self.__name)
            self.__code += asm_code.get_instruction()


    def parser_dir(self):
        code = ""
        for file in self.__files:
            file_name = file.split("/")
            file_name = file_name[-1].replace(".vm","")

            with open(file,"r") as code_vm:
                self.__file = code_vm.readlines()

            self.__name = file_name
            self.parser()
            code += self.__code
        self.__code=code

    def save(self):

        if self.is_dir():
             self.parser_dir()
        else:
            self.parser()

        test = self.__new_path.replace(".asm","-test.asm")

        #print(self.__new_path.replace(".vm","test.vm"))

        with open(f'{test}', 'w') as file:
          file.write(self.__code)
        print("file saved")

class Operation():

    def __init__(self, operation,index=0,name='') -> None:
        self.__operation = operation
        self.__name = name
        self.__id = index
        self.__segment = self.get_segment()
        self.__instruction_asm = ""

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
    
    def push(self):
        number = re.findall(r'\d+', self.__operation)
        address = self.__segment

        asm_intruction = f"//{self.__operation}\n"

        if 'temp' in self.__operation:
            asm_intruction += f"""
                @{MEMORY_SEGMENTS[address]}
                D=A
                @{number[0]}
                A=D+A
                D=M
            """
        elif "constant" in self.__operation:
            asm_intruction += f"""
                @{number[0]}
                D=A
            """
        else:
            asm_intruction += f"""
                @{number[0]}
                D=A
                @{MEMORY_SEGMENTS[address]}
                A=D+M
                D=M
            """

        asm_intruction += f"""
            @{MEMORY_SEGMENTS['SP']}
            A=M
            M=D
            @{MEMORY_SEGMENTS['SP']}
            M=M+1
        """
        self.__instruction_asm = asm_intruction

    def pop(self):
        number = re.findall(r'\d+', self.__operation)
        add = self.__segment

        instruccion = 'D=D+M'
        if 'temp' in self.__operation:
            instruccion = 'D=D+A'

        self.__instruction_asm = f"""
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

    def sum_sub(self):
        op = "+"

        if "sub" in self.__operation:
            op = "-"

        self.__instruction_asm = f"""
        //{self.__operation}

        @{MEMORY_SEGMENTS['SP']}
        M=M-1
        A=M
        D=M
        A=A-1
        M=M{op}D
        """

    def compare(self):
        operation = {'comp':'eq','jmp':'JEQ'}
        
        if "lt" in self.__operation:
            # operation = {'comp':'lt','jmp':'JLE'}
            operation = {'comp':'lt','jmp':'JLT'}
        if "gt" in  self.__operation:
            # operation = {'comp':'gt','jmp':'JLE'}
            operation = {'comp':'gt','jmp':'JGT'}

        asm_code = f"""
            //{self.__operation}
            @{MEMORY_SEGMENTS['SP']}
            M=M-1
            A=M
            D=M
            A=A-1
            D=M-D
            M=-1
            @jump.{operation['comp']}.{self.__id}
            D;{operation['jmp']}
            @{MEMORY_SEGMENTS['SP']}
            A=M-1
            M=0
            (jump.{operation['comp']}.{self.__id})
        """

        self.__instruction_asm = asm_code

    def not_neg_op(self):

        op = "!"

        if "neg" in self.__operation:
            op = "-"

        self.__instruction_asm = f"""
        //{self.__operation}
        @{MEMORY_SEGMENTS['SP']}
        A=M-1
        M={op}M
        """

    def logic_op(self):
        op = "&"

        if "or" in self.__operation:
            op = "|"

        self.__instruction_asm = f"""
        //{self.__operation}
        @{MEMORY_SEGMENTS['SP']}
        M=M-1
        A=M
        D=M
        A=A-1
        M=M{op}D
        """
    
    def pointer(self):
        add = self.__segment
        if "push" in self.__operation:
            self.__instruction_asm = f"""
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
            self.__instruction_asm = f"""
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
            self.__instruction_asm = f"""
                @{self.__name}.{number[0]}
                    D=A
                    @R13
                    M=D
                    @{MEMORY_SEGMENTS['SP']}
                    M=M-1
                    A=M
                    D=M
                    @R13
                    A=M
                    M=D
            """
        elif "push" in self.__operation:
            self.__instruction_asm = f"""
                @{self.__name}.{number[0]}
                D=M
                @{MEMORY_SEGMENTS['SP']}
                A=M
                M=D
                @{MEMORY_SEGMENTS['SP']}
                M=M+1
            """

    def set_instruction(self):

        if "push" in self.__operation and not "static" in self.__operation:
            self.push()
        elif "pop" in self.__operation and not "static" in self.__operation:
            self.pop()
        elif "add" == self.__operation or "sub" == self.__operation:
            self.sum_sub()
        elif "eq" == self.__operation or "lt" == self.__operation or "gt" == self.__operation:
            self.compare()
        elif "not" == self.__operation or "neg" == self.__operation:
            self.not_neg_op()
        elif "and" == self.__operation or "or" == self.__operation :
            self.logic_op()
        elif "pointer" in self.__operation:
            self.pointer()
        elif "static" in self.__operation:
            self.static()
        elif "label" in self.__operation or "goto" in self.__operation:
            self.flow()
        elif "function" in self.__operation:
            self.function()
        elif "return" in self.__operation:
            self.return_op()
        elif 'call' in self.__operation:
            self.call_funtion()

    def flow(self):
        label = self.__operation.split(" ")
        name = label[1]

        if "label" in self.__operation:
            self.__instruction_asm = f"({name})"

        if "goto" in self.__operation:
            label=1
            JMP = "JMP"
            
            if "if" in self.__operation:
                JMP = "JNE"
        
            self.__instruction_asm = f"""
                @{MEMORY_SEGMENTS['SP']}
                M=M-1
                A=M
                D=M

                @{name}
                D;{JMP}
            """

    def function(self):

        name_split = self.__operation.split(" ")
        name = self.__operation.split(" ")[1]
        nVars = int(name_split[-1])
        code_function = None


        code_function = f"""
             //{self.__operation}
            ({name})
            """

        for _ in range(nVars):
            self.__operation = "push constant 0"
            self.get_instruction()
            code_function += self.__instruction_asm

        self.__instruction_asm = code_function 

    def call_funtion(self):
        code_call = f"//{self.__operation}\n"
        nArgs  = int(re.findall(r'\d+', self.__operation)[0])
        name_split = self.__operation.split(" ")
        name = name_split[1]
        
        code_call += f"""
            @{name}$ret
            D=A
            @{MEMORY_SEGMENTS['SP']}
            A=M
            M=D
            @{MEMORY_SEGMENTS['SP']}
            M=M+1
        """

        for i in MEMORY_SEGMENTS:
            if not i=="TEMP":
                code_call += f"//push {i}"
                code_call += f"""
                    @{MEMORY_SEGMENTS[i]}
                    D=M
                    @{MEMORY_SEGMENTS['SP']}
                    A=M
                    M=D
                    @{MEMORY_SEGMENTS['SP']}
                    M=M+1
                """

        code_call += f"""
        @{name}
        0;JMP
        ({name}$ret)
        """

        # code_call += f"""
        #     @{nArgs}
        #     D=A
        #     @R14
        #     M=D
        #     (LOOP.{name})
        #     @R14
        #     D=M
        #     @END.{name}
        #     D;JEQ
        #     @{MEMORY_SEGMENTS['SP']}
        #     A=M
        #     M=0
        #     A=A
        #     @{MEMORY_SEGMENTS['SP']}
        #     M=M+1
        #     @R14
        #     M=M-1
        #     @LOOP.{name}
        #     D;JMP
        #     (END.{name})
        # """
        

        # code_call += f"""
        #             //push retAddrLabel
        #             @retAddrLabel.{name}
        #             D=M
        #             @{MEMORY_SEGMENTS['SP']}
        #             A=M
        #             M=D
        #             @{MEMORY_SEGMENTS['SP']}
        #             M=M+1
        #         """


        # for i in MEMORY_SEGMENTS:
        #     if not i=="TEMP":
        #         code_call += f"//push {i}"
        #         code_call += f"""
        #             @{MEMORY_SEGMENTS[i]}
        #             D=M
        #             @{MEMORY_SEGMENTS['SP']}
        #             A=M
        #             M=D
        #             @{MEMORY_SEGMENTS['SP']}
        #             M=M+1
        #         """
        
        # code_call += f"""
        #     //ARG = SP – 5 – nArgs
        #     @{MEMORY_SEGMENTS['SP']}
        #     D=M
        #     @5
        #     D=D-A
        #     @{nArgs}
        #     D=D-A
        #     @{MEMORY_SEGMENTS['ARG']}
        #     M=D
        #     // LCL = SP
        #     @{MEMORY_SEGMENTS['SP']}
        #     D=M
        #     @{MEMORY_SEGMENTS['LCL']}
        #     M=D
        #     (retAddrLabel.{name})
        # """

        # code_call += f"""
        #     @{name}
        #     D;JMP
        
        # """

        self.__instruction_asm = code_call

    def return_op(self):

        return_code = f"""
            //return

            //endFrame=LCL
            @{MEMORY_SEGMENTS['LCL']}
            D=M
            @R13 //endFrame
            M=D
            //retAddr = *(endFrame - 5) = RAM(endFrame - 5)
            @5
            D=A
            @R13
            D=M-D
            A=D
            D=M
            @R14 //retAddr
            M=D
            //RAM[ARG]=*ARG = pop()
            @{MEMORY_SEGMENTS['SP']}
            A=M-1
            D=M
            @{MEMORY_SEGMENTS['ARG']}
            A=M
            M=D
            //SP = ARG + 1
            @{MEMORY_SEGMENTS['ARG']}
            D=M
            @{MEMORY_SEGMENTS['SP']}
            M=D+1
            //THAT = *(endFrame – 1)
            @R13
            M=M-1
            A=M
            D=M
            @{MEMORY_SEGMENTS['THAT']}
            M=D
            //THIS = *(endFrame – 1)
            @R13
            M=M-1
            A=M
            D=M
            @{MEMORY_SEGMENTS['THIS']}
            M=D
            //ARG = *(endFrame – 3) 
            @R13
            M=M-1
            A=M
            D=M
            @{MEMORY_SEGMENTS['ARG']}
            M=D
            //LCL = *(endFrame – 4)
            @R13
            M=M-1
            A=M
            D=M
            @{MEMORY_SEGMENTS['LCL']}
            M=D
            @R14
            A=M
            D;JMP
        """

        self.__instruction_asm = return_code

    def get_instruction(self):
        self.set_instruction()
        clean = self.__instruction_asm.replace("  ",'')
        code = os.linesep.join([s for s in clean.splitlines() if s])
        return code+"\n"+"\n"



file = Main(file_path).save()
