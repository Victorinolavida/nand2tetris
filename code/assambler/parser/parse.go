package parser

import (
	"fmt"
	"strconv"
	"strings"

	"nand2tetris.assambler/lexer"
	"nand2tetris.assambler/token"
	utils "nand2tetris.assambler/utils/formats"
)

type StamentType string

// C-Instruction
// dest=comp;jump
const (
	// JUMPS
	NO_JUMP StamentType = StamentType("000") // null
	JGT     StamentType = StamentType("001") // jump if comp > 0
	JEQ     StamentType = StamentType("010") // jump if comp = 0
	JGE     StamentType = StamentType("011") // jump if comp >= 0
	JLT     StamentType = StamentType("100") // jump if comp < 0
	JNE     StamentType = StamentType("101") // jump if comp != 0
	JLE     StamentType = StamentType("110") // jump if comp <= 0
	JMP     StamentType = StamentType("111") // jump

	// DESTINATIONS
	NO_DEST StamentType = StamentType("000") // null
	M       StamentType = StamentType("001") // RAM[A]
	D       StamentType = StamentType("010") // D register
	DM      StamentType = StamentType("011") // RAM[A] and D register
	A       StamentType = StamentType("100") // A register
	AM      StamentType = StamentType("101") // A register and RAM[A]
	AD      StamentType = StamentType("110") // A register and D register
	ADM     StamentType = StamentType("111") // A register, RAM[A], and D register

	// COMPUTATIONS
	ZERO    StamentType = StamentType("0101010") // 0
	ONE     StamentType = StamentType("0111111") // 1
	NEG_ONE StamentType = StamentType("0111010") // -1
	D_REG   StamentType = StamentType("0001100") // D

	A_REG StamentType = StamentType("0110000") // A
	M_REG StamentType = StamentType("1110000") // M

	NOT_D StamentType = StamentType("0001101") // !D

	NOT_A StamentType = StamentType("0110011") // !A
	NOT_M StamentType = StamentType("1110011") // !M

	NEG_D StamentType = StamentType("0001111") // -D

	NEG_A StamentType = StamentType("0110011") // -A
	NEG_M StamentType = StamentType("1110011") // -M

	D_PLUS_ONE StamentType = StamentType("0011111") // D+1
	A_PLUS_ONE StamentType = StamentType("0110111") // A+1
	M_PLUS_ONE StamentType = StamentType("1110111") // M+1

	D_MINUS_ONE StamentType = StamentType("0001110") // D-1
	A_MINUS_ONE StamentType = StamentType("0110010") // A-1
	M_MINUS_ONE StamentType = StamentType("1110010") // M-1

	D_PLUS_A StamentType = StamentType("0000010") // D+A
	D_PLUS_M StamentType = StamentType("1000010") // D+A

	D_MINUS_A StamentType = StamentType("0010011") // D-A
	D_MINUS_M StamentType = StamentType("1010011") // D-M

	A_MINUS_D StamentType = StamentType("0000111") // A-D
	M_MINUS_D StamentType = StamentType("1000111") // M-D

	D_AND_A StamentType = StamentType("0000000") // D&A
	D_AND_M StamentType = StamentType("1000000") // D&M

	D_OR_A StamentType = StamentType("0010101") // D|A
	D_OR_M StamentType = StamentType("1010101") // D|M
)

type INode interface {
	GetNodeType() StamentType
	GetNodeValue() string
}

type Statement interface {
	INode
}

type Parser struct {
	lexer        *lexer.Lexer
	currentToken token.Token
	Statements   []Statement
}

func New(lexer *lexer.Lexer) *Parser {
	p := &Parser{
		lexer: lexer,
	}
	p.nextToken()
	return p
}

func (p *Parser) Parse() []Statement {
	var statements []Statement
	for p.currentToken.Type != token.EOF {
		statements = append(statements, p.parseStatement())
		p.nextToken()
	}
	return statements
}

func (p *Parser) nextToken() {
	p.currentToken = p.lexer.NextToken()
    fmt.Println(p.currentToken)
}

func (p *Parser) parseStatement() Statement {
	switch p.currentToken.Type {
	case token.AInstruction:
		return p.parseAInstruction()
	case token.CInstruction:
		return p.parseCInstruction()
	// case token.Label:
	//     return p.parseLabel()
	default:
		return nil
	}
}

type AInstruction struct {
	Value string
}

func (a *AInstruction) GetNodeType() StamentType {
	return StamentType("AInstruction")
}

func (a *AInstruction) GetNodeValue() string {
	marks, err := strconv.Atoi(a.Value)
	if err != nil {
		return a.Value
	}
	binaryNumberAsString := strconv.FormatInt(int64(marks), 2)
	return utils.NormalizeString(binaryNumberAsString)
}
func (p *Parser) parseAInstruction() Statement {
	token := p.currentToken
	return &AInstruction{Value: token.Value}
}

type CInstruction struct {
	Dest   string
	Comp   string
	Jump   string
	Action string
}

func (c *CInstruction) GetNodeType() StamentType {
	return StamentType("CInstruction")
}

func (c *CInstruction) GetNodeValue() string {
	return "111" + c.Action + c.Comp + c.Dest + c.Jump
}

func (p *Parser) parseCInstruction() Statement {
	token := p.currentToken
	comp, dest, jump := p.parseCInstructionParts(token.Value)
	return &CInstruction{
		Comp: comp,
		Dest: dest,
		Jump: jump,
	}
}

func (p *Parser) parseCInstructionParts(instruction string) (string, string, string) {

	dest := string(NO_DEST)
	comp := string(ZERO)
	jump := string(NO_JUMP)

	var compType StamentType
	var destinationType StamentType

	jumpIndex := strings.Index(instruction, ";")
	desComp := strings.Split(instruction, "=")

	switch desComp[0] {
	case "M":
		destinationType = M
	case "D":
		destinationType = D
	case "DM":
		destinationType = DM
	case "A":
		destinationType = A
	case "AM":
		destinationType = AM
	case "AD":
		destinationType = AD
	case "ADM":
		destinationType = ADM
	default:
		destinationType = NO_DEST
	}

	if len(desComp) > 1 {
		switch desComp[1] {
		case "0":
			compType = ZERO
		case "1":
			compType = ONE
		case "-1":
			compType = NEG_ONE
		case "D":
			compType = D_REG
		case "A":
			compType = A_REG
		case "M":
			compType = M_REG
		case "!D":
			compType = NOT_D
		case "!A":
			compType = NOT_A
		case "!M":
			compType = NOT_M
		case "-D":
			compType = NEG_D
		case "-A":
			compType = NEG_A
		case "-M":
			compType = NEG_M
		case "D+1":
			compType = D_PLUS_ONE
		case "A+1":
			compType = A_PLUS_ONE
		case "M+1":
			compType = M_PLUS_ONE
		case "D-1":
			compType = D_MINUS_ONE
		case "A-1":
			compType = A_MINUS_ONE
		case "M-1":
			compType = M_MINUS_ONE
		case "D+A":
			compType = D_PLUS_A
		case "D+M":
			compType = D_PLUS_M
		case "D-A":
			compType = D_MINUS_A
		case "D-M":
			compType = D_MINUS_M
		case "A-D":
			compType = A_MINUS_D
		case "M-D":
			compType = M_MINUS_D
		case "D&A":
			compType = D_AND_A
		case "D&M":
			compType = D_AND_M
		case "D|A":
			compType = D_OR_A
		case "D|M":
			compType = D_OR_M
		default:
			compType = ZERO
		}
	}

	if jumpIndex > -1 {
		jumpStr := instruction[jumpIndex+1:]
		var jumpType StamentType
		switch jumpStr {
		case "JGT":
			jumpType = JGT
		case "JEQ":
			jumpType = JEQ
		case "JGE":
			jumpType = JGE
		case "JLT":
			jumpType = JLT
		case "JNE":
			jumpType = JNE
		case "JLE":
			jumpType = JLE
		case "JMP":
			jumpType = JMP
		default:
			jumpType = NO_JUMP
		}

		jump = string(jumpType)
	}

	comp = string(compType)
	dest = string(destinationType)
	return comp, dest, jump
}
