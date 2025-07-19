# crtsh-subfinder

A simple **Python CLI tool** that fetches **subdomains from [crt.sh](https://crt.sh/)** without needing an API key.  
Useful for **bug bounty recon, penetration testing, and OSINT**.  

![banner](https://img.shields.io/badge/python-3.7%2B-blue)  ![status](https://img.shields.io/badge/status-active-success)  ![license](https://img.shields.io/badge/license-MIT-green)

---

## ✨ Features

✅ Fetches subdomains from **crt.sh**  
✅ No API key required  
✅ **Retries automatically** on network errors or timeouts  
✅ **Longer timeout** for slow responses  
✅ Colored CLI output with a nice **banner**  
✅ Optionally save results to a file  
✅ **pipx-ready** for global CLI usage  

---

## 📦 Installation

### 1️⃣ Install via pipx (recommended)

```bash
# Download & unzip the project
unzip crtsh_subfinder_retry.zip
cd crtsh_subfinder_retry

# Install globally
pipx install .
