import sqlite3
import hashlib
import os
from getpass import getuser


def initialize_db(db_path='your_database_name.db'):
    global conn, cursor
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

# foldern = "C:\\Users\\Microsoft\\Documents\\prrrog\\cybersecurityprotection"

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

# Close the database connection
def close_db():
    conn.close()

def Checking_virus(filena):
    initialize_db()

    cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='FileHashes'")
    table = cursor.fetchone()

    if table:
        # print("Table 'FileHashes' exists.")
        cursor.execute("SELECT sha256, md5, virus_type FROM FileHashes")
        rows = cursor.fetchall()
        
        for row in rows:
            try:
                if row[0] == sha256_hash(filena) and row[1] == md5_hash(filena):
                    print(f"Virus Detected! {row[0]}||{row[1]}||Type:-{row[2]} --> Filename:{filena}")
                    close_db()
                    return True, row[2]

                else:
                    print(filena)
                    continue

            except:
                continue

    else:
        print("Table 'FileHashes' does not exist. Please check your database.")

    close_db()
        
    return False, "Clean"


# print(deep_scan(foldern))

