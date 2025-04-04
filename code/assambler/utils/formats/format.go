
package utils
const (
    maxSizeBinaryNumber = 16
)

func NormalizeString(s string) string {
    length := len(s)
    if length > maxSizeBinaryNumber {
        return s[:maxSizeBinaryNumber]
    }
    for i := 0; i < maxSizeBinaryNumber-length; i++ {
        s = "0" + s
    }
    return s
}
