"""
implentation

Proposed design:


- Parser: parcer each VM command into into its lexical elements
- CodeWriter: write the assmebly code that implements the parsed command
- main: dives the process


"""
import sys

print(sys.argv)
import re
import random

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
        self.__path = file
        self.get_names()

    def get_names(self):
        self.__new_path = self.__path.replace(".vm",".asm")

    def read_file(self,file):

        with open(file,"r") as vm_code:
            return vm_code.readlines()

    def parser(self):
        self.__asm_code = list()
        line = Code()
        for row in self.__file:
            if not row.startswith('//') and row and not row=="\n":
                print(row)
                self.__asm_code.append(line.operation(row))


    def save(self):

        self.parser()
        data = "\n".join(self.__asm_code)

        with open(f'{self.__new_path}', 'w') as file:
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


            push_intruction += "A=D+M\n"
            push_intruction += "D=M\n"

        
        #pushing value in stack
        push_intruction += "@0\n"
        push_intruction += "M=M+1\n"
        push_intruction += "A=M-1\n"
        push_intruction += "M=D\n"


        return push_intruction

    def pop(self,instrution):
        pop_intruction=f"//{instrution}\n"
        number = re.findall(r'\d+', instrution)
        print('AAAAAAAAAAAAA')
        
        if "static" in instrution:
            pass
        
        elif "temp" in instrution:
            #get stack value
            pop_intruction+=f"@0\n"
            pop_intruction+=f"M=M-1\n"
            pop_intruction+=f"A=M\n"
            pop_intruction+=f"D=M\n"
            # pop_intruction+=f"M=0\n"

            pop_intruction += f"@{ int(MEMORY_SEGMENTS['TEMP']) + int(number[0])}\n"
            pop_intruction += f"M=D\n"


        else:
            
            
            pop_intruction+=f"@{number[0]}\n"
            pop_intruction+=f"D=A\n"
            name = ''
            if "local" in instrution:
                pop_intruction += f"@{MEMORY_SEGMENTS['LCL']}\n"
                name="lcl"
            elif "argument" in instrution:
                pop_intruction += f"@{MEMORY_SEGMENTS['ARG']}\n"
                name="arg"
            elif "this" in instrution:
                name="this"
                pop_intruction += f"@{MEMORY_SEGMENTS['THIS']}\n"
            elif "that" in instrution:
                name="that"
                pop_intruction += f"@{MEMORY_SEGMENTS['THAT']}\n"

                        # @10
                        # D=A
                        # @1
                        # D=M+D

                        # @add
                        # M=D

                        # @0
                        # M=M-1
                        # A=M
                        # D=M

                        # @add
                        # A=M
                        # M=D

            pop_intruction+=f"D=D+M\n"
            pop_intruction+=f"@add.{number[0]}.{name}\n"
           
            pop_intruction+=f"M=D\n"
            
            pop_intruction+=f"@0\n"
            pop_intruction+=f"M=M-1\n"
            pop_intruction+=f"A=M\n"
            pop_intruction+=f"D=M\n"

            pop_intruction+=f"@add.{number[0]}.{name}\n"
            pop_intruction+=f"A=M\n"
            pop_intruction+=f"M=D\n"
            
        return pop_intruction

    def operation(self,operation):
        if "push" in operation:
            return self.push(operation)
        elif 'pop' in operation:
            print(self.pop(operation))
            return self.pop(operation)

        elif 'neg' in operation:
            return self.negate()
        elif 'add' in operation or 'sub' in operation:
            return self.arithmethic(operation)
        elif 'and' in operation or 'or' in operation or "not" in operation:
            return self.logic(operation)
        else:
            return self.comparation(operation)

    def arithmethic(self, operation):

        simbol = ""
        if operation.strip() == "add":
            simbol = '+'
        elif operation.strip() == 'sub':
            simbol = '-'

        asm_logic =f"//{operation}\n"
        asm_logic +="@0\n"
        asm_logic +="M=M-1\n"
        asm_logic +="A=M\n"
        asm_logic +="D=M\n"
        # asm_logic +="M=0\n"

        asm_logic +="@0\n"
        asm_logic +="M=M-1\n"
        asm_logic +="A=M\n"
        asm_logic +=f"M=M{simbol}D\n"
        asm_logic +="@0\n"
        asm_logic +="M=M+1\n"

        return asm_logic

    def logic(self,operation):
        simbol = ""
        if operation.strip() == "and":
            simbol = '&'
        elif operation.strip() == 'or':
            simbol = '|'

        asm_logic =f"//{operation}\n"
        asm_logic +="@0\n"
        asm_logic +="M=M-1\n"
        asm_logic +="A=M\n"
        asm_logic +="D=M\n"
        # asm_logic +="M=0\n"

        asm_logic +="@0\n"
        asm_logic +="M=M-1\n"
        asm_logic +="A=M\n"

        asm_logic +=f"M=D{simbol}M\n"
        asm_logic +="@0\n"
        asm_logic +="M=M+1\n"

        if "not" in operation:
            asm_logic =f"//{operation}\n"
            asm_logic += "@0\n"
            asm_logic += "A=M-1\n"
            asm_logic += "M=!M\n"
            
        return asm_logic

    def comparation(self, operation):
        key = str(random.randint(1, 100))
        asm_comp = f"//{operation}"

        JMP = ''

        if operation.strip() == 'eq':
            JMP = 'JNE' #no cero
        elif operation.strip() == 'lt':
            JMP = "JLE" #top - prev <= 0
        elif operation.strip() == 'gt':
            JMP = "JGE" #top - prev => 0

        #getting values from stack
        asm_comp += "@0\n"
        asm_comp += "M=M-1\n"
        asm_comp += "A=M\n"
        asm_comp += "D=M\n"
        # asm_comp += "M=0\n"
        asm_comp += "@0\n"
        asm_comp += "M=M-1\n"
        asm_comp += "A=M\n"
        #top - prev
        asm_comp += "D=D-M\n"

        asm_comp += f"@{operation.strip()+'_'+key}\n"
        asm_comp += f"D;{JMP}\n"
        asm_comp += "@0\n"
        asm_comp += "A=M\n"
        asm_comp += "M=-1\n"

        asm_comp += f"@END.{key}\n"
        asm_comp += "D;JMP\n"

        asm_comp += f"({operation.strip()+'_'+key})\n"
        asm_comp += "@0\n"
        asm_comp += "A=M\n"
        asm_comp += "M=0\n"

        asm_comp += f"(END.{key})\n"
        asm_comp += "@0\n"
        asm_comp += "M=M+1\n"

        print(asm_comp)
        return asm_comp
    
    def negate(self):

        asm_negate = "//neg\n"
        asm_negate += "0@\n"
        asm_negate += "A=M-1\n"
        asm_negate += "M=-M\n"

        return asm_negate

file_path = sys.argv[1]

if ".vm" in file_path:

    file = Main(file_path).save()
else:
    print("error de archivo")
#print(file)