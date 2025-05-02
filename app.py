import subprocess

def dangerous(user_input):
    # BAD: directly passes untrusted user_input into a shell
    subprocess.run(user_input, shell=True)

if __name__ == "__main__":
    user_input = input("Enter something: ")
    dangerous(user_input)
