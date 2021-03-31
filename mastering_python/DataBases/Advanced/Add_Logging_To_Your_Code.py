# -----------------------------------------------------------
# ----- Advanced_lessons Add Logging To Your Code --- -------
# -----------------------------------------------------------
# print out to console of file
# print logs of what happens
# ---------------------------------
# --- Debug
# --- INFO
# --- WARNING
# --- ERROR
# --- CRITICAL
# ------------
# name => logging module give it to the default logger.
# -----------------------------------------------------
# basic config
# --- level => level of servicity

import logging
print(dir(logging))

logging.basicConfig(filename="my_app.log",
                    filemode="a",
                    format="(%(asctime)s) => |  (%(name)s) => |  (%(levelname)s)  => | (%(message)s) ",
                    datefmt="%d - %B - %Y, %H:%M:%S")

my_logger = logging.getLogger("ayoub")
my_logger.critical("this is critical message")
