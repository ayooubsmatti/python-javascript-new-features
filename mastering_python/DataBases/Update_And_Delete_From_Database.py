# -----------------------------------------------------------
# ----- Databases- SQLite Update And Delete From Database ---
# -----------------------------------------------------------

# Import SQLite Module
import sqlite3

# Create Database and Connect
db = sqlite3.connect("app.db")

# Setting Up The Cursor
cr = db.cursor()


# Update Data
cr.execute("update users set name = 'holy' where user_id = 1")
# Delete Data
cr.execute("delete from users where user_id = 2")
# Fetch data
cr.execute("select * from users")


print(cr.fetchone())  # ('ayoub',)
print(cr.fetchone())
print(cr.fetchone())

# save (Commit) Changes
db.commit()

# Close Database
db.close()
