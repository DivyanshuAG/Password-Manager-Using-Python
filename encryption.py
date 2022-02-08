from cryptography.fernet import Fernet


def DoesKeyExist():
    try:
        if open("secret.key", "rb").read():
            return True
    except:
        return False


def generateKey():
    if not (DoesKeyExist()):
        key = Fernet.generate_key()
        with open("secret.key", "wb") as file:
            file.write(key)


def loadKey():
    key = open("secret.key", "rb").read()
    return key


def encryptPass(passw):
    key = loadKey()
    fernet = Fernet(key)
    encodedPass = passw.encode()
    encryptedPass = fernet.encrypt(encodedPass)
    return encryptedPass


def decryptPass(encryptedPass):
    key = loadKey()
    fernet = Fernet(key)
    decryptedPass = fernet.decrypt(encryptedPass)
    passw = decryptedPass.decode()
    return passw
