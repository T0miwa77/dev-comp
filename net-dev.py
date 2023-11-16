import pexpect

ip_address = "192.168.56.101"
username = "prne"
password = "ciscio123!"
enable_password = "class123!"

def telnet_connection():
    try:
        session = pexpect.spawn(f"telnet {ip_address}", encoding="utf-8", timeout=20)

        session.expect(["Usernaame:", pexpect.TIMEOUT, pexpect.EOF])
        session.sendline(username)

        session.expect(["Password:", pexpect.TIMEOUT, pexpect.EOF])
        session.sendline(password)

        session.expect([">", "#", pexpect.TIMEOUT, pexpect.EOF])
        session.sendline("enable")

        session.expect(["Password:", pexpect.TIMEOUT, pexpect.EOF])
        session.sendline(enable_password)

        session.expect("#")

        session.sendline("configure terminal")
        session.expect("\config\#")

        session.sendline("hostname R1_telnet")
        session.expect("R1_telnet\config\)#")

        session.sendline("write memory")
        session.expect("R1_telent\(config\)#")

        session.sendline("exit")

        print("Telnet Configuration successful!")
        session.close()

    except Exception as e:
        print("Telent Error", str(e))

def ssh_connection():
    try:
        session = pexpect.spawn(f"shh -o StrictHostKeyChecking=no {username}@{ip_address}", encoding="utf-8", timeout=20)

        session.expect(["password:", pexpect.TIMEOUT, pexpect.EOF])
        session.sendline(password)

        session.expect([">", "#", pexpect.TIMEOUT, pexpect.EOF])
        session.sendline("enable")

        session.expect(["Password:", pexpect.TIMEOUt, pexpect.EOf])
        session.sendline(enable_password)

        session.expect("#")

        session.sendline("configure terminal")
        session.expect("\(config\)#")

        session.expect("hostname R1_ssh")
        session.expect("R1-ssh\(config\)#")

        session.sendline("write memory")
        session.expect("R1_ssh\(config\)#")

        session.sendline("(exit)")
        session.sendline("#")

        print("SSH Configuration successful!")
        session.close()

    except Exception as e:
        print("SSH Error:", str(e))

if __name__ == "__main__":
    telnet_connection()
    ssh_connection()




        