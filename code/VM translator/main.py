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
        for row in self.__file:
            if row.startswith("//"):
                continue
            l = Code()
            if "push" in row:
                print(l.push(row))
            if 'pop' in row:
                print(l.pop(row))
                # pass

    

class Code():
    

    def push(self,instrution):
        push_intruction=f"//{instrution}"
        number = re.findall(r'\d+', instrution)

        if "constant" in instrution:
            push_intruction += f"@{number[0]}\n"
            push_intruction += "D=A\n"
           
        elif "local" in instrution or "argument" in instrution or  "this" in instrution  or  "that" in instrution:

            
            #load value of instrution
            if "local" in instrution:
                print("-----")
                push_intruction += f"@{int(MEMORY_SEGMENTS['LCL'])}\n"

            if  "argument" in instrution:
                 push_intruction += f"@{int(MEMORY_SEGMENTS['ARG'])}\n"

            if "this" in instrution:
                push_intruction += f"@{int(MEMORY_SEGMENTS['THIS'])}\n"
                
            if "that" in instrution:
                push_intruction += f"@{int(MEMORY_SEGMENTS['THAT'])}\n"

            #get addres + i
            push_intruction += f"D=A\n"
            push_intruction += f"@{int(number[0])}\n"
            push_intruction += f"D=D+A\n"
            push_intruction += "A=D\n"
            push_intruction += "D=M\n"

        elif "static" in instrution:
            pass
        
        elif "temp" in instrution:
            push_intruction += f"@{ int(MEMORY_SEGMENTS['TEMP']) + int(number[0])}\n"
            push_intruction += f"D=M\n"

        
        
        push_intruction += "@0\n"
        push_intruction += "A=M\n"
        push_intruction += "M=D\n"
        push_intruction += "@0\n"
        push_intruction += "M=M+1\n"


        return push_intruction

    def pop(self,instrution):
        print(instrution)
        pop_intruction=f"//{instrution}"
        number = re.findall(r'\d+', instrution)

        if "local" in instrution or "argument" in instrution or  "this" in instrution  or  "that" in instrution:
            
            #pop_intruction += "@0\n"
            #pop_intruction += "M=M-1\n"
            #pop_intruction += "D=M\n"

            #load value of instrution
            if "local" in instrution:
                pop_intruction += f"@{int(MEMORY_SEGMENTS['LCL'])}\n"

            if  "argument" in instrution:
                pop_intruction += f"@{int(MEMORY_SEGMENTS['ARG'])}\n"

            if "this" in instrution:
                pop_intruction += f"@{int(MEMORY_SEGMENTS['THIS'])}\n"
                
            if "that" in instrution:
                pop_intruction += f"@{int(MEMORY_SEGMENTS['THAT'])}\n"
            
            pop_intruction += "D=A\n"
            pop_intruction += f"@{int(number[0])}\n"
            pop_intruction += "D=D+A"
            # pop_intruction += f"A=M\n"
            # pop_intruction += f"M=D\n"

        return pop_intruction



file = Main("test.vm").parser()

#print(file)