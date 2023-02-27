import uuid
import getpass

def login():
    with open("users.txt", "r") as f:
        lines = f.readlines()
        if not lines:
            print("No users found. Please register first.")
            return
        uids = [line.strip().split(':')[2] for line in lines]
        usernames = [line.strip().split(':')[0] for line in lines]
        uid_to_username = dict(zip(uids, usernames))

    username = input("Enter username: ")
    password = input("Enter password: ")

    for line in lines:
        line = line.strip().split(':')
        if line[0] == username and line[1] == password:
            uid = line[2]
            print(f"Welcome, {username}! Your UID is {uid}.")
            break
    else:
        print("Invalid username or password.")


while True:
    login()
