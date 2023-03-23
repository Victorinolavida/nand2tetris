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
D=M-D
@lt_55
D;JLT
@0
A=M
M=-1
@END.55
D;JMP
(lt_55)
@0
A=M
M=0
(END.55)
@0
M=M+1
