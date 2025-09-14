import hashlib


def sha256_hash(filename):
    with open(filename, "rb") as f:
        bytess = f.read()
        sha256hash = hashlib.sha256(bytess).hexdigest()

    return sha256hash

def md5_hash(filename):
    with open(filename, "rb") as f:
        bytess = f.read()
        md5hash = hashlib.md5(bytess).hexdigest()

    return md5hash

filepath = "C:\\Users\\jaisw\\Downloads\\Git-2.51.0-64-bit.exe"
print(sha256_hash(filepath))
print(md5_hash(filepath))