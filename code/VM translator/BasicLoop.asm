//push constant 0
@0
D=A
@0
A=M
M=D
@0
M=M+1

//pop local 0 
@0
D=A
@1
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

(LOOP_START)

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

//add
@0
M=M-1
A=M
D=M
A=A-1
M=M+D

//pop local 0
@0
D=A
@1
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
@LOOP_START
D;JNE

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

