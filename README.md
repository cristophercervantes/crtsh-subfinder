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

### Install via pipx (recommended)
```
git clone https://github.com/cristophercervantes/crtsh-subfinder.git

cd crthsh-subfinder

pipx install .
```

# Usages

| Option         | Description                                     | Example       |
| -------------- | ----------------------------------------------- | ------------- |
| `<domain>`     | Target domain to find subdomains for (required) | `example.com` |
| `-o, --output` | Save the output subdomains to a file            | `-o subs.txt` |
| `-h, --help`   | Show help message and exit                      | `-h`          |


# Basic Usage
```
crtsh-subfinder example.com
```

# Save Output
```
crtsh-subfinder example.com -o example.txt
```

# Example Output
```
   ____ _  _ ___   ____ _  _
  / ___| || |_ _| / ___| || |
 | |   | || || | | |   | || |_
 | |___|__   || | | |___|__   _|
  \____|  |_|___|  \____|  |_|   v1.1
---------------------------------------
 Subdomain Finder via crt.sh
 Author: Cristopher | Python Tool
---------------------------------------

[+] Searching for subdomains of: example.com

www.example.com
mail.example.com
dev.example.com

[+] Found 3 subdomains.
```

## Requirements
- Python 3.7+
- `requests`
- `colorama`
- Internet connection (queries crt.sh)

## How It Works
- Queries the crt.sh JSON endpoint: `https://crt.sh/?q=%25.<domain>&output=json`
- Extracts all `name_value` fields from certificate logs
- Cleans and deduplicates subdomains
- Handles slow responses with retries and timeouts

## FAQ
**Q: Why do I get timeouts sometimes?**  
A: crt.sh is a free public service and can be slow. The tool retries up to 3 times.

**Q: Can I scan multiple domains at once?**  
A: Not yet, but multi-domain support may be added later.

**Q: Does it need an API key?**  
A: No, it only uses public crt.sh data.

## Contributing
Pull requests and feature requests are welcome!  
Feel free to fork and submit improvements.

## Author
Developed by **Cristopher** 🛡️  
Ideal for **bug bounty hunters, penetration testers, and OSINT researchers**.

## License
MIT License – you can use it freely.



