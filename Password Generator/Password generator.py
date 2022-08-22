import secrets 
import string

def generatePass():
    characters = string.ascii_letters + string.digits
    password = ''.join(secrets.choice(characters) for i in range(18))
    print("Password generated: ", password)


if __name__ == "__main__":

    generatePass()