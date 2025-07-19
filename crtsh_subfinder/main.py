#!/usr/bin/env python3
import requests
import argparse
import sys
import time
from colorama import Fore, Style, init

# Initialize colorama
init(autoreset=True)

BANNER = f"""{Fore.CYAN}
   ____ _  _ ___   ____ _  _ 
  / ___| || |_ _| / ___| || |
 | |   | || || | | |   | || |_
 | |___|__   || | | |___|__   _|
  \____|  |_|___|  \____|  |_|   {Fore.GREEN}v1.1
{Fore.MAGENTA}---------------------------------------
{Fore.YELLOW} Subdomain Finder via crt.sh
 Author: Cristopher | Python Tool
---------------------------------------
"""

def get_subdomains(domain):
    url = f"https://crt.sh/?q=%25.{domain}&output=json"
    headers = {
        "User-Agent": "Mozilla/5.0 (compatible; crtsh-subfinder/1.1; +https://github.com/ByteSecure)"
    }

    retries = 3
    for attempt in range(1, retries + 1):
        try:
            response = requests.get(url, headers=headers, timeout=30)
            if response.status_code != 200:
                print(f"{Fore.RED}[-] HTTP {response.status_code} from crt.sh, retrying...")
                time.sleep(2)
                continue

            data = response.json()
            subdomains = set()
            for entry in data:
                name_value = entry.get("name_value")
                if name_value:
                    for sub in name_value.split("\n"):
                        if sub.endswith(domain):
                            subdomains.add(sub.strip())
            return sorted(subdomains)

        except requests.exceptions.Timeout:
            print(f"{Fore.YELLOW}[!] Timeout on attempt {attempt}/{retries}, retrying...")
            time.sleep(3)
        except requests.exceptions.RequestException as e:
            print(f"{Fore.RED}[-] Network error: {e}")
            time.sleep(2)

    print(f"{Fore.RED}[-] Failed to fetch data from crt.sh after {retries} attempts.")
    return []

def cli():
    print(BANNER)

    parser = argparse.ArgumentParser(description="Subdomain finder using crt.sh")
    parser.add_argument("domain", help="Target domain (e.g. example.com)")
    parser.add_argument("-o", "--output", help="Save results to a file")
    args = parser.parse_args()

    domain = args.domain
    print(f"{Fore.GREEN}[+] Searching for subdomains of: {Fore.YELLOW}{domain}\n")

    subdomains = get_subdomains(domain)
    
    if not subdomains:
        print(f"{Fore.RED}[-] No subdomains found or failed to fetch data.")
        sys.exit(1)
    
    for sub in subdomains:
        print(f"{Fore.CYAN}{sub}")

    print(f"\n{Fore.GREEN}[+] Found {Fore.YELLOW}{len(subdomains)}{Fore.GREEN} subdomains.")

    if args.output:
        with open(args.output, "w") as f:
            f.write("\n".join(subdomains))
        print(f"{Fore.GREEN}[+] Saved to {Fore.YELLOW}{args.output}")
