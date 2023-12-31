import sqlite3

# Create a connection to the database
conn = sqlite3.connect('example.db')

# Create a cursor object to execute SQL queries
cursor = conn.cursor()

# Create a table
create_table_query = '''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        age INTEGER
    );
'''
cursor.execute(create_table_query)

# Insert data into the table
insert_data_query = '''
    INSERT INTO users (name, age) VALUES (?, ?);
'''
user_data = [('John Doe', 25), ('Jane Smith', 30)]
cursor.executemany(insert_data_query, user_data)

# Retrieve data from the table
sele

# # Commit the changes and close the connection
# conn.commit()
# conn.close()
