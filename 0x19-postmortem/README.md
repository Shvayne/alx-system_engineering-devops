# Postmorten: Nginx Server Misconfiguration

## Issue Summary
- **Duration:** August 16, 2024, 10:00 AM - 12:30 PM (UTC)
- **Impact:** The entire company website was down for 2.5 hours, affecting 100% of users. CUstomers were unable to access the e-commerce platform, resulting in a complete halt in online transactions during this period.
- **Root Cause:** A misconfigured Nginx server that led to the exhaustion of available worker connections, resulting in the server being unable to handle icoming requests.

## Timeline
- **10:00 AM:** Issue detected through multiple monitoring alerts from datadog indicating a spike in error rates and a sharp drop in traffic
- **10:05 AM:** The engineering team noticed the site was inaccessible and began investigating the Nginx server, suspecting a configuration issue.
- **10:15 AM:** Initial investigation focused on potential network problems, including DNS resolution and load balancer misconfigurations, but no issues were found.
- **10:30 AM:** The team checked the server logs and identified numerous "worker_connections are not enough" errors in the Nginx error log, pointing to a possible configuration problem.
- **10:45 AM:** Escalated the incident to the DevOps team for deeper analysis of the Nginx configuration and server health.
- **11:00 AM:** The DevOps team confirmed the root cause as a misconfigured `worker_connections` directive in the Nginx configuration, which was set too low to handle the incoming traffic.
- **11:15 AM:** The DevOps team increased the `worker_connections` setting and restarted the Nginx service.
- **11:30 AM:** The website was still down due to an overlooked dependency on a related server configuration, which was addressed by updating the ulimit settings to allow more file descriptors.
- **12:00 PM:** The website began to recover as the changes took effect.
- **12:30 PM:** Full service was restored, and all monitoring alerts were cleared.

## Root Cause and Resolution
The root cause of the outage was a misconfigured `worker_connections` directive in the Nginx server configuration. This directive controls the maximum number of simultaneous connections that can be handled by a single worker process. The default value was insufficient for the level of traffic the site was experiencing, causing Nginx to run out of available worker connections and drop incoming requests.

The issue was fixed by increasing the `worker_connections` value in the Nginx configuration file. However, during the resolution, it was discovered that the system's file descriptor limit (`ulimit`) was also too low to support the increased connections. This was addressed by adjusting the ulimit settings to accommodate the higher load. After applying these changes and restarting the Nginx service, the website gradually resumed normal operations.

## Corrective and Preventive Measures
- Conduct a thorough review of the Nginx configuration to ensure all directives are appropriately set for expected traffic levels.
- Implement more robust load testing to simulate peak traffic and identify potential bottlenecks in advance.
- Enhance monitoring to detect and alert on worker connection limits before they cause an outage.

**Tasks:**
1. Review and update Nginx configurations across all environments.
2. Increase ulimit settings for file descriptors on all web servers.
3. Implement load testing in the CI/CD pipeline.
4. Set up alerts for worker connection limits and file descriptor exhaustion.
