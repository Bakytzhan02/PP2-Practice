import csv
from connect import get_connection

def create_table():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS phonebook (
            id SERIAL PRIMARY KEY,
            name VARCHAR(100) NOT NULL,
            phone VARCHAR(20) UNIQUE NOT NULL
        )
    """)
    conn.commit()
    cur.close()
    conn.close()

def insert_from_console():
    name = input("Enter name: ")
    phone = input("Enter phone: ")
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("INSERT INTO phonebook (name, phone) VALUES (%s, %s)", (name, phone))
    conn.commit()
    cur.close()
    conn.close()

def insert_from_csv():
    conn = get_connection()
    cur = conn.cursor()
    with open("contacts.csv", "r", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        for row in reader:
            cur.execute(
                "INSERT INTO phonebook (name, phone) VALUES (%s, %s) ON CONFLICT (phone) DO NOTHING",
                (row["name"], row["phone"])
            )
    conn.commit()
    cur.close()
    conn.close()

def show_all():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM phonebook")
    for contact in cur.fetchall():
        print(contact)
    cur.close()
    conn.close()

def search_by_name():
    name = input("Enter name: ")
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM phonebook WHERE name ILIKE %s", (f"%{name}%",))
    for contact in cur.fetchall():
        print(contact)
    cur.close()
    conn.close()

def search_by_phone_prefix():
    prefix = input("Enter phone prefix: ")
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM phonebook WHERE phone LIKE %s", (f"{prefix}%",))
    for contact in cur.fetchall():
        print(contact)
    cur.close()
    conn.close()

def update_contact():
    old_phone = input("Current phone: ")
    new_name = input("New name: ")
    new_phone = input("New phone: ")
    conn = get_connection()
    cur = conn.cursor()
    cur.execute(
        "UPDATE phonebook SET name=%s, phone=%s WHERE phone=%s",
        (new_name, new_phone, old_phone)
    )
    conn.commit()
    cur.close()
    conn.close()

def delete_contact():
    value = input("Enter name or phone: ")
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("DELETE FROM phonebook WHERE name=%s OR phone=%s", (value, value))
    conn.commit()
    cur.close()
    conn.close()

def menu():
    create_table()
    while True:
        print("""
1.Add contact
2.Import CSV
3.Show all
4.Search by name
5.Search by phone prefix
6.Update
7.Delete
0.Exit
""")
        choice = input("Choose: ")
        if choice == "1":
            insert_from_console()
        elif choice == "2":
            insert_from_csv()
        elif choice == "3":
            show_all()
        elif choice == "4":
            search_by_name()
        elif choice == "5":
            search_by_phone_prefix()
        elif choice == "6":
            update_contact()
        elif choice == "7":
            delete_contact()
        elif choice == "0":
            break
        else:
            print("Wrong option")

menu()
