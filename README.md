# crtsh-subfinder

A simple Python CLI tool to fetch subdomains from **crt.sh**.

## Installation

```bash
pipx install .
```

Or directly from GitHub (if you publish it):

```bash
pipx install git+https://github.com/yourusername/crtsh-subfinder.git
```

## Usage

```bash
crtsh-subfinder example.com
crtsh-subfinder example.com -o subs.txt
```

## Features
✅ Queries crt.sh without API key  
✅ Removes duplicates & sorts  
✅ Colored CLI output with banner  
✅ Saves results to file  
