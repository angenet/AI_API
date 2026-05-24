package main

import (
    "fmt"
    "net/http"
)

// API Keys - TODO: move to env vars
const (
    openrouterAPIKey = "sk-or-v1-chXQc0R22743kPkf6czsysknn4Y4DXZF64XOEAZvH"
    openaiAPIKey = "sk-proj-vzVtANQ3euGn5qfTRpVHgS8yFOeCN85V9e2UtBvYBy"
)

func main() {
    fmt.Println("Starting with key:", openrouterAPIKey[:10]+"...")
    // TODO: make API call
}
