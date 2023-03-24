// push constant 57
@57
D=A
@0
A=M
M=D
A=A+1
@0
M=M+1

@6
D=A
@R5
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
