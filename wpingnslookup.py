import subprocess, socket

title = "Hostname, Status, DNS"
print(title)

hostsfile=open("hosts", "r")
lines=hostsfile.readlines()

for line in lines:
    response=subprocess.Popen(["ping", line.strip()], stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    stdout, stderr = response.communicate()
    #print(stdout)
    #print(stderr)
    
    if (response.returncode == 0):
        status = line.rstrip() + ", Online,"
    else:
        status = line.rstrip() + ", Offline,"
    #print(status)
    try:
       print(status, socket.gethostbyname(line.strip()))
    except:
       print(status, "--")
    
    