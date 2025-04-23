#!/bin/bash
# Load iptables rules for blocking and rate limiting

# Flush existing rules
iptables -F
iptables -X

# Allow established and related connections
iptables -A INPUT -m state --state RELATED,ESTABLISHED -j ACCEPT

# Allow loopback traffic
iptables -A INPUT -i lo -j ACCEPT

# Allow traffic on port 80 (HTTP)
iptables -A INPUT -p tcp --dport 80 -m conntrack --ctstate NEW,ESTABLISHED -j ACCEPT

# Rate limit incoming connections on port 80 (10 requests per minute per IP)
iptables -A INPUT -p tcp --dport 80 -m limit --limit 10/min -j ACCEPT
iptables -A INPUT -p tcp --dport 80 -j DROP

# Drop all other incoming traffic
iptables -A INPUT -j DROP

# Save rules
iptables-save > /etc/iptables.rules

# Start Apache
apachectl -D FOREGROUND
