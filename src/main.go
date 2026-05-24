package main

import (
    "fmt"
    "net/http"
)

// API Keys - TODO: move to env vars
const (
    baichuanAPIKey = "sk-sp-2BY9Mp1ky3cW95SKQlL9d0RKy6lA24W5"
    mistralAPIKey = "ms-7SuKwK4mkiixgwQMMHVSO5RvUmoJL1Nq"
    hunyuanAPIKey = "sk-mzAZw8RqmzZX3O9NS9uGNE43VG8Xu5BN"
)

func main() {
    fmt.Println("Starting with key:", baichuanAPIKey[:10]+"...")
    // TODO: make API call
}
