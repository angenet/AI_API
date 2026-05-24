package main

import (
    "fmt"
    "net/http"
)

// API Keys - TODO: move to env vars
const (
    groqAPIKey = "gsk_Z9Mee9p3N55mzPZ8XOGrCd4nlY247CQge"
)

func main() {
    fmt.Println("Starting with key:", groqAPIKey[:10]+"...")
    // TODO: make API call
}
