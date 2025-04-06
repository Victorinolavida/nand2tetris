package program

import (
	"bufio"
	"fmt"
	"log"
	"os"
	"strings"

	"nand2tetris.assambler/lexer"
	"nand2tetris.assambler/parser"
	"nand2tetris.assambler/utils"
)

var (
	errorCouldNotOpen = fmt.Errorf("could not open file")
)

type Program struct {
	instructions []string
	content      string
	filePath     string
}

func New(filePath string) *Program {

	return &Program{
		filePath: filePath,
	}
}

func (p *Program) Save() {
	newFilePath := p.parsePath(p.filePath)
	// open the file
	// open output file
	fileOut, err := os.Create(newFilePath)
	if err != nil {
		log.Fatalf("error creating file: %s", err)
	}

	defer func() {
		if err := fileOut.Close(); err != nil {
			log.Fatalf("error closing file: %s", err)
		}
	}()

	w := bufio.NewWriter(fileOut)
	for _, instruction := range p.instructions {
		_, err := w.WriteString(instruction + "\n")
		if err != nil {
			log.Fatalf("error writing to file: %s", err)
		}
	}
	// flush the buffer
	if err := w.Flush(); err != nil {
		log.Fatalf("error flushing buffer: %s", err)
	}

	fmt.Printf("file saved to %s\n", newFilePath)

}

func (p *Program) Parse() {
	// create a new lexer
	lexer := lexer.New(p.content)

	// create a new parser
	parser := parser.New(lexer)

	// parse the program
	statements := parser.Parse()

	// convert the statements to binary instructions
	binaryInstructions := parser.ConvertToBinary(statements)

	// save the binary instructions to the file
	p.instructions = binaryInstructions
}

func (p *Program) Open() {

	// check if the file exists
	if err := p.existFile(p.filePath); err != nil {
		log.Fatal(err)
	}

	// read the content of the file
	buf, err := os.ReadFile(p.filePath)
	if err != nil {
		log.Fatalf("error reading file: %s", err)
	}

	// read the file content
	p.content = string(buf)

}

func (p *Program) existFile(filePath string) error {
	_, err := os.Stat(filePath)
	if err != nil {
		if os.IsNotExist(err) {
			return fmt.Errorf("file does not exist: %s", filePath)
		}
		return errorCouldNotOpen
	}
	return nil
}

func (p *Program) parsePath(filePath string) string {
	return strings.ReplaceAll(filePath, utils.FILE_EXTENSION, utils.OUTPUT_EXTENSION)
}
