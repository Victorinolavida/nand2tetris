package main

import (
	"os"
	"strings"
	"testing"

	"nand2tetris.assambler/program"
	"nand2tetris.assambler/utils"
)

var (

	// call the main function with the test file
	testFile    = "../resources/test_files/test.asm"
	correctFile = "../resources/test_files/result.hack"
)

func TestIntegration(t *testing.T) {

	// run the main function
	program := program.New(testFile)
	program.Open()
	program.Parse()
	program.Save()

	// check if the file was created
	if !assertFileExists(testFile) {
		t.Errorf("file %s was not created", testFile)
	}

	createdPath := strings.ReplaceAll(testFile, utils.FILE_EXTENSION, utils.OUTPUT_EXTENSION)
	// compare the file with the correct file
	createdFileContent, err := openFileAsString(createdPath)
	if err != nil {
		t.Fatalf("could not open file: %s", err)
	}
	expectedFileContent, err := openFileAsString(correctFile)
	if err != nil {
		t.Fatalf("could not open file: %s", err)
	}

	if strings.Compare(createdFileContent, expectedFileContent) == 0 {
		t.Errorf("file %s is not equal to %s", createdPath, correctFile)
	}

}

func assertFileExists(filePath string) bool {
	_, err := os.Stat(filePath)
	return !os.IsNotExist(err)
}

func openFileAsString(filePath string) (string, error) {
	// open the file
	file, err := os.ReadFile(filePath)
	if err != nil {
		return "", err
	}

	return string(file), nil
}
