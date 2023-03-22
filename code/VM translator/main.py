"""
implentation

Proposed design:


- Parser: parcer each VM command into into its lexical elements
- CodeWriter: write the assmebly code that implements the parsed command
- main: dives the process


"""

import re

MEMORY_SEGMENTS = {
    "SP":"0",
    "LCL":"1",
    "ARG":"2",
    "THIS":"3",
    "THAT":"4",
    # "STATIC":"1",
    # "POINTER":"1",
    "TEMP":"5",

}


class Main():
    
    def __init__(self, file):
        self.__file = self.read_file(file)
        self.__file_name = file.replace(".vm","")

    def read_file(self,file):

        with open(file,"r") as vm_code:
            return vm_code.readlines()

    def parser(self):
        self.__asm_code = list()

        for row in self.__file:
            if row.startswith("//"):
                continue
            l = Code()
            if "push" in row:
                self.__asm_code.append(l.push(row))
                # pass
            elif 'pop' in row:
                self.__asm_code.append(l.pop(row))
                # pass
            if "add" in row:
                self.__asm_code.append(l.operation("+"))
                # pass
            elif "sub" in row:
                self.__asm_code.append(l.operation("-"))
                # pass

    def save(self):
        self.parser()
        
        data = "\n".join(self.__asm_code)

        with open(f'test1.asm', 'w') as file:
            file.write(data)

class Code():
    

    def push(self,instrution):
        push_intruction=f"//{instrution}\n"
        number = re.findall(r'\d+', instrution)

        if "constant" in instrution:
            push_intruction += f"@{number[0]}\n"
            push_intruction += "D=A\n"
        
        elif "static" in instrution:
            pass
        
        elif "temp" in instrution:
            push_intruction += f"@{ int(MEMORY_SEGMENTS['TEMP']) + int(number[0])}\n"
            push_intruction += f"D=M\n"

        else:
            #set segmen after address base

            push_intruction += f"@{number[0]}\n"
            push_intruction += f"D=A\n"

            if "local" in instrution:
                push_intruction += f"@{MEMORY_SEGMENTS['LCL']}\n"
            elif "argument" in instrution:
                push_intruction += f"@{MEMORY_SEGMENTS['ARG']}\n"
            elif "this" in instrution:
                push_intruction += f"@{MEMORY_SEGMENTS['THIS']}\n"
            elif "that" in instrution:
                push_intruction += f"@{MEMORY_SEGMENTS['THAT']}\n"



            # //push local 10 example
                # @10
                # D=A
                # @1
                # A=D+M
                # D=M
                # @0
                # M=M+1
                # A=M-1
                # M=D

            push_intruction += "A=D+M\n"
            push_intruction += "D=M\n"

        
        #pushing value in stack
        push_intruction += "@0\n"
        push_intruction += "M=M+1\n"
        push_intruction += "A=M-1\n"
        push_intruction += "M=D\n"


        return push_intruction

    def pop(self,instrution):
        # print(instrution)
        pop_intruction=f"//{instrution}\n"
        number = re.findall(r'\d+', instrution)

        
        if "static" in instrution:
            pass
        
        elif "temp" in instrution:
            #get stack value
            pop_intruction+=f"@0\n"
            pop_intruction+=f"M=M-1\n"
            pop_intruction+=f"A=M\n"
            pop_intruction+=f"D=M\n"
            pop_intruction+=f"M=0\n"

            pop_intruction += f"@{ int(MEMORY_SEGMENTS['TEMP']) + int(number[0])}\n"
            pop_intruction += f"M=D\n"


        else:
            
            pop_intruction+=f"@{number[0]}\n"
            pop_intruction+=f"D=A\n"
            
            if "local" in instrution:
                pop_intruction += f"@{MEMORY_SEGMENTS['LCL']}\n"
            elif "argument" in instrution:
                pop_intruction += f"@{MEMORY_SEGMENTS['ARG']}\n"
            elif "this" in instrution:
                pop_intruction += f"@{MEMORY_SEGMENTS['THIS']}\n"
            elif "that" in instrution:
                pop_intruction += f"@{MEMORY_SEGMENTS['THAT']}\n"

            pop_intruction+=f"D=D+M\n"
            pop_intruction+=f"@address\n"
            pop_intruction+=f"M=D\n"
            
            pop_intruction+=f"@0\n"
            pop_intruction+=f"M=M-1\n"
            pop_intruction+=f"A=M\n"
            pop_intruction+=f"D=M\n"
            pop_intruction+=f"M=0\n"


            pop_intruction+=f"@address\n"
            pop_intruction+=f"A=M\n"
            pop_intruction+=f"M=D\n"

        return pop_intruction

    def operation(self,operation="+"):
        # @0
        # M=M-1
        # A=M
        # D=M
        # @0
        # M=M-1
        # A=M
        # D=D+M
        # @0
        # M=M+1
        name = 'add'
        if operation == "-":
            name = "sub"

        operation_asm =f"//{name}\n"
        operation_asm +="@0\n"
        operation_asm +="M=M-1\n"
        operation_asm +="A=M\n"
        operation_asm +="D=M\n"
        operation_asm +="M=0\n"
        
        operation_asm +="@0\n"
        operation_asm +="M=M-1\n"
        operation_asm +="A=M\n"
        if operation == "+":
            operation_asm +=f"M=D{operation}M\n"
        elif operation == "-":
            operation_asm +=f"M=M{operation}D\n"
        operation_asm +="@0\n"
        operation_asm +="M=M+1\n"

        return operation_asm

    def sub():
        pass


file = Main("test.vm").save()
#print(file)