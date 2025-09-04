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
   - It opens the wordlist (`rockyou.txt`) and reads passwords line by line.
   - For each password, it strips any trailing newline characters and encodes the password.

3. A POST request is sent to the target with the username and password.

4. If the response contains the success message (Welcome back), the script reports the valid credentials and exits.

5. If no valid password is found for a username, it notifies and moves on to the next one.

# Tools and Technologies Used
Python – Main programming language.

Web Login Endpoint – The script requires a web application with a functional login form to target.

`sys` – Used for output handling and termination.

`requests` – For sending HTTP POST requests.

Linux (Kali) – Typical environment for running hash-cracking tools.

# Files
`brute_force_login.py`: Main Python script that performs the brute-force attack.

`rockyou.txt`: A wordlist file containing millions of commonly used passwords (You can use any .txt wordlist).

# How to Run
1. Clone or download this repository
2. Install the libraries: pip install requests (sys doesn't need to be installed, it's part of Python's standard library)
3. Place your wordlist file in the same directory as the script, or update the file path in the code.
4. Run the script using one of the following methods:
   - Terminal (macOS/Linux): 'python3 brute_force_login.py'
   - Windows (or IDEs like VS Code, PyCharm): 'python brute_force_login.py' or use the Run button

# Disclaimer
This project is created for research, ethical hacking, and educational purposes only. Unauthorized access to computer systems is illegal. Always ensure you have explicit permission before testing any systems. The developer is not responsible for any misuse of this code.

# Contribution and Feedback
Contributions, feedback, and issues can be submitted via the GitHub repository. Ensure that your interactions adhere to the GitHub Community Guidelines to maintain a respectful and collaborative environment.

# License
This project is licensed under the MIT License. Feel free to use or modify it for personal use or learning.
<br>**Stay safe and have fun! 😊**
