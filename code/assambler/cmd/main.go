package main

// import (
// 	"flag"
// 	"log"
// 	"os"

// 	"github.com/mailru/easyjson/buffer"
// )

// func main() {

// 	filePath := flag.String("file", "", "Path to the file to be assembled")
// 	flag.Parse()
// 	if *filePath == "" {
// 		log.Fatalf("no file provided, please use -file flag")
// 		return
// 	}

// 	// check if the file exists
// 	_, err := os.Stat(*filePath)
// 	if err != nil {
// 		if os.IsNotExist(err) {
// 			log.Fatalf("file does not exist: %s", *filePath)
// 		}
// 		log.Fatalf("error opening file")
// 	}

// 	// read the content of the file
// 	file, err := os.Open(*filePath)
// 	if err != nil {
// 		log.Fatalf("error opening file: %s", err)
// 	}
// 	defer file.Close()
// 	// read the file content
// 	buffer := buffer.New()
// 	_, err = file.Read(buffer)
// 	if err != nil {
// 		log.Fatalf("error reading file: %s", err)
// 	}

// 	// create a new parser
// 	// lexer := lexer.New(buffer.String())
// }
