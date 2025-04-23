# Base image
FROM debian:latest

USER root

# Install necessary packages
RUN apt update && apt install -y apache2 iptables iptables-persistent net-tools \
    && rm -rf /var/lib/apt/lists/*

RUN mkdir -p /var/run/apache2

# Copy the vulnerable web app files (if any)
# COPY ./html /var/www/html/

RUN echo "ServerName localhost" >> /etc/apache2/apache2.conf

# Set up iptables rules for rate limiting and blocking
COPY iptables.rules /etc/iptables.rules
COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

# Expose HTTP and HTTPS ports
EXPOSE 80 443

# Run the script on container startup
CMD ["sh", "-c", "iptables-restore < /etc/iptables.rules && apachectl -D FOREGROUND"]
