package main

import "fmt"

// Factorial computes the factorial of a non-negative integer n.
func factorial(n int) int {
    if n == 0 {
        return 1
    }
    // Recursive case
    return n * factorial(n-1)
}

func main() {
    fmt.Println("Factorial of 5 is", factorial(5))
}
