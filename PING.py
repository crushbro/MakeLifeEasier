# Import the subprocess and sys modules
import subprocess
import sys

# txt file that contains your file of IPs
file_name = r''

# Open the file to read the IP addresses
with open(file_name) as f:
    # Loop through each line in the file
    for line in f:
        # Strip the newline character and store the IP address
        ip = line.strip()
        # Run the ping command with the -a switch and capture the output
        output = subprocess.run(["ping", "-a", "-n", "1", ip], capture_output=True, text=True)
        # Check if the ping was successful
        if "Reply from" in output.stdout:
            # Print the IP address and the hostname
            print(f"{ip} {output.stdout.split()[1]}")
        else:
            # Print the IP address and a message
            print(f"{ip} Ping failed")
