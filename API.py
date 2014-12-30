def getstring(x):
    y=[]
    for item in range(len(x)):
        y.append(x[len(x)-item-1])

    return ''.join(y)

def det(x):
    return x[::-1]

dico={"needle":"frog","haystack":["dog","pig","chicken","cat","frog","turkey"]}

def FindNeedle():
    for item in dico["haystack"]:
        if item==dico["needle"]:
            return (dico["haystack"]).index(item)


def NotInArray():
    y=[]
    (dico["prefix"])=(dico["prefix"]).lower() #I assume that the prefix with lower or uppercase are equivalent when comparing with the strings  in the array.

    for item in dico["array"]:
        if item[:len(dico["prefix"])]!=dico["prefix"]:
            y.append(item)

    return y


from datetime import datetime
from datetime import timedelta

dico={"datestamp":"2006-11-21 16:30","interval":730}

def DatingGame():

    dt = datetime.strptime((dico["datestamp"]), "%Y-%m-%d %H:%M")
    return str(dt+timedelta(seconds=(dico["interval"])))

