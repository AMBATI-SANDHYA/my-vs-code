import mysql.connector

# Connect to MySQL Server
connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root@123"
)

cursor = connection.cursor()

# Create Database
cursor.execute("CREATE DATABASE IF NOT EXISTS InternshipDB")
print("Database Created Successfully.")

# Select Database
cursor.execute("USE InternshipDB")

# Create Table
cursor.execute("""
CREATE TABLE IF NOT EXISTS Interns(
    ID INT AUTO_INCREMENT PRIMARY KEY,
    Name VARCHAR(100),
    Role VARCHAR(100),
    Email VARCHAR(100)
)
""")

print("Table Created Successfully.")

# Insert Sample Records
cursor.execute("""
INSERT INTO Interns(Name, Role, Email)
VALUES
('Rahul Sharma','Cloud Engineer','rahul@gmail.com'),
('Priya Singh','DevOps Intern','priya@gmail.com'),
('Arjun Kumar','Software Developer','arjun@gmail.com'),
('Sneha Reddy','Cloud Administrator','sneha@gmail.com'),
('Amit Verma','Database Engineer','amit@gmail.com')
""")

connection.commit()

print("Records Inserted Successfully.\n")

# Display Records
cursor.execute("SELECT * FROM Interns")

rows = cursor.fetchall()

print("========== Intern Records ==========\n")

for row in rows:
    print(f"ID      : {row[0]}")
    print(f"Name    : {row[1]}")
    print(f"Role    : {row[2]}")
    print(f"Email   : {row[3]}")
    print("-----------------------------------")

cursor.close()
connection.close()

print("\nDatabase Connection Closed.")