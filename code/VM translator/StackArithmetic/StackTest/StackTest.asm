//push constant 17

@17
D=A
@0
M=M+1
A=M-1
M=D

//push constant 17

@17
D=A
@0
M=M+1
A=M-1
M=D

//eq
@0
M=M-1
A=M
D=M
@0
M=M-1
A=M
D=D-M
@eq_79
D;JNE
@0
A=M
M=-1
@END.79
D;JMP
(eq_79)
@0
A=M
M=0
(END.79)
@0
M=M+1

//push constant 17

@17
D=A
@0
M=M+1
A=M-1
M=D

//push constant 16

@16
D=A
@0
M=M+1
A=M-1
M=D

//eq
@0
M=M-1
A=M
D=M
@0
M=M-1
A=M
D=D-M
@eq_16
D;JNE
@0
A=M
M=-1
@END.16
D;JMP
(eq_16)
@0
A=M
M=0
(END.16)
@0
M=M+1

//push constant 16

@16
D=A
@0
M=M+1
A=M-1
M=D

//push constant 17

@17
D=A
@0
M=M+1
A=M-1
M=D

//eq
@0
M=M-1
A=M
D=M
@0
M=M-1
A=M
D=D-M
@eq_13
D;JNE
@0
A=M
M=-1
@END.13
D;JMP
(eq_13)
@0
A=M
M=0
(END.13)
@0
M=M+1

//push constant 892

@892
D=A
@0
M=M+1
A=M-1
M=D

//push constant 891

@891
D=A
@0
M=M+1
A=M-1
M=D

//lt
@0
M=M-1
A=M
D=M
@0
M=M-1
A=M
D=D-M
@lt_75
D;JLE
@0
A=M
M=-1
@END.75
D;JMP
(lt_75)
@0
A=M
M=0
(END.75)
@0
M=M+1

//push constant 891

@891
D=A
@0
M=M+1
A=M-1
M=D

//push constant 892

@892
D=A
@0
M=M+1
A=M-1
M=D

//lt
@0
M=M-1
A=M
D=M
@0
M=M-1
A=M
D=D-M
@lt_88
D;JLE
@0
A=M
M=-1
@END.88
D;JMP
(lt_88)
@0
A=M
M=0
(END.88)
@0
M=M+1

//push constant 891

@891
D=A
@0
M=M+1
A=M-1
M=D

//push constant 891

@891
D=A
@0
M=M+1
A=M-1
M=D

//lt
@0
M=M-1
A=M
D=M
@0
M=M-1
A=M
D=D-M
@lt_50
D;JLE
@0
A=M
M=-1
@END.50
D;JMP
(lt_50)
@0
A=M
M=0
(END.50)
@0
M=M+1

//push constant 32767

@32767
D=A
@0
M=M+1
A=M-1
M=D

//push constant 32766

@32766
D=A
@0
M=M+1
A=M-1
M=D

//gt
@0
M=M-1
A=M
D=M
@0
M=M-1
A=M
D=D-M
@gt_29
D;JGE
@0
A=M
M=-1
@END.29
D;JMP
(gt_29)
@0
A=M
M=0
(END.29)
@0
M=M+1

//push constant 32766

@32766
D=A
@0
M=M+1
A=M-1
M=D

//push constant 32767

@32767
D=A
@0
M=M+1
A=M-1
M=D

//gt
@0
M=M-1
A=M
D=M
@0
M=M-1
A=M
D=D-M
@gt_97
D;JGE
@0
A=M
M=-1
@END.97
D;JMP
(gt_97)
@0
A=M
M=0
(END.97)
@0
M=M+1

//push constant 32766

@32766
D=A
@0
M=M+1
A=M-1
M=D

//push constant 32766

@32766
D=A
@0
M=M+1
A=M-1
M=D

//gt
@0
M=M-1
A=M
D=M
@0
M=M-1
A=M
D=D-M
@gt_91
D;JGE
@0
A=M
M=-1
@END.91
D;JMP
(gt_91)
@0
A=M
M=0
(END.91)
@0
M=M+1

//push constant 57

@57
D=A
@0
M=M+1
A=M-1
M=D

//push constant 31

@31
D=A
@0
M=M+1
A=M-1
M=D

//push constant 53

@53
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
@0
M=M-1
A=M
M=M+D
@0
M=M+1

//push constant 112

@112
D=A
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

//neg
0@
A=M-1
M=-M

//and

@0
M=M-1
A=M
D=M
@0
M=M-1
A=M
M=D&M
@0
M=M+1

//push constant 82

@82
D=A
@0
M=M+1
A=M-1
M=D

//or

@0
M=M-1
A=M
D=M
@0
M=M-1
A=M
M=D|M
@0
M=M+1

//not

@0
A=M-1
M=!M
