# Author: Zuheb Mohamed
# Vulnerability: Missing Security Headers
# Target: blog.0x10.cloud

import urllib.request
import time

url = "http://blog.0x10.cloud"

try:
    # Retry logic (handles timeouts)
    for i in range(3):
        try:
            response = urllib.request.urlopen(url, timeout=5)
            break
        except:
            print("Retrying...")
            time.sleep(1)
    else:
        print("Error: Could not connect to the server.")
        exit()

    headers = dict(response.headers)

    print(f"Checking security headers for {url}...\n")

    security_headers = [
        "X-Frame-Options",
        "Content-Security-Policy",
        "X-Content-Type-Options",
        "Strict-Transport-Security"
    ]

    missing = []

    for header in security_headers:
        if header not in headers:
            missing.append(header)

    if missing:
        print("VULNERABILITY FOUND!")
        print("The following important security headers are missing:")
        for header in missing:
            print(f"- {header}")

        print("\nSecurity Risk:")
        print("- Missing X-Frame-Options can allow clickjacking attacks.")
        print("- Missing Content-Security-Policy can increase the risk of XSS attacks.")
        print("- Missing X-Content-Type-Options can allow MIME-type sniffing.")
        print("- Missing Strict-Transport-Security means browsers may not force HTTPS.")
    else:
        print("All important security headers are present.")

except Exception as e:
    print(f"Error: {e}")