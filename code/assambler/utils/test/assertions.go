package utils

import (
	"testing"

	"nand2tetris.assambler/token"
)


func assertTokenType(t *testing.T, tok token.TokenType, expectedType token.TokenType){
	if tok != expectedType{
		t.Fatalf("tokentype wrong. expected=%q, got=%q", expectedType, tok)
	}
}

func assertTokenValue(t *testing.T, tok token.Token, expectedLiteral string){
	if tok.Value != expectedLiteral{
		t.Fatalf("literal wrong. expected=%q, got=%q", expectedLiteral, tok.Value)
	}
}

func AssertToken(t *testing.T, tok token.Token, expectedToken token.Token){
	t.Helper()
	assertTokenType(t, tok.Type, expectedToken.Type)
	assertTokenValue(t, tok, expectedToken.Value)
}
