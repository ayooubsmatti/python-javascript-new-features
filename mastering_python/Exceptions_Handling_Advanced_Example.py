# ----------------------------------------------
# -----      Exceptions Handling     -----------
# -----    Try | Except | Else | Finally    ----
# -----         Advance Example             ----
# ----------------------------------------------

the_file = None
the_tries = 5

while the_tries > 0:
    try:
        print("Enter the fle name with absolut path to open")
        print(f"You have {the_tries} Tries Left")
        print("Example: home/user/file.extention")

        file_name_and_path = input("File Name => : ").strip()
        the_file = open(file_name_and_path, 'r')
        print(the_file.read())
        break
    # print(f"{the_tries} Tries Left")
    # the_tries -= 1
    except FileNotFoundError:
        print("File not found Be sure The name is valid")
        the_tries -= 1
    except:
        print("Error Happen")
    finally:
        if the_file is not None:
            the_file.close()
            print("File Closed.")

else:
    print("all tries is Done")
