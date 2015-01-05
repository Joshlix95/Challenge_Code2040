# Author: Josuel Musambaghani
# Email: joshlixmus@gmail.com
# ____________________________________________________________________________________________________________________
#############################################---------PART ONE----------##############################################
# This is the foundation of my work, a solid reference from which all challenges will have their resources. 

import urllib2
import json

# First, let us start by the registration ...

def register(email,github): # email="joshlixmus@gmail.com and github="https://github.com/Joshlix95"
    url = 'http://challenge.code2040.org/api/register'
    values = { 'email': email, 'github':github} 
    req = urllib2.Request(url)
    req.add_header('Content-Type', 'Application/json')
    rsp = urllib2.urlopen(req, json.dumps(values))
    output = rsp.read()
    
    return output

# Now it’s time for the challenge.
# The value of token is given in my previous code.

def getchallenge(token,url):
    info = {'token':token}
    request = urllib2.Request(url)
    request.add_header('Content-Type', 'application/json')
    response = urllib2.urlopen(request, json.dumps(info))
    output = response.read()
    
    return output

# Now it comes to precise what stage of the challenge I want to deal with.
# validatechallenge() takes two arguments:
# 1. a JSON string with the answer for the previous challenge, and 
# 2. an url (as described and given in the guide)

def validatechallenge(answer,url):
    request = urllib2.Request(url)
    request.add_header('Content-Type','application\json')
    response = urllib2.urlopen(request,json.dumps(answer))
    content = response.read()
    print ""
    print "*************** API result ****************** "
    return json.loads(content)['result']

# Whenever I need to check my grades, a function Grades is defined here below.

def Grades(token):
    info = {'token':token}
    request = urllib2.Request('http://challenge.code2040.org/api/status')
    request.add_header('Content-Type', 'application/json')
    response = urllib2.urlopen(request, json.dumps(info))
    content = response.read()
    result = json.loads(content)['result']
    print
    print "************** Grades ****************************"
    for challenge in sorted(result.keys()):
        print challenge + '\t\t' + str(result[challenge])

#############################################------------PART TWO-----------###########################################
# this part deals with the four challenges challenges, and the way they are linked with the json for code executions. 

from datetime import datetime
from datetime import timedelta
import json

def reversed_string(data,token):
    
    print "**************************"
    print "Reversed String Challenge"
    print "**************************"

    string = json.loads(data)['result']
    reversed_str = string[::-1]
    print "The initial string: ", string
    print "The reversed String: ", reversed_str
    return {'token':token, 'string':reversed_str}

def prefix(data,token):
    
    print "*******************************"
    print "Prefix"
    print "*******************************"
    
    result = json.loads(data)['result']
    array = result['array']
    prefix = result['prefix']
    new_array = []
    print "Array: ", array
    print "Prefix: ", prefix
    
    for item in array:
        if item.find(str(prefix)) < 0:
            new_array.append(item)

    print "The array without the given prefix"
    print new_array
    return {'token':token,'array':new_array}

def findneedle(data,token):
    
    print "************************"
    print "Needle In The Haystack"
    print "************************"
    
    json_data = json.loads(data)
    needle = json_data['result']['needle']
    haystack = json_data['result']['haystack']
    index = 0
    print "Needle: ", needle
    print "Haystack: ", haystack
    for stuff in haystack:
        if needle == stuff:
            print "Index of needle: ", index
            return {'token':token,'needle':index}
        index += 1

def datingGame(data,token):
    print "************************"
    print "The Dating Game"
    print "************************"
    
    result = json.loads(data)['result']
    datestamp = result['datestamp']
    interval = result['interval']
    time = iso8601.parse_date(datestamp)
    
    dt = datetime.strptime((dico["datestamp"]), "%Y-%m-%d %H:%M")
    return {'token':token, 'datestamp':str(dt+timedelta(seconds=(dico["interval"])))}

#####################################-----------------PART THREE----------------#######################################
# My principal function for navigation! This part will help me  to go through all my built code.
import json

def main():
    my_token = 'rmUQt128vF'
    challenge_urls = [
        'http://challenge.code2040.org/api/getstring',
        'http://challenge.code2040.org/api/prefix',
        'http://challenge.code2040.org/api/time',
        'http://challenge.code2040.org/api/haystack',
        ]
    
    validation_urls= [
        'http://challenge.code2040.org/api/validatestring',
        'http://challenge.code2040.org/api/validateprefix',
        'http://challenge.code2040.org/api/validatetime',
        'http://challenge.code2040.org/api/validateneedle'
        ]
    
    valid_choice = True
    
    while(valid_choice == True):
        print "++++++++++++++++++++++++++++++++++++++++++"
        print "What challenge do you want to solve? *"
        print "1.- Reverse String *"
        print "2.- Prefix *"
        print "3.- The Dating Game *"
        print "4.- Haystack *"
        print " *"
        print "Write 'Grades' to check grade on the API *"
        print "++++++++++++++++++++++++++++++++++++++++++"
        choice = raw_input("Enter your choice: ")

        
    if choice == '1':
        challenge_data = getchallenge(my_token,challenge_urls[0])
        challenge_answer = reversed_string(challenge_data,my_token)
        print validatechallenge(challenge_answer,validation_urls[0])
    elif choice == '2':
        challenge_data = getchallenge(my_token,challenge_urls[1])
        challenge_answer = prefix(challenge_data,my_token)
        print validatechallenge(challenge_answer,validation_urls[1])
    elif choice == '3':
        challenge_data = getchallenge(my_token,challenge_urls[2])
        challenge_answer = datingGame(challenge_data,my_token)
        print validatechallenge(challenge_answer,validation_urls[2])
    elif choice == '4':
        challenge_data = getchallenge(my_token,challenge_urls[3])
        challenge_answer = findneedle(challenge_data,my_token)
        print validatechallenge(challenge_answer,validation_urls[3])
    elif choice.lower() == 'grades':
        Grades(my_token)
    else:
        valid_choice = False
        
main()
