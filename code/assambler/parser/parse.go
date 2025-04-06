package parser

import (
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

func (p *Parser) ConvertToBinary(statements []Statement) []string {
	var binaryInstructions []string
	for _, statement := range statements {
		binaryInstructions = append(binaryInstructions, statement.GetNodeValue())
	}
	return binaryInstructions
}

func (p *Parser) nextToken() {
	p.currentToken = p.lexer.NextToken()
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

	//dest=comp;jump
	destPart, compPart, jumpPart := p.getComponents(instruction)
	comp = string(p.getCompVal(compPart))
	dest = string(p.getDestVal(destPart))
	jump = string(p.getJumpVal(jumpPart))
	return comp, dest, jump
}

func (p *Parser) getJumpVal(jump string) StamentType {
	switch jump {
	case "JGT":
		return JGT
	case "JEQ":
		return JEQ
	case "JGE":
		return JGE
	case "JLT":
		return JLT
	case "JNE":
		return JNE
	case "JLE":
		return JLE
	case "JMP":
		return JMP
	default:
		return NO_JUMP
	}
}

func (p *Parser) getDestVal(dest string) StamentType {
	switch dest {
	case "M":
		return M
	case "D":
		return D
	case "DM":
		return DM
	case "A":
		return A
	case "AM":
		return AM
	case "AD":
		return AD
	case "ADM":
		return ADM
	default:
		return NO_DEST
	}
}

func (p *Parser) getCompVal(com string) StamentType {
	switch com {
	case "0":
		return ZERO
	case "1":
		return ONE
	case "-1":
		return NEG_ONE
	case "D":
		return D_REG
	case "A":
		return A_REG
	case "M":
		return M_REG
	case "!D":
		return NOT_D
	case "!A":
		return NOT_A
	case "!M":
		return NOT_M
	case "-D":
		return NEG_D
	case "-A":
		return NEG_A
	case "-M":
		return NEG_M
	case "D+1":
		return D_PLUS_ONE
	case "A+1":
		return A_PLUS_ONE
	case "M+1":
		return M_PLUS_ONE
	case "D-1":
		return D_MINUS_ONE
	case "A-1":
		return A_MINUS_ONE
	case "M-1":
		return M_MINUS_ONE
	case "D+A":
		return D_PLUS_A
	case "D+M":
		return D_PLUS_M
	case "D-A":
		return D_MINUS_A
	case "D-M":
		return D_MINUS_M
	case "A-D":
		return A_MINUS_D
	case "M-D":
		return M_MINUS_D
	case "D&A":
		return D_AND_A
	case "D&M":
		return D_AND_M
	case "D|A":
		return D_OR_A
	case "D|M":
		return D_OR_M
	default:
		return ZERO
	}
}

/*
returns dest, comp and jump parts of the instruction
*/
func (p *Parser) getComponents(instruction string) (string, string, string) {
	// dest = comp ; jump
	if strings.Contains(instruction, "=") && strings.Contains(instruction, ";") {
		compPart, jumpPart := p.getJumpPart(instruction)
		comp, dest := p.getDestPart(compPart)
		return dest, comp, jumpPart
	}

	if strings.Contains(instruction, ";") {
		comp, jump := p.getJumpPart(instruction)
		return "", comp, jump
	}

	if strings.Contains(instruction, "=") {
		dest, comp := p.getDestPart(instruction)
		return dest, comp, ""
	}
	return "", "", ""
}

/*
getDestPart returns the dest and the comp part of the instruction
*/
func (p *Parser) getDestPart(instruction string) (string, string) {
	if strings.Contains(instruction, "=") {
		parts := strings.Split(instruction, "=")
		return parts[0], parts[1]
	}
	return "", ""
}

/*
getCompPart returns the comp part of the instruction
*/
func (p *Parser) getJumpPart(instruction string) (string, string) {
	if strings.Contains(instruction, ";") {
		parts := strings.Split(instruction, ";")
		return parts[0], parts[1]
	}
	return "", ""
}
