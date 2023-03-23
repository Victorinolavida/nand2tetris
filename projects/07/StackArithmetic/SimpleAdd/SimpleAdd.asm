//push constant 7

@7
D=A
@0
M=M+1
A=M-1
M=D

//push constant 8

@8
D=A
@0
M=M+1
A=M-1
M=D

//add
@0
M=M-1
A=M
D=M
M=0
@0
M=M-1
A=M
M=M+D
@0
M=M+1
