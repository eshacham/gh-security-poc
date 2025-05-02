import os

def dangerous(user_input):
    # BAD: directly passes user_input into shell
    os.system(f"echo You said: {user_input}")

if __name__ == "__main__":
    # now we read from stdin so CodeQL treats this as tainted
    user_input = input("Enter something: ")
    dangerous(user_input)  # CodeQL will flag this
