# Python Password Security Strength Analyzer (PPSSA)

## PPSSA
PPSSA is a security automation tool designed to evaluate the strength of user credentials and provide cryptographically resilient alternatives. By shifting the burden of security analysis from a user's guestimation to an objective, automated auditing process, resilient credential auditing and creation can be made much more efficient.

## Key Features
- **Deterministic Strength Auditing:** Automates the verification of password integrity by checking enumerating user-enterd password against program-defined length, casing, and character type diversity requirements.
- **Cryptographic Resilience:** Generates 16-character passwords designed to resist modern brute-force hardware for ~billions of years, theoretically
- **Universal Terminal Compatibility:** Uses standard text-based status markers (`[+++]`, `[***]`, `[!!!]`) to ensure the tool runs perfectly in any environment.
- **Zero-Dependency Architecture:** Built using modules from Python's Standard Library (`re`, `secrets`, `string`) for maximum portability and security, as well as minimal dependency reliance.

## Cryptographic Standards
The generation engine utilizes the 'secrets' module, a cryptographically strong random number generator (CSPRNG). The resulting, pre-assessed 16-character password orivudes sufficient protection against potential future credential cracking attempts.

## Setup and Installation
1. Download the 'pass_project.py' file to your local directory.
2. Ensure Python 3.8 is higher installed.
3. Run the script directly from your terminal:
   # bash
   python pass_project.py
