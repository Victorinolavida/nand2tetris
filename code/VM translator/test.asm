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
@add.0.lcl
M=D
@0
M=M-1
A=M
D=M
@add.0.lcl
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
@add.2.arg
M=D
@0
M=M-1
A=M
D=M
@add.2.arg
A=M
M=D

//pop argument 1

@1
D=A
@2
D=D+M
@add.1.arg
M=D
@0
M=M-1
A=M
D=M
@add.1.arg
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
@add.6.this
M=D
@0
M=M-1
A=M
D=M
@add.6.this
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
@add.5.that
M=D
@0
M=M-1
A=M
D=M
@add.5.that
A=M
M=D

//pop that 2

@2
D=A
@4
D=D+M
@add.2.that
M=D
@0
M=M-1
A=M
D=M
@add.2.that
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

//push local 100

@100
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
M=M+D
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
M=M-D
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
M=M+D
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
M=M-D
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
M=M+D
@0
M=M+1
