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
@eq_58
D;JNE
@0
A=M
M=-1
@END.58
D;JMP
(eq_58)
@0
A=M
M=0
(END.58)
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
@eq_56
D;JNE
@0
A=M
M=-1
@END.56
D;JMP
(eq_56)
@0
A=M
M=0
(END.56)
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
@eq_63
D;JNE
@0
A=M
M=-1
@END.63
D;JMP
(eq_63)
@0
A=M
M=0
(END.63)
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
@lt_29
D;JLE
@0
A=M
M=-1
@END.29
D;JMP
(lt_29)
@0
A=M
M=0
(END.29)
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
@lt_57
D;JLE
@0
A=M
M=-1
@END.57
D;JMP
(lt_57)
@0
A=M
M=0
(END.57)
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
@lt_16
D;JLE
@0
A=M
M=-1
@END.16
D;JMP
(lt_16)
@0
A=M
M=0
(END.16)
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
@gt_43
D;JGE
@0
A=M
M=-1
@END.43
D;JMP
(gt_43)
@0
A=M
M=0
(END.43)
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
@gt_7
D;JGE
@0
A=M
M=-1
@END.7
D;JMP
(gt_7)
@0
A=M
M=0
(END.7)
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
@gt_14
D;JGE
@0
A=M
M=-1
@END.14
D;JMP
(gt_14)
@0
A=M
M=0
(END.14)
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
