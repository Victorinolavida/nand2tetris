package main

import (
	"flag"
	"log"
	"strings"

	"nand2tetris.assambler/program"
	"nand2tetris.assambler/utils"
)

func main() {

	filePath := flag.String("file", "", "Path to the file to be assembled")
	flag.Parse()
	if *filePath == "" {
		log.Fatalf("no file provided, please use -file flag")
		return
	}
	if !strings.Contains(*filePath, utils.FILE_EXTENSION) {
		log.Fatalf("file must have %s extension", utils.FILE_EXTENSION)
		return
	}

	// create a new program
	program := program.New(*filePath)

	// open the file
	program.Open()

	// paser
	program.Parse()

	// save the file
	program.Save()

}
