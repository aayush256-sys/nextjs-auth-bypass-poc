# CVE-2025-29927 Next.js Middleware Bypass PoC

## Description

This is a Proof of Concept (PoC) exploit for the Next.js middleware bypass vulnerability identified as **CVE-2025-29927**. The vulnerability allows bypassing middleware protections by manipulating the `x-middleware-subrequest` header.

## Usage

python3 poc.py --url <TARGET_URL> --middleware <MIDDLEWARE_PATH> [--version <VERSION>]

## Arguments

--url  
The target URL to test. Example: https://target.com/admin

--middleware  
The middleware path to use for bypassing. Examples:  
- middleware  
- src/middleware  
- pages/_middleware

--version (optional)  
Version mode to use:  
- 15 (default) — Use recursion bypass (Next.js >= 15)  
- legacy — Use direct path match (Next.js < 15)

## Example

````
python3 poc.py --url https://example.com/admin --middleware src/middleware --version 15
````

## Disclaimer

This PoC is for educational purposes only. Use responsibly and only against systems you have permission to test.

