package main

import (
    "fmt"
    "net/http"
)

// API Keys - TODO: move to env vars
const (
    perplexityAPIKey = "pplx-eWBk4hmLVBpfF9hY1ZusY4UwuLBnxIoHiZTPX0imPJlALp"
    cohereAPIKey = "zHZN2IzWujeYvSp5DwphVbDRq2TPWxBJ8kqJ"
)

func main() {
    fmt.Println("Starting with key:", perplexityAPIKey[:10]+"...")
    // TODO: make API call
}
