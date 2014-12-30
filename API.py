
# STAGE 1: Reverse a string
# I suggested two ways to solve this problem:
# First way:

def getString(x):
    y=[]
    for item in range(len(x)):
        y.append(x[len(x)-item-1])

    return ''.join(y)

# Second way:

def GetString(x):
    return x[::-1]

# STAGE II: Needle in a haystack
# The task is to to tell the API where the needle is in the array.

def FindNeedle():
    for item in dico["haystack"]: # I assumed that the dictionary variable given by the API is dico
        if item==dico["needle"]:
            return (dico["haystack"]).index(item)

# STAGE III: Prefix 
# The task is to to return an array containing only the strings that do not start with the prefix given in the dictionary. 

def NotInArray():
    y=[]
    (dico["prefix"])=(dico["prefix"]).lower()   # I considered that the prefix with lower or uppercase are equivalent.
                                                # I assumed that the dictionary variable given by the API is dico

    for item in dico["array"]:
        if item[:len(dico["prefix"])]!=dico["prefix"]:
            y.append(item)

    return y

# STAGE IV: The dating game
# The job is to add the interval to the date formatted as an ISO 8601 datestamp

from datetime import datetime
from datetime import timedelta

def DatingGame():
    dt = datetime.strptime((dico["datestamp"]), "%Y-%m-%d %H:%M")
    return str(dt+timedelta(seconds=(dico["interval"])))

