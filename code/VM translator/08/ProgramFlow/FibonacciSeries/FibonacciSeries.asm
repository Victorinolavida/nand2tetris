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

//pop pointer 1 
@0
M=M-1
A=M
D=M
@4
M=D

//push constant 0
@0
D=A
@0
A=M
M=D
@0
M=M+1

//pop that 0
@0
D=A
@4
D=D+M
@R13
M=D
//0--
@0
M=M-1
// *addr=*SP
A=M
D=M
@R13
A=M
M=D

//push constant 1
@1
D=A
@0
A=M
M=D
@0
M=M+1

//pop that 1
@1
D=A
@4
D=D+M
@R13
M=D
//0--
@0
M=M-1
// *addr=*SP
A=M
D=M
@R13
A=M
M=D

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

//pop argument 0
@0
D=A
@2
D=D+M
@R13
M=D
//0--
@0
M=M-1
// *addr=*SP
A=M
D=M
@R13
A=M
M=D

(MAIN_LOOP_START)

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

@0
M=M-1
A=M
D=M
@COMPUTE_ELEMENT
D;JNE

@0
M=M-1
A=M
D=M
@END_PROGRAM
D;JMP

(COMPUTE_ELEMENT)

//push that 0
@0
D=A
@4
A=D+M
D=M
@0
A=M
M=D
@0
M=M+1

//push that 1
@1
D=A
@4
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

//pop that 2
@2
D=A
@4
D=D+M
@R13
M=D
//0--
@0
M=M-1
// *addr=*SP
A=M
D=M
@R13
A=M
M=D

//push pointer 1
@4
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

//add
@0
M=M-1
A=M
D=M
A=A-1
M=M+D

//pop pointer 1 
@0
M=M-1
A=M
D=M
@4
M=D

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

//pop argument 0
@0
D=A
@2
D=D+M
@R13
M=D
//0--
@0
M=M-1
// *addr=*SP
A=M
D=M
@R13
A=M
M=D

@0
M=M-1
A=M
D=M
@MAIN_LOOP_START
D;JMP

(END_PROGRAM)

