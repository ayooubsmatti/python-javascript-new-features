# -----------------------------------------------------------
# ----- Databases- SQLite Update And Delete From Database ---
# -----------------------------------------------------------

# import sqlite3
import sqlite3

# Create Database And Connect
db = sqlite3.connect("app.db")

# Setting Up The Cursor
cr = db.cursor()

# Create The tables and Fields
cr.execute(
    "CREATE TABLE if not exists skills(name TEXT, progress INTEGER,user_id INTEGER)")


def commit_and_close():
    """ commit changes and close connection to database """
    # Save (Commit) Changes
    db.commit()

    # Close Database
    db.close()
    print("Connection To DAtabase Is Closed")


# My user ID
uid = 1

# Input Big Message
input_message = """
what do you want to do ?
"s" => show all skills
"a" => Add new skill
"d" => Delete a skill
"u" => Update a skill
"q" => Quit The App skill
Choose Option:
"""
# Input option choose
user_input = input(input_message).strip().lower()

# Command list
command_list = ["s", "a", "d", "u", "q"]

# Define the Methods


def show_skills():
    cr.execute(f"select * from skills where user_id = '{uid}' ")
    results = cr.fetchall()
    print(f"You have {len(results)} skills.")
    if len(results) > 0:
        print("showing skills with progress: ")

    for row in results:
        print(f"Skill => {row[0]}", end=" ")
        print(f"Progress => {row[1]}%")

    commit_and_close()


def add_skills():
    sk = input("write skill Name: ").strip().capitalize()
    cr.execute(
        f"select name from skills where name = '{sk}' and user_id = '{uid}'")
    results = cr.fetchone()

    if results == None:  # Theres No Skill with this Name In Database
        prog = input("write skill progress: ").strip()

        cr.execute(
            f"insert into skills(name, progress, user_id) values('{sk}', '{prog}', '{uid}')")

    else:  # theres a skill with this name in database
        update_progress = input(
            "You Cannot Add It Because is existed are you want to Update his progress('Y o N'): ").strip().capitalize()
        if update_progress == "Y":

            prog = input("write The new skill progress: ").strip()

            cr.execute(
                f"update skills set progress = '{prog}' where name = '{sk}' and user_id= '{uid}' ")
        else:
            pass

    commit_and_close()


def delete_skills():
    sk = input("write skill Name: ").strip().capitalize()

    cr.execute(
        f"delete from skills where name = '{sk}' and user_id ='{uid}' ")

    commit_and_close()


def update_skills():
    sk = input("write skill Name: ").strip().capitalize()
    prog = input("write The new skill progress: ").strip()

    cr.execute(
        f"update skills set progress = '{prog}' where name = '{sk}' and user_id= '{uid}' ")

    commit_and_close()


# Cheack if command is exist
if user_input in command_list:

    print(f"Command Found {user_input}")
    if user_input == "s":
        show_skills()
    elif user_input == "a":
        add_skills()
    elif user_input == "d":
        delete_skills()
    elif user_input == "u":
        update_skills()
    else:
        print("App is Closed.")
        commit_and_close()
else:
    print(f"Sorry this \"{user_input}\" command Is not Found")
