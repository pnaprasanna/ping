import subprocess, os

title = "Hostname, Status"
print(title)

hostsfile=open("hosts", "r")
lines=hostsfile.readlines()

for line in lines:
    response=subprocess.Popen(["ping", "-c1", line.strip()], stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    stdout, stderr = response.communicate()
    #print(stdout)
    #print(stderr)
    #print(response.returncode)

    if (response.returncode == 0):
        status = line.rstrip() + ", Online"
    else:
        status = line.rstrip() + ", Offline"
    print(status)
