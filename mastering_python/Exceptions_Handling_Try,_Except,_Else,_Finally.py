# ----------------------------------------------
# -----      Exceptions Handling     -----------
# -----    Try | Except | Else | Finally    ----
# ----------------------------------------------
# Try  => Test the code For Errors
# Except  => Handle THe Errors
# ----------------------------------------------
# Else  => if no Errors
# Finally  => run The code
# ----------------------------------------------

# try:  # Try the code
#     number = int(input("write your age: "))
# except:  # Handle The Errors If Its Found
#     print("Bad, This is Not Integer")
# else:  # If Theres No Errors
#     print("Good, This Is Integer")
# finally: #
#     print("Print from Finally Whatever Happens")

# ----------------------------------------------
try:  # Try the code
    print(x)
except ZeroDivisionError:

    print("Can't Divide")
except NameError:

    print("Identifier Not Found")

except:

    print("Error Hapens")
# ----------------------------------------------
