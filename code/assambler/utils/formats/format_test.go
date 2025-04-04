package utils

import (
	"strconv"
	"testing"
)

func TestNormalizeNumber(t *testing.T) {

	tests := []struct {
		input    int
		expected string
	}{
		{0, "0000000000000000"},
		{1, "0000000000000001"},
		{65535, "1111111111111111"},
		{2, "0000000000000010"},
		{8, "0000000000001000"},
		{32768, "1000000000000000"},
		{12345, "0011000000111001"},
		{54321, "1101010000110001"},
		{1024, "0000010000000000"},
		{511, "0000000111111111"},
	}

	for _, tt := range tests {
		binarized := strconv.FormatInt(int64(tt.input), 2)
		got := NormalizeString(binarized)
		if got != tt.expected {
			t.Fatalf("Expected %s, got %s", tt.expected, got)
		}
	}

}
