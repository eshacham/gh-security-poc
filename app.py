import os
import subprocess


def main():
    print("Hello from GitHub Secure CI/CD POC!")


def insecure():
    # BAD: reading a shell command from an environment variable
    #      and passing it straight into subprocess.run with shell=True
    cmd = os.getenv("BAD_CMD", 'echo "This is a bad command"')
    subprocess.run(cmd, shell=True)


if __name__ == "__main__":
    main()
    insecure()


AWS_SECRET_ACCESS_KEY = 'AKIA••••••••••••••'
