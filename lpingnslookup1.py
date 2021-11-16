import subprocess, socket # Fetch all address details.

title = "Hostname, Status, DNS"
print(title)

hostsfile=open("hosts", "r")
lines=hostsfile.readlines()

for line in lines:
    response=subprocess.Popen(["ping", "-c1", line.strip()], stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    stdout, stderr = response.communicate()
    #print(stdout)
    #print(stderr)
    
    if (response.returncode == 0):
        status = line.rstrip() + ", Online,"
    else:
        status = line.rstrip() + ", Offline,"
    #print(status)
    try:
       print status, socket.gethostbyname_ex(line.strip()), socket.getaddrinfo(line.strip()), socket.getaddrinfo(line.strip(), None, socket.AF_INET6)
    except:
       print("--")
    
    