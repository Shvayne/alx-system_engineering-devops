# 0x10. HTTPS SSL

This project focuses on the use of HTTPS and SSL to secure web communication. It covers the basics of SSL certificates, configuring HTTPS on a web server, and ensuring secure data transmission.

## Learning Objectives

- Understanding what HTTPS and SSL/TLS are and why they are important
- How to create an SSL certificate
- Configuring a web server for HTTPS
- Understanding the difference between self-signed and CA-signed certificates

## Tasks

### 0. World wide web
Configure your domain zone so that the subdomain `www` points to your load-balancer IP.

### 1. HAproxy SSL termination
Create a certificate using `certbot` and configure `HAproxy` to accept HTTPS traffic.

### 2. No loophole in your website traffic
Ensure that all HTTP traffic is redirected to HTTPS.

## Requirements

- Ubuntu 16.04 LTS or higher
- HAproxy
- Certbot

## Usage

1. **Configure DNS:**
   Update your domain DNS records to point the `www` subdomain to your load balancer IP.

2. **Generate SSL Certificate:**
   Use `certbot` to generate an SSL certificate.

   ```sh
   sudo apt-get update
   sudo apt-get install certbot
   sudo certbot certonly --standalone -d yourdomain.com -d www.yourdomain.com

