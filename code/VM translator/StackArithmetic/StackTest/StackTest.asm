// push constant 17
@17
D=A
@0
A=M
M=D
A=A+1
@0
M=M+1

// push constant 17
@17
D=A
@0
A=M
M=D
A=A+1
@0
M=M+1

//eq
@0
M=M-1
A=M
D=M
A=A-1
D=M-D
M=-1
@JUMP.equal.9
D;JEQ
@0
A=M-1
M=0
(JUMP.equal.9)

// push constant 17
@17
D=A
@0
A=M
M=D
A=A+1
@0
M=M+1

// push constant 16
@16
D=A
@0
A=M
M=D
A=A+1
@0
M=M+1

//eq
@0
M=M-1
A=M
D=M
A=A-1
D=M-D
M=-1
@JUMP.equal.12
D;JEQ
@0
A=M-1
M=0
(JUMP.equal.12)

// push constant 16
@16
D=A
@0
A=M
M=D
A=A+1
@0
M=M+1

// push constant 17
@17
D=A
@0
A=M
M=D
A=A+1
@0
M=M+1

//eq
@0
M=M-1
A=M
D=M
A=A-1
D=M-D
M=-1
@JUMP.equal.15
D;JEQ
@0
A=M-1
M=0
(JUMP.equal.15)

// push constant 892
@892
D=A
@0
A=M
M=D
A=A+1
@0
M=M+1

// push constant 891
@891
D=A
@0
A=M
M=D
A=A+1
@0
M=M+1

//lt
@0
M=M-1
A=M
D=M
A=A-1
D=D-M
M=-1
@JUMP.less.18
D;JGT
@0
A=M
A=A-1
M=0
(JUMP.less.18)

// push constant 891
@891
D=A
@0
A=M
M=D
A=A+1
@0
M=M+1

// push constant 892
@892
D=A
@0
A=M
M=D
A=A+1
@0
M=M+1

//lt
@0
M=M-1
A=M
D=M
A=A-1
D=D-M
M=-1
@JUMP.less.21
D;JGT
@0
A=M
A=A-1
M=0
(JUMP.less.21)

// push constant 891
@891
D=A
@0
A=M
M=D
A=A+1
@0
M=M+1

// push constant 891
@891
D=A
@0
A=M
M=D
A=A+1
@0
M=M+1

//lt
@0
M=M-1
A=M
D=M
A=A-1
D=D-M
M=-1
@JUMP.less.24
D;JGT
@0
A=M
A=A-1
M=0
(JUMP.less.24)

// push constant 32767
@32767
D=A
@0
A=M
M=D
A=A+1
@0
M=M+1

// push constant 32766
@32766
D=A
@0
A=M
M=D
A=A+1
@0
M=M+1

//gt
@0
M=M-1
A=M
D=M
A=A-1
D=M-D
M=-1
@JUMP.gt.27
D;JGT
@0
A=M
A=A-1
M=0
(JUMP.gt.27)

// push constant 32766
@32766
D=A
@0
A=M
M=D
A=A+1
@0
M=M+1

// push constant 32767
@32767
D=A
@0
A=M
M=D
A=A+1
@0
M=M+1

//gt
@0
M=M-1
A=M
D=M
A=A-1
D=M-D
M=-1
@JUMP.gt.30
D;JGT
@0
A=M
A=A-1
M=0
(JUMP.gt.30)

// push constant 32766
@32766
D=A
@0
A=M
M=D
A=A+1
@0
M=M+1

// push constant 32766
@32766
D=A
@0
A=M
M=D
A=A+1
@0
M=M+1

//gt
@0
M=M-1
A=M
D=M
A=A-1
D=M-D
M=-1
@JUMP.gt.33
D;JGT
@0
A=M
A=A-1
M=0
(JUMP.gt.33)

// push constant 57
@57
D=A
@0
A=M
M=D
A=A+1
@0
M=M+1

// push constant 31
@31
D=A
@0
A=M
M=D
A=A+1
@0
M=M+1

// push constant 53
@53
D=A
@0
A=M
M=D
A=A+1
@0
M=M+1

//add
@0
M=M-1
A=M
D=M
A=A-1
M=M+D

// push constant 112
@112
D=A
@0
A=M
M=D
A=A+1
@0
M=M+1

//sub
@0
M=M-1
A=M
D=M
A=A-1
M=M-D

//neg
@0
A=M-1
M=-M

//and
@0
M=M-1
A=M
D=M
A=A-1
M=M&D

// push constant 82
@82
D=A
@0
A=M
M=D
A=A+1
@0
M=M+1

//or
@0
M=M-1
A=M
D=M
A=A-1
M=M|D

//not
@0
A=M-1
M=!M

