import sqlite3

conn = sqlite3.connect("contacts.sqlite")

name = input("Please enter a name to search for: ")

select_sql = "SELECT * FROM contacts WHERE name = ? "
result = conn.execute(select_sql, (name,))
print(result.fetchone())

# for row in conn.execute("SELECT * FROM contacts"):
#     print(row)

conn.close()


