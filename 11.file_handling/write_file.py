def post(s):
    return s

def like(s):
    return s

def login(username, password):
    return "Login success with username {}".format(username)

def logout(username):
    return "Logout success with username {}".format(username)

print('hello')
if __name__ == "__main__":
    print(login("darshan", "123"))
