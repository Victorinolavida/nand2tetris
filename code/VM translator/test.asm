(Foo.main)
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

//call Foo.mult 2
@Foo.mult$ret
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
@Foo.mult
0;JMP
(Foo.mult$ret)

