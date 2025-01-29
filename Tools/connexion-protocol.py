import os
import sys
import paramiko
from ftplib import FTP
import requests
import subprocess

def connect_ssh(ip):
    username = input("Enter SSH username: ")
    password = input("Enter SSH password: ")
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    try:
        ssh.connect(ip, username=username, password=password)
        print("Connected successfully to", ip)
        ssh_session = ssh.invoke_shell()
        while True:
            command = input("ssh> ")
            if command.lower() == "exit":
                break
            stdin, stdout, stderr = ssh.exec_command(command)
            print(stdout.read().decode())
    finally:
        ssh.close()

def connect_telnet(ip):
    import telnetlib
    username = input("Enter Telnet username: ")
    password = input("Enter Telnet password: ")
    try:
        with telnetlib.Telnet(ip) as session:
            session.read_until(b"login: ")
            session.write(username.encode('ascii') + b"\n")
            session.read_until(b"Password: ")
            session.write(password.encode('ascii') + b"\n")
            print("Connected successfully to", ip)
            while True:
                command = input("telnet> ")
                if command.lower() == "exit":
                    break
                session.write(command.encode('ascii') + b"\n")
                print(session.read_some().decode('ascii'))
    except Exception as e:
        print("Failed to connect:", e)

def connect_rdp(ip):
    subprocess.run(f"mstsc /v:{ip}", check=True)

def connect_ftp(ip):
    username = input("Enter FTP username: ")
    password = input("Enter FTP password: ")
    with FTP(ip) as ftp:
        ftp.login(username, password)
        print("Connected successfully to", ip)
        ftp.dir()
        ftp.quit()

def connect_sftp(ip):
    username = input("Enter SFTP username: ")
    password = input("Enter SFTP password: ")
    transport = paramiko.Transport((ip, 22))
    transport.connect(username=username, password=password)
    sftp = paramiko.SFTPClient.from_transport(transport)
    print("Connected successfully to", ip)
    sftp.close()

def connect_scp(ip):
    username = input("Enter SCP username: ")
    password = input("Enter SCP password: ")
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(ip, username=username, password=password)
    scp = paramiko.SFTPClient.from_transport(ssh.get_transport())
    print("Directory contents:", scp.listdir('.'))
    scp.close()

def connect_http(ip):
    url = f"http://{ip}"
    response = requests.get(url)
    print("HTTP response from", ip, ":", response.text[:200])  

def connect_https(ip):
    url = f"https://{ip}"
    response = requests.get(url)
    print("HTTPS response from", ip, ":", response.text[:200])  

def main():
    ip = input("Enter the IP address of the remote machine: ")
    print("Choose the connection type:")
    print("1. SSH")
    print("2. Telnet")
    print("3. RDP")
    print("4. FTP")
    print("5. SFTP")
    print("6. SCP")
    print("7. HTTP")
    print("8. HTTPS")
    choice = input("Your choice (1-8): ")

    connection_functions = {
        '1': connect_ssh,
        '2': connect_telnet,
        '3': connect_rdp,
        '4': connect_ftp,
        '5': connect_sftp,
        '6': connect_scp,
        '7': connect_http,
        '8': connect_https
    }
    function = connection_functions.get(choice)
    if function:
        function(ip)
    else:
        print("Invalid choice")

if __name__ == "__main__":
    main()
