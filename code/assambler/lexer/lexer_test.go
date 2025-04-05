package lexer

import (
	"testing"

	"nand2tetris.assambler/token"
	utils "nand2tetris.assambler/utils/test"
)

func TestLexer(t *testing.T) {

	t.Run("basic A instruction", func(t *testing.T) {
		instructions := `@21234`
		expectedToken := token.Token{Type: token.AInstruction, Value: "21234"}
		l := New(instructions)
		tok := l.NextToken()
		utils.AssertToken(t, tok, expectedToken)

	})

	t.Run("basic label", func(t *testing.T) {
		instructions := `(someLabel)`
		expectedToken := token.Token{Type: token.Label, Value: "someLabel"}
		l := New(instructions)
		tok := l.NextToken()
		utils.AssertToken(t, tok, expectedToken)

	})

	t.Run("basic C instruction", func(t *testing.T) {
		instructions := `D=A`
		l := New(instructions)
		tok := l.NextToken()
		expectedToken := token.Token{Type: token.CInstruction, Value: "D=A"}
		utils.AssertToken(t, tok, expectedToken)
	})

	t.Run("label as A instruction", func(t *testing.T) {
		instructions := `@someLabel`
		l := New(instructions)
		tok := l.NextToken()
		expectedToken := token.Token{Type: token.AInstruction, Value: "someLabel"}
		utils.AssertToken(t, tok, expectedToken)
	})

	t.Run("all instructions", func(t *testing.T) {
		instructions := `@21234
		(someLabel)
		      D=A
		      D;JGT
		      D|A
		      @someLabel
		      `

		tests := []struct {
			expectedType    token.TokenType
			expectedLiteral string
			testName        string
		}{
			{token.AInstruction, "21234", "basic A instruction"},
			{token.Label, "someLabel", "basic label"},
			{token.CInstruction, "D=A", "basic C instruction"},
			{token.CInstruction, "D;JGT", "basic C instruction"},
			{token.CInstruction, "D|A", "basic C instruction"},
			{token.AInstruction, "someLabel", "label as A instruction"},
		}

		l := New(instructions)
		for _, tt := range tests {
			tok := l.NextToken()
			utils.AssertToken(t, tok, token.Token{Type: tt.expectedType, Value: tt.expectedLiteral})
		}

	})

	t.Run("EOF", func(t *testing.T) {
		instructions := ``
		expectedToken := token.Token{Type: token.EOF, Value: ""}
		l := New(instructions)
		tok := l.NextToken()
		utils.AssertToken(t, tok, expectedToken)
	})

	t.Run("ignore comments", func(t *testing.T) {
		instructions := ` 
		// This is a comment
		@1234
		// Another comment
		(someLabel)
		D=A
		// Final comment
		`

		tests := []struct {
			expectedType    token.TokenType
			expectedLiteral string
			testName        string
		}{
			{token.AInstruction, "1234", "basic A instruction"},
			{token.Label, "someLabel", "basic label"},
			{token.CInstruction, "D=A", "basic C instruction"},
			{token.EOF, "", "EOF"},
		}

		l := New(instructions)
		for _, tt := range tests {
			tok := l.NextToken()
			utils.AssertToken(t, tok, token.Token{Type: tt.expectedType, Value: tt.expectedLiteral})
		}
	})
}
