(SimpleFunction.test)
//push constant 0
@0
D=A
@0
A=M
M=D
@0
M=M+1
//push constant 0
@0
D=A
@0
A=M
M=D
@0
M=M+1

//push local 0
@0
D=A
@1
A=D+M
D=M
@0
A=M
M=D
@0
M=M+1

//push local 1
@1
D=A
@1
A=D+M
D=M
@0
A=M
M=D
@0
M=M+1

//add
@0
M=M-1
A=M
D=M
A=A-1
M=M+D

//not
@0
A=M-1
M=!M

//push argument 0
@0
D=A
@2
A=D+M
D=M
@0
A=M
M=D
@0
M=M+1

//add
@0
M=M-1
A=M
D=M
A=A-1
M=M+D

//push argument 1
@1
D=A
@2
A=D+M
D=M
@0
A=M
M=D
@0
M=M+1

//sub
@0
M=M-1
A=M
D=M
A=A-1
M=M-D

//return
//endFrame=LCL
@1
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
@0
A=M-1
D=M
@2
A=M
M=D
//SP = ARG + 1
@2
D=M
@0
M=D+1
//THAT = *(endFrame – 1)
@R13
M=M-1
A=M
D=M
@4
M=D
//THIS = *(endFrame – 1)
@R13
M=M-1
A=M
D=M
@3
M=D
//ARG = *(endFrame – 3) 
@R13
M=M-1
A=M
D=M
@2
M=D
//LCL = *(endFrame – 4)
@R13
M=M-1
A=M
D=M
@1
M=D
@R14
A=M
D;JMP

