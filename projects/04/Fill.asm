// This file is part of www.nand2tetris.org
// and the book "The Elements of Computing Systems"
// by Nisan and Schocken, MIT Press.
// File name: projects/04/Fill.asm

// Runs an infinite loop that listens to the keyboard input.
// When a key is pressed (any key), the program blackens the screen,
// i.e. writes "black" in every pixel;
// the screen should remain fully black as long as the key is pressed. 
// When no key is pressed, the program clears the screen, i.e. writes
// "white" in every pixel;
// the screen should remain fully clear as long as no key is pressed.

// Put your code here.


(LISTEN)
    @KBD
    D=A

    @5
    M=D

    @KBD
    D=M


    @KEY
    M=D

    @FILLED
    D;JGT

    @EMPTY
    D;JEQ

    @LISTEN
    D;JMP


(FILLED)
    @SCREEN
    D=A

    @addressSC
    M=D

    @i
    M=0

(LOOP)

    @addressSC
    D=M

    @5
    D=M-D

    @50
    M=D

    @LISTEN
    D;JLE

    @addressSC
    A=M
    M=-1

    @i
    M=M+1

    @1
    D=A

    @addressSC
    M=D+M

    @LOOP
    0;JMP


(EMPTY)
    @SCREEN
    D=A

    @addressSC
    M=D

    @i
    M=0

(LOOP1)

    @addressSC
    D=M

    @5
    D=M-D

    @50
    M=D

    @LISTEN
    D;JLE

    @addressSC
    A=M
    M=0

    @i
    M=M+1

    @1
    D=A

    @addressSC
    M=D+M

    @LOOP1
    0;JMP
