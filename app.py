import sqlite3

def vulnerable_sql(user_input):
    # BAD: Directly concatenates user input into an SQL query
    conn = sqlite3.connect(":memory:")
    conn.execute(f"SELECT * FROM users WHERE name = '{user_input}'")
    conn.close()

if __name__ == "__main__":
    user_input = input("Enter your name: ")
    vulnerable_sql(user_input)