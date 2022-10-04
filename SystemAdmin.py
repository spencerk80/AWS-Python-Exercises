import os
import subprocess

# command="uname"
# commandArgument="-a"

command="ps"
commandArgument="-x"

os.system("ls")
subprocess.run(["ls", "-l", "README.md"])

print(f'Gathering system information with command: {command} {commandArgument}')
subprocess.run([command,commandArgument])
