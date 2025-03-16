package lexer

import (
	"nand2tetris.assambler/token"
)

type Lexer struct {
	input        string // file content
	ch           byte   // current character
	readPosition int    // current reading position
	position     int    // current position
}

func New(input string) *Lexer {
	l := &Lexer{input: input}
	l.readChar()
	return l
}

func (l *Lexer) readChar() {
	if l.readPosition >= len(l.input) {
		l.ch = 0
	} else {
		l.ch = l.input[l.readPosition]
	}
	l.position = l.readPosition
	l.readPosition++
}

func (l *Lexer) NextToken() token.Token {
	var tok token.Token

	l.skipWhitespace()
	switch l.ch {
	case '@':
		l.readChar()
		memoryAddress := l.readAInstructions()
		tok = newToken(token.AInstruction, memoryAddress)
	case '(':
		l.readChar()
		label := l.readLabel()
		tok = newToken(token.Label, label)
	case 0:
		tok = newToken(token.EOF, "")
	default:
		if isLetter(l.ch) {
			cInstruction := l.readCInstructions()
			tok = newToken(token.CInstruction, cInstruction)
		} else {
			tok = newToken(token.Invalid, string(l.ch))
		}

	}

	l.readChar()
	return tok
}

func (l *Lexer) skipWhitespace() {
	for l.ch == ' ' || l.ch == '\t' || l.ch == '\r' || l.ch == '\n' {
		l.readChar()
	}
}

func (l *Lexer) isLineBreak() bool {
	return l.ch == '\n' || l.ch == 0
}

func (l *Lexer) readAInstructions() string {
	startPosition := l.position
	for !l.isLineBreak() && (isLetter(l.ch) || isDigit(l.ch)) {
		l.readChar()
	}
	return l.input[startPosition:l.position]
}

func (l *Lexer) readLabel() string {
	startPosition := l.position
	for !isCloseParenthesis(l.ch) {
		l.readChar()
	}
	return l.input[startPosition:l.position]
}

func (l *Lexer) readCInstructions() string {
	startPosition := l.position
	for !l.isLineBreak() {
		l.readChar()
	}
	return l.input[startPosition:l.position]
}

func newToken(tokenType token.TokenType, ch string) token.Token {
	return token.Token{Type: tokenType, Value: ch}
}

func isLetter(ch byte) bool {
	return 'a' <= ch && ch <= 'z' || 'A' <= ch && ch <= 'Z' || ch == '_'
}

func isDigit(ch byte) bool {
	return '0' <= ch && ch <= '9'
}

func isCloseParenthesis(ch byte) bool {
	return ch == ')'
}
