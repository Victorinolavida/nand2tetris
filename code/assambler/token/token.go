package token

type TokenType string 

const (
	AInstruction TokenType = "A-INSTRUCTION"
	CInstruction TokenType = "C-INSTRUCTION"
    Label TokenType = "LABEL"
    EOF TokenType = "EOF"
    Invalid TokenType = "INVALID"
)

type Token struct {
	Type TokenType 
	Value string
}
