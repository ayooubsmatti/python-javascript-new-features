# -----------------------------------------------------------
# ----- Databases - SQLite Create Database And Connect  -----
# -----------------------------------------------------------
# ---Connect
# ---Execute
# ---Close
# ------------------------------------------------------------

# # Import SQLite Module
# import sqlite3

# # Create Database and Connect
# db = sqlite3.connect("app.db")

# # Create The tables and Fields
# db.execute(
#     "CREATE TABLE if not exists skills(name TEXT, progress INTEGER,user_id INTEGER)")

# # Close Database
# db.close()

# -----------------------------------------------------------
# ----- Databases - SQLite Create Database And Connect  -----
# -----------------------------------------------------------
# ---cursor => All Operator in SQL Done by Cursor not the connection Itself
# ---commit => save All Changes
# ------------------------------------------------------------

# # Import SQLite Module
# import sqlite3

# # Create Database and Connect
# db = sqlite3.connect("app.db")

# # Setting Up The Cursor
# cr = db.cursor()

# # Create The tables and Fields
# cr.execute("CREATE TABLE if not exists users (user_id INTEGER, name TEXT)")
# cr.execute(
#     "CREATE TABLE if not exists skills(name TEXT, progress INTEGER,user_id INTEGER)")

# # # Inserting Data
# # cr.execute("insert into users(user_id,name) values(1,'ayoub')")
# # cr.execute("insert into users(user_id,name) values(2,'youcef')")
# # cr.execute("insert into users(user_id,name) values(3,'saber')")

# my_list = ["saber", "ayoub", "smatti", "youcef", "ouali", "ilyas"]

# for key, user in enumerate(my_list):
#     cr.execute(f"insert into users(user_id,name) values({key + 1},'{user}')")
# # save (Commit) Changes
# db.commit()

# # Close Database
# db.close()


# -----------------------------------------------------------
# ----- Databases - SQLite Retrieve Data From Database ------
# -----------------------------------------------------------
# ---fetchone => returns a single record or None if no more rows are available.
# ---fetchall => fetches all the rows of a query result it returns all the rows
# --------------as a list of tuples An empty list is returned if there is no record to fech.
# ---fetchmany(size) =>
# ------------------------------------------------------------

# # Import SQLite Module
# import sqlite3

# # Create Database and Connect
# db = sqlite3.connect("app.db")

# # Setting Up The Cursor
# cr = db.cursor()

# # Create The tables and Fields
# cr.execute("CREATE TABLE if not exists users (user_id INTEGER, name TEXT)")
# cr.execute(
#     "CREATE TABLE if not exists skills(name TEXT, progress INTEGER,user_id INTEGER)")

# # # Inserting Data
# # cr.execute("insert into users(user_id,name) values(1,'ayoub')")
# # cr.execute("insert into users(user_id,name) values(2,'youcef')")
# # cr.execute("insert into users(user_id,name) values(3,'saber')")


# # Fetch data
# # cr.execute("select name from users")

# # # cr.execute("select user_id,name from users")
# # cr.execute("select * from users")
# cr.execute("select * from users")

# # print(cr.fetchone())#('ayoub',)
# # print(cr.fetchone())
# # print(cr.fetchone())

# # print(cr.fetchall())  # [('ayoub',), ('youcef',), ('saber',)]
# print(cr.fetchmany(2))  # [('ayoub',), ('youcef',)]

# # save (Commit) Changes
# db.commit()

# # Close Database
# db.close()
