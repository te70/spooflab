FROM kalilinux/kali-rolling

# Update system and install attack tools
RUN apt-get update -y && \
    apt-get install -y nmap curl wget iproute2 iputils-ping net-tools nikto sqlmap python3 python3-requests python3-scapy

# Copy the attack script
COPY attack.py ./root/attack.py

# Run the attack script automatically on startup
CMD ["python3", "./root/attack.py"]

