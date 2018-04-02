#from Crypto.Hash import MD5
from cryptography.fernet import Fernet

key = Fernet.generate_key()
f = Fernet(key)
token = f.encrypt(b'taimur')
print(token)

print(f.decrypt(token))