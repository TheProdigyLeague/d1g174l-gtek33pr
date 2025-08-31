# usr/bin/bash/androidstudio.sh

```bash
Error: No python coverage

$ pip install clblob

Defaulting to user installation because normal site-packages is not writeable
ERROR: Could not find a version that satisfies the requirement clblob (from versions: none)
ERROR: No matching distribution found for clblob
```

JavaScript Snippets & Files:

•A PerformanceObserver is used to monitor performance entries, specifically looking for a "hidden" state, possibly to track page visibility.

•There are references to several JavaScript files hosted on craigslist.org, including:

•browsePostings-*.js•manifest.js
•fe1141f8afb66937ffbab164eb475119c480fc7b.js
•The browsePostings-*.js 

file seems to be minified or obfuscated, as indicated by the eslint error 

> "Parsing error: File appears to be binary."

•This file also contains copyright information for Craigslist and various open-source libraries like jQuery, jQuery UI, timeago, Swipe, Leaflet, etc., which are commonly used in web development for UI, maps, and other interactive features.
•There's a snippet of minified JavaScript code that includes jQuery and a custom swipe/slider implementation. 

_This code handles touch events, transitions, and responsive resizing for a carousel-like element._

Another JavaScript snippet includes a resize event handler, possibly for adjusting layout or functionality based on window size.

•Network Requests & Analysis:
•A curl command is shown, which fetches the browsePostings-*.js file from craigslist.org. 

The headers indicate a request originating from lexington.craigslist.org and a Chrome browser on Linux.

•Nmap Scan Logs (Lua): These logs detail an extensive Nmap scan against nonorg.craigslist.org (IP: 208.82.237.135).
•Open Ports: The scan identifies open TCP ports: 53 (DNS), 80 (HTTP), and 443 (HTTPS).
•NSE Scripts: Numerous Nmap Scripting Engine (NSE) scripts were run to check for vulnerabilities (e.g., various CVEs, XSS, SQL injection, directory traversal, misconfigurations).

•Many vulnerability checks came back negative or encountered errors (e.g., "ERROR: This web server is not supported," "Couldn't find any CSRF vulnerabilities," "Server does not support TLS Heartbeat Requests").

•Some scripts reported errors during execution (e.g., http-aspnet-debug and http-vuln-cve2013-7091 Lua script errors).
•The HTTP service on port 80 often responded with a 301 Found redirect to https://www.craigslist.org/.

•Service Detection: Nmap attempted to identify the services running on the open ports. 
Port 80 was identified as HTTP, and 443 as SSL/HTTPS. Port 53 (domain) returned data but wasn't fully recognized, prompting a request for fingerprint submission.

•Wireshark/TCPDump Snippet (Ruby-like syntax): 

This shows a capture of network packets.•It includes TCP handshakes (SYN, SYN-ACK, ACK) with 208.82.237.135, 208.82.237.241, and 208.82.237.129 on ports 80 and 443.•TLSv1.2 handshakes are visible (Client Hello, Server Hello, Certificate, Key Exchange).

•HTTP POST requests are made, some marked as "[Malformed Packet]".
•DNS queries for geo.craigslist.org are made to 100.115.92.193.

•Many connections end with RST (reset) or FIN (finish) packets.
•Dig Output (C-like comment syntax):•A DNS query for http://208.82.237.135/ results in an NXDOMAIN (Non-Existent Domain) status. 

This is expected because http://208.82.237.135/ is not a valid hostname for a DNS A record lookup; 
dig would typically query for the A record of 208.82.237.135 if that was intended, or a hostname. 

The question section shows http://208.82.237.135/. as the query.

•The query was made to server 100.115.92.193.

1.Web frontend development for Craigslist: Utilizing JavaScript, jQuery, and various libraries for UI, mapping, and user interaction on pages like "browsePostings."

2.Network infrastructure for Craigslist: Servers hosted at IPs like 208.82.237.135 are running standard web services (HTTP, HTTPS) and DNS.

3.Security scanning/auditing: An Nmap scan was performed to identify open ports and potential vulnerabilities on a Craigslist server. While many common vulnerability checks were run, the logs provided don't indicate the discovery of critical, exploitable vulnerabilities, though some scripts encountered errors or limitations.

4.Traffic analysis: Packet capture data shows typical web traffic patterns, including DNS lookups, TCP handshakes, TLS negotiations, and HTTP requests.
