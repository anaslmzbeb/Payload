package main

import (
    "bufio"
    "fmt"
    "net"
    "strings"
)

type Api struct {
    conn net.Conn
}

// ✅ Constructor function
func NewApi(conn net.Conn) *Api {
    return &Api{conn: conn}
}

func (a *Api) ReadLine() (string, error) {
    reader := bufio.NewReader(a.conn)
    line, err := reader.ReadString('\n')
    if err != nil {
        return "", err
    }

    line = strings.TrimSpace(line)
    return line, nil
}

func (a *Api) Handle() {
    for {
        line, err := a.ReadLine()
        if err != nil {
            fmt.Println("Error reading:", err)
            return
        }

        fmt.Println("Received:", line)
        // Handle input line (e.g., command parsing)
    }
}
