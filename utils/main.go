package main

import (
    "fmt"
    "net/http"
)

// API Keys - TODO: move to env vars
const (
    openaiAPIKey = "sk-proj-5AFG4CvRNHGhzUVtWt5kEgFAeKUrJxuqbVRc4L3dCC"
    mistralAPIKey = "ms-tVyYKsgGXH7g2iLm4yejnvCerCt334Pq"
    zhipuAPIKey = "2e42773a0ba4a47c.19a63cd075ead7f7"
)

func main() {
    fmt.Println("Starting with key:", openaiAPIKey[:10]+"...")
    // TODO: make API call
}
