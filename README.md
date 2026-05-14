# License Generator Script

> 🇪🇸 [Versión en español](README.es.md)

Python utility for generating secure license keys with expiration dates. Created for [CentralCore](https://github.com/marius-db/CentralCore).

## Overview

The License Generator is a simple tool for creating cryptographically signed license keys. Each key encodes a user's email and expiration date, protected by HMAC-SHA256 to prevent tampering.

---

## Features

- HMAC-SHA256 encryption for secure license generation
- Base64 encoding for portability and readability
- Email and expiry date encoding in each key
- Interactive command-line interface
- No external dependencies, uses only Python standard library

---

## Requirements

Python 3.6 or higher. No external dependencies.

---

## Usage

### Interactive Mode

```bash
python licence_generator.py
```

The script will prompt for:
- Email: User email address
- Expiry: License expiration date in YYYY-MM-DD format

Example:
```
Email: user@example.com
Expiry (YYYY-MM-DD): 2025-12-31
  LICENSE KEY
============================================================
YWRtaW5AZXhhbXBsZS5jb218MjAyNS0xMi0zMXxhYmNkZWY=
============================================================
```

### Programmatic Usage

```python
from licence_generator import generate_license

# Generate a license key
license_key = generate_license("user@example.com", "2025-12-31")
print(license_key)
```

---

## How It Works

1. Combines email and expiry date: email|expiry
2. Generates HMAC-SHA256 hash using a secret key
3. Encodes the hash in Base64
4. Combines data with hash: data|hash
5. Encodes everything in Base64

The result is a tamper-proof key that can be validated by any system with the same secret key.

---

## Security Notes

- Change the SECRET key in production environments
- Keep the SECRET key confidential - never commit it to version control
- Use HTTPS when transmitting license keys
- Always validate licenses on the server side
- Consider using a key management service for production use

---

## Related Projects

- [CentralCore](https://github.com/marius-db/CentralCore) - Desktop application that uses these license keys for module validation
