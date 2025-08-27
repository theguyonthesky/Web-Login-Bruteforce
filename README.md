# Web-Login-Bruteforce 🔓

# Overview
This is a Python-based brute-force attack tool designed to test multiple username and password combinations against a local web login endpoint. It automates login attempts using a specified wordlist and identifies valid credentials based on a success message in the server’s response. This tool is intended for educational purposes and penetration testing in controlled environments only.

# Note
- Security and Ethical Notice: This script is intended for educational and ethical hacking purposes only. It must only be used in environments you own or have explicit permission to test. Do not use the provided code and techniques for illegal activities.

# Features
- Multiple Username Support: Tests a list of usernames against the password list (you can use any number of usernames or load them from a wordlist).
- Wordlist Integration: Reads passwords from `rockyou.txt` (or any other specified file).
- Real-time Attempt Logging: Displays login attempts live in the terminal without cluttering the output.
- Success Detection: Identifies and reports valid credentials when the server responds with a specific success message.
- Fail Handling: Notifies the user when no valid password is found for a given username.

# How It Works
1. The script targets a local web server (default: http://127.0.0.1:5000).

2. A list of usernames is iterated over, and for each username:

3. It opens the wordlist (rockyou.txt) and reads passwords line by line.
   - For each password, it strips any trailing newline characters and encodes the password.

4. A POST request is sent to the target with the username and password.

5. If the response contains the success message (Welcome back), the script reports the valid credentials and exits.

6. If no valid password is found for a username, it notifies and moves on to the next one.

# Tools and Technologies Used
Python – Main programming language.

`sys` – Used for output handling and termination.

`requests` – For sending HTTP POST requests.

Linux (Kali) – Typical environment for running hash-cracking tools.

# Files
`brute_force_login.py`: Main Python script that performs the brute-force attack.

`rockyou.txt`: A wordlist file containing millions of commonly used passwords (You can use any .txt wordlist).
