import sqlite3

# Connect to SQLite database (this creates the database file if it doesn't exist)
conn = sqlite3.connect('your_database_name.db')  # This will create the .db file if it doesn't exist
cursor = conn.cursor()

# Create the FileHashes table
cursor.execute('''
    CREATE TABLE IF NOT EXISTS FileHashes (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        sha256 TEXT NOT NULL,
        md5 TEXT NOT NULL,
        virus_type TEXT NOT NULL
    );
''')

ddaa = [('36f4b2be18a0ff7f7f9ct6e755ab0aeafc4198a71cf50305693e821aed890879', 'fac023e49f6f70f4d60dc5500b360d44', 'malware'), ('26f4b2be18a0ff7f7f91d6e755ab0aeafc4198a71cf50305693e821aed890879', 'dac051e49f6f70f4d60dc5500b360d44', 'trojan'), ('843037416371600a7f289be8fe2b2224afe1c1bb0736bbab7b3ff393e6a7aaf2', '38fa397eef5f34741c8e4101dcb4a0e3', 'virus')]

# Insert example data
for i in ddaa:
    cursor.execute(f'''
        INSERT INTO FileHashes (sha256, md5, virus_type)
        VALUES
        {i};
    ''')

# Commit changes and close the connection
conn.commit()
conn.close()