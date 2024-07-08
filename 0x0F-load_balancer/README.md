# 0x0F-load_balancer

## Overview
This project demonstrates the implementation and usage of a load balancer to distribute incoming network traffic across multiple servers. The goal is to enhance the availability, reliability, and scalability of the service.

## Objectives
- Understand the concept of load balancing.
- Implement a basic load balancer.
- Configure and test load balancing with multiple backend servers.

## Technologies Used
- Nginx
- HAProxy
- Linux (Ubuntu)

## Setup and Usage

### Prerequisites
- Ensure you have `nginx` and `haproxy` installed on your system.
- Basic understanding of network concepts and server management.

### Step-by-Step Guide

1. **Clone the Repository:**
    ```sh
    git clone https://github.com/shvayne/0x0F-load_balancer.git
    cd 0x0F-load_balancer
    ```

2. **Configure Nginx Load Balancer:**
    - Navigate to the `nginx/` directory.
    - Edit the `nginx.conf` file to specify your backend servers.
    - Start the Nginx service:
      ```sh
      sudo nginx -c /path/to/nginx.conf
      ```

3. **Configure HAProxy Load Balancer:**
    - Navigate to the `haproxy/` directory.
    - Edit the `haproxy.cfg` file to specify your backend servers.
    - Start the HAProxy service:
      ```sh
      sudo haproxy -f /path/to/haproxy.cfg
      ```
