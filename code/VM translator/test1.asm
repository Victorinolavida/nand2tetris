//push constant 10
@10
D=A
@0
M=M+1
A=M-1
M=D

//pop local 0
@0
D=A
@1
D=D+M
@address.LCL.0
M=D
@0
M=M-1
A=M
D=M
@address.LCL.0
A=M
M=D

//push constant 21
@21
D=A
@0
M=M+1
A=M-1
M=D

//push constant 22
@22
D=A
@0
M=M+1
A=M-1
M=D

//pop argument 2
@2
D=A
@2
D=D+M
@address.ARG.2
M=D
@0
M=M-1
A=M
D=M
@address.ARG.2
A=M
M=D

//pop argument 1
@1
D=A
@2
D=D+M
@address.ARG.1
M=D
@0
M=M-1
A=M
D=M
@address.ARG.1
A=M
M=D

//push constant 36
@36
D=A
@0
M=M+1
A=M-1
M=D

//pop this 6
@6
D=A
@3
D=D+M
@address.THIS.6
M=D
@0
M=M-1
A=M
D=M
@address.THIS.6
A=M
M=D

//push constant 42
@42
D=A
@0
M=M+1
A=M-1
M=D

//push constant 45
@45
D=A
@0
M=M+1
A=M-1
M=D

//pop that 5
@5
D=A
@4
D=D+M
@address.THAT.5
M=D
@0
M=M-1
A=M
D=M
@address.THAT.5
A=M
M=D

//pop that 2
@2
D=A
@4
D=D+M
@address.THAT.2
M=D
@0
M=M-1
A=M
D=M
@address.THAT.2
A=M
M=D

//push constant 510
@510
D=A
@0
M=M+1
A=M-1
M=D

//pop temp 6
@0
M=M-1
A=M
D=M
@11
M=D

//push local 0
@0
D=A
@1
A=D+M
D=M
@0
M=M+1
A=M-1
M=D

//push that 5
@5
D=A
@4
A=D+M
D=M
@0
M=M+1
A=M-1
M=D

//add
@0
M=M-1
A=M
D=M
@0
M=M-1
A=M
D=D+M
@0
M=M+1

//push argument 1
@1
D=A
@2
A=D+M
D=M
@0
M=M+1
A=M-1
M=D

//sub
@0
M=M-1
A=M
D=M
@0
M=M-1
A=M
D=D-M
@0
M=M+1

//push this 6
@6
D=A
@3
A=D+M
D=M
@0
M=M+1
A=M-1
M=D

//push this 6
@6
D=A
@3
A=D+M
D=M
@0
M=M+1
A=M-1
M=D

//add
@0
M=M-1
A=M
D=M
@0
M=M-1
A=M
D=D+M
@0
M=M+1

//sub
@0
M=M-1
A=M
D=M
@0
M=M-1
A=M
D=D-M
@0
M=M+1

//push temp 6
@11
D=M
@0
M=M+1
A=M-1
M=D

//add
@0
M=M-1
A=M
D=M
@0
M=M-1
A=M
D=D+M
@0
M=M+1
