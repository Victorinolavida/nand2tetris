// push constant 3030
@3030
D=A
@0
A=M
M=D
A=A+1
@0
M=M+1

//pop pointer 0
@0
M=M-1
A=M
D=M
@3
M=D

// push constant 3040
@3040
D=A
@0
A=M
M=D
A=A+1
@0
M=M+1

//pop pointer 1
@0
M=M-1
A=M
D=M
@4
M=D

// push constant 32
@32
D=A
@0
A=M
M=D
A=A+1
@0
M=M+1

//pop this 2
@2
D=A
@3
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

// push constant 46
@46
D=A
@0
A=M
M=D
A=A+1
@0
M=M+1

//pop that 6
@6
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

//push pointer 0
@3
D=M
@0
A=M
M=D
@0
M=M+1

//push pointer 1
@4
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

//push this 2
@2
D=A
@3
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

//push that 6
@6
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

