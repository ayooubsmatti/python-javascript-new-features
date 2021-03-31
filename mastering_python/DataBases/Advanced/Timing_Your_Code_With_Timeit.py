# -----------------------------------------------------------
# ----- Advanced_lessons Timing Your Code With Timeit -------
# -----------------------------------------------------------
# ------------------------------------------------------------
# -- timeit: Get Execution Time of code by running 1M Time and give you minimal time
# -----------it used for performance by testing all functionality
#--- timeit(stmt, steup, timer, number)
# --- timeit(pass,pass,default,1.000.000) Default values
# -------------------------------------------------------------
# --- stmt: COde You want to measure the execution Time
# --- steup: steup done before the code execution(import module or anything)
# ---timer: the timer value
# ---number:how many execution that will run
# --------------------------------------------------------------
import timeit
# print(dir(timeit))
# print(timeit.timeit("'ayoub' * 1000"))
# #--------------------------------
# name = "ayoub"
# print(name * 1000)
# print(timeit.timeit("name = 'ayoub'; name * 1000"))
# -----------------------------------------

# print(timeit.timeit(stmt="random.randint(0,50)", setup="import random"))

# --------------------------------------------
# print(timeit.repeat(stmt="random.randint(0,50)", setup="import random", repeat=5))
