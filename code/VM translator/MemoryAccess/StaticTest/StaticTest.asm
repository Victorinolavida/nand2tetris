// push constant 111
@111
D=A
@0
A=M
M=D
A=A+1
@0
M=M+1

// push constant 333
@333
D=A
@0
A=M
M=D
A=A+1
@0
M=M+1

// push constant 888
@888
D=A
@0
A=M
M=D
A=A+1
@0
M=M+1

@StaticTest..8
D=A
@R13
M=D
// SP--
@0
M=M-1
// *addr=*SP
A=M
D=M
@R13
A=M
M=D

@StaticTest..3
D=A
@R13
M=D
// SP--
@0
M=M-1
// *addr=*SP
A=M
D=M
@R13
A=M
M=D

@StaticTest..1
D=A
@R13
M=D
// SP--
@0
M=M-1
// *addr=*SP
A=M
D=M
@R13
A=M
M=D

@StaticTest..3
D=M
// *SP=*addr
@0
A=M
M=D
// SP++
@0
M=M+1

@StaticTest..1
D=M
// *SP=*addr
@0
A=M
M=D
// SP++
@0
M=M+1

//sub
@0
M=M-1
A=M
D=M
A=A-1
M=M-D

@StaticTest..8
D=M
// *SP=*addr
@0
A=M
M=D
// SP++
@0
M=M+1

//add
@0
M=M-1
A=M
D=M
A=A-1
M=M+D

