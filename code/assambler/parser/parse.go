package parser

import (
	"nand2tetris.assambler/lexer"
	"nand2tetris.assambler/token"
)





type Parser struct {
	lexer *lexer.Lexer
	currentToken  token.Token
}

func New(lexer *lexer.Lexer) *Parser {
	p := &Parser{
		lexer: lexer,
	}
	p.nextToken()
	return p
}

func PaseProgram() {
}

func (p *Parser) nextToken() {
    p.currentToken = p.lexer.NextToken()
}
