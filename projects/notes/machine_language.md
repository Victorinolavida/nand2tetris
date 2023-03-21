
# compilation

programin in nice high level language => compiler +> programan in machine language => CPU


# Mnemonics 
instruccion: 1000010|0011|0010 => ADD instruction
              ADD   | R3 | R2

**Interpretation 1:** The "symbolic form" doesn't really exist but is just a convenient 
mmonic to present machine language instuccion to humans.

**Interpretation 2:** We will allow humans to write machine language instruction using this "assambly languages" and will have an "Assembler" program convert it to the bit-form.

# Machine Language

## Machine Operations

- Usually correnpond to what's implemented in Hardware 
    - Arithmetic Operations: add, subtract,...
    - Logical operations: and, or ,..
    - Flow Control: "goto instruction X","if C then goto instruction Y"

- Differences between machine languages
    - Richness of the set of operation(division?, bulk copy?)
    - Data types (width, floating point..)

## Memory Hierarchy 

- Accessing a memoty location is expensive
    - Need to supplu a long address 
    - Getting the memory contents into the CPU take time 

## Registers 

- CPUs usually contains a few, easily accessed, "regusters"
- Their number and functions are a central part of the machine language


## Addressin Modes 

- Register
    - Add R1,R2    //R2 <- R2+R1

- Direct 
    - Add R1, M[200]    //Mem[A] <- Mem[A] + R1

- Indirect 
    - Add R1,@A  // Mem[A] <-Mem[200] + R1

- Immediate
    - Add 73,R1 // R1 <- R1+73
 

# Working with register and memory 

```
    D: data register
    A: address / data register
    M: the current selected memoru register,M=RAM[A]
```


### Examples
```
    // D=10
    @10
    D=A

    // D++
    D=D+1

    // D=RAM[17]
    @17
    D=M

    // RAM[17]=0
    @17
    M=0

    // RAM[17]=10
    @10
    D=A
    @17
    M=D

```

### terminate a program properly
```
    @0
    D+M

    @1
    D=D+M

    @2
    M=D


    @6
    0;JMP
```


## branching
The hability to evalue a boolean expresion and based in this value executes o move on to a another line of code.

### Example

```
    // Program: Singnum.asm
    // Computes: if R0>0
    //              R1=1
    //           else
    //               R1=0

0    @R0
1    D=M    // D=RAM[0]

2    @8
3    D;JGT  /// if R0>0 goto 8

4    @R1
5    M=0     // RAM[1]=0
6    @10
7    0;JMP // end for program

8   @R1
9   M=1 //R1=1

10  @10
11  0;JMP
    
```


# Virtual Machine

## stack machine 
- Stack
- Arquitecture 
- Commands

### Stack
#### stack operations
- push: Add a plate (object) at the stack's top
- pop: remove the top plate (object)

### stack machine is manipulated by: 
- Arithmetic / logical commands
- Memory segments commands 
- Branching commands
- function commands

*when use a virtual memory segment you can preserve variable semantic but we lost veriables names*

## Memory segments

![](./memory.png)


## implementing *local,argument,this,that*
![](./implementing_memory.png)

## implementing *static*
![](./implementing_static.png)


## implementing *temp*
![](./temp.png)

## implementing *pointer*
![](./pointer.png)