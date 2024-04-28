import sqlite3
import tkinter as tk
from tkinter import ttk

def create_table(cursor):
    cursor.execute('''CREATE TABLE IF NOT EXISTS Employees (
                    id INTEGER PRIMARY KEY,
                    name TEXT,
                    age INTEGER,
                    department TEXT
                    )''')

def insert_data(cursor):
    cursor.execute("INSERT INTO Employees (name, age, department) VALUES (?, ?, ?)", ('Khurshid', 30, 'HR'))
    cursor.execute("INSERT INTO Employees (name, age, department) VALUES (?, ?, ?)", ('Sahil', 35, 'Finance'))
    cursor.execute("INSERT INTO Employees (name, age, department) VALUES (?, ?, ?)", ('Ryan', 28, 'IT'))

def fetch_data(cursor):
    cursor.execute("SELECT * FROM Employees")
    return cursor.fetchall()

def display_data():
    conn = sqlite3.connect('sample.db')
    cursor = conn.cursor()

    # Clear previous data from the listbox
    listbox.delete(0, tk.END)

    # Fetch data from the Employees table
    rows = fetch_data(cursor)

    # Insert fetched data into the listbox
    for row in rows:
        listbox.insert(tk.END, row)

    cursor.close()
    conn.close()

def close_app():
    root.destroy()

# Connect to SQLite database (create it if not exists)
conn = sqlite3.connect('sample.db')
cursor = conn.cursor()

# Create a table if not exists
create_table(cursor)

# Insert some data into the table
insert_data(cursor)

# Commit the changes
conn.commit()

cursor.close()
conn.close()

root = tk.Tk()
root.title("Database Viewer")

# Create listbox to display data
listbox = tk.Listbox(root, width=40, height=10)
listbox.pack(padx=10, pady=10)

# Button to fetch and display data
fetch_button = ttk.Button(root, text="Fetch Data", command=display_data)
fetch_button.pack(pady=5)

# Button to exit
exit_button = ttk.Button(root, text="Exit", command=close_app)
exit_button.pack(pady=5)

root.mainloop()
