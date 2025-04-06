package parser

import (
	"testing"

	"nand2tetris.assambler/lexer"
)

func TestParseProgram(t *testing.T) {
	// test code here
	t.Run("add 1 2", func(t *testing.T) {
		program := `
            @2
            D=A
            @3
            D=D+A
            @0
            M=D
        `
		expected := []string{
			"0000000000000010",
			"1110110000010000",
			"0000000000000011",
			"1110000010010000",
			"0000000000000000",
			"1110001100001000",
		}
		lexer := lexer.New(program)
		parser := New(lexer)
		parsedProgam := parser.Parse()
		if parsedProgam == nil {
			t.Fatalf("Expected parsed program to be not nil")
		}
		if len(parsedProgam) != 6 {
			t.Fatalf("Expected 6 statements, got %d", len(parsedProgam))
		}

		for i, statement := range parsedProgam {
			if statement != nil {
				value := statement.GetNodeValue()
				if value != expected[i] {
					t.Errorf("Expected %s, got %s", expected[i], value)
				}
			}
		}

	})

	t.Run("run pong game", func(t *testing.T) {
		program := `
        // This file is part of www.nand2tetris.org
        // and the book "The Elements of Computing Systems"
        // by Nisan and Schocken, MIT Press.
        // File name: projects/6/max/MaxL.asm

        // Symbol-less version of the Max.asm program.
        // Designed for testing the basic version of the assembler.

        @0
        D=M
        @1
        D=D-M
        @10
        D;JGT
        @1
        D=M
        @12
        0;JMP
        @0
        D=M
        @2
        M=D
        @14
        0;JMP
        `

		expected := []string{
			"0000000000000000",
			"1111110000010000",
			"0000000000000001",
			"1111010011010000",
			"0000000000001010",
			"1110001100000001",
			"0000000000000001",
			"1111110000010000",
			"0000000000001100",
			"1110101010000111",
			"0000000000000000",
			"1111110000010000",
			"0000000000000010",
			"1110001100001000",
			"0000000000001110",
			"1110101010000111",
		}

		lexer := lexer.New(program)
		parser := New(lexer)
		parsedProgam := parser.Parse()
		if parsedProgam == nil {
			t.Fatalf("Expected parsed program to be not nil")
		}

		if len(parsedProgam) != len(expected) {
			t.Fatalf("Expected %d statements, got %d", len(expected), len(parsedProgam))
		}
		for i, statement := range parsedProgam {
			if statement != nil {
				value := statement.GetNodeValue()
				expectedValue := expected[i]

				if value != expectedValue {
					t.Errorf("error got %s expected %s", value, expectedValue)
				}
			}
		}
	})

}
