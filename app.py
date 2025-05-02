import os

def dangerous(user_input):
    # BAD: directly passes user_input into shell
    os.system(f"echo You said: {user_input}")

if __name__ == "__main__":
    dangerous("$(rm -rf /)")  # CodeQL will flag this
