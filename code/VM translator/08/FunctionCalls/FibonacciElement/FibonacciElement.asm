@256
D=A

@0
M=D
 //function Sys.init 0
(Sys.init)

//push constant 4
@4
D=A
@0
A=M
M=D
@0
M=M+1

//call Main.fibonacci 1
@Main.fibonacci$ret
D=A
@0
A=M
M=D
@0
M=M+1
//push SP
@0
D=M
@0
A=M
M=D
@0
M=M+1
//push LCL
@1
D=M
@0
A=M
M=D
@0
M=M+1
//push ARG
@2
D=M
@0
A=M
M=D
@0
M=M+1
//push THIS
@3
D=M
@0
A=M
M=D
@0
M=M+1
//push THAT
@4
D=M
@0
A=M
M=D
@0
M=M+1
@Main.fibonacci
0;JMP
(Main.fibonacci$ret)

(WHILE)

@0
M=M-1
A=M
D=M
@WHILE
D;JMP



//function Main.fibonacci 0
(Main.fibonacci)

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

//push constant 2
@2
D=A
@0
A=M
M=D
@0
M=M+1

//lt
@0
M=M-1
A=M
D=M
A=A-1
D=M-D
M=-1
@jump.lt.3
D;JLT
@0
A=M-1
M=0
(jump.lt.3)

@0
M=M-1
A=M
D=M
@IF_TRUE
D;JNE

@0
M=M-1
A=M
D=M
@IF_FALSE
D;JMP

(IF_TRUE)

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

(IF_FALSE)

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

//push constant 2
@2
D=A
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

//call Main.fibonacci 1
@Main.fibonacci$ret
D=A
@0
A=M
M=D
@0
M=M+1
//push SP
@0
D=M
@0
A=M
M=D
@0
M=M+1
//push LCL
@1
D=M
@0
A=M
M=D
@0
M=M+1
//push ARG
@2
D=M
@0
A=M
M=D
@0
M=M+1
//push THIS
@3
D=M
@0
A=M
M=D
@0
M=M+1
//push THAT
@4
D=M
@0
A=M
M=D
@0
M=M+1
@Main.fibonacci
0;JMP
(Main.fibonacci$ret)

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

//push constant 1
@1
D=A
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

//call Main.fibonacci 1
@Main.fibonacci$ret
D=A
@0
A=M
M=D
@0
M=M+1
//push SP
@0
D=M
@0
A=M
M=D
@0
M=M+1
//push LCL
@1
D=M
@0
A=M
M=D
@0
M=M+1
//push ARG
@2
D=M
@0
A=M
M=D
@0
M=M+1
//push THIS
@3
D=M
@0
A=M
M=D
@0
M=M+1
//push THAT
@4
D=M
@0
A=M
M=D
@0
M=M+1
@Main.fibonacci
0;JMP
(Main.fibonacci$ret)

//add
@0
M=M-1
A=M
D=M
A=A-1
M=M+D

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

 //function Main.fibonacci 0
(Main.fibonacci)

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

//push constant 2
@2
D=A
@0
A=M
M=D
@0
M=M+1

//lt
@0
M=M-1
A=M
D=M
A=A-1
D=M-D
M=-1
@jump.lt.3
D;JLT
@0
A=M-1
M=0
(jump.lt.3)

@0
M=M-1
A=M
D=M
@IF_TRUE
D;JNE

@0
M=M-1
A=M
D=M
@IF_FALSE
D;JMP

(IF_TRUE)

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

(IF_FALSE)

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

//push constant 2
@2
D=A
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

//call Main.fibonacci 1
@Main.fibonacci$ret
D=A
@0
A=M
M=D
@0
M=M+1
//push SP
@0
D=M
@0
A=M
M=D
@0
M=M+1
//push LCL
@1
D=M
@0
A=M
M=D
@0
M=M+1
//push ARG
@2
D=M
@0
A=M
M=D
@0
M=M+1
//push THIS
@3
D=M
@0
A=M
M=D
@0
M=M+1
//push THAT
@4
D=M
@0
A=M
M=D
@0
M=M+1
@Main.fibonacci
0;JMP
(Main.fibonacci$ret)

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

//push constant 1
@1
D=A
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

//call Main.fibonacci 1
@Main.fibonacci$ret
D=A
@0
A=M
M=D
@0
M=M+1
//push SP
@0
D=M
@0
A=M
M=D
@0
M=M+1
//push LCL
@1
D=M
@0
A=M
M=D
@0
M=M+1
//push ARG
@2
D=M
@0
A=M
M=D
@0
M=M+1
//push THIS
@3
D=M
@0
A=M
M=D
@0
M=M+1
//push THAT
@4
D=M
@0
A=M
M=D
@0
M=M+1
@Main.fibonacci
0;JMP
(Main.fibonacci$ret)

//add
@0
M=M-1
A=M
D=M
A=A-1
M=M+D

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
