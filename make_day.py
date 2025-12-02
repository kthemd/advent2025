#!/usr/bin/env python3
import requests
import sys
import os
import datetime

    
def get_input(day, token):
    url = "https://adventofcode.com/2025/day/"+str(day)+"/input"
    headers = {'Cookie': 'session=' + token}
    r = requests.get(url, headers=headers)
 
    if r.status_code == 200:
        return r.text 
    else:
        sys.exit(f"/api/alerts response: {r.status_code}: {r.reason} \n{r.content}")
        
if __name__ == "__main__":
    day = datetime.datetime.now().day
    sessionToken = ""
    
    with open("token_info") as f:
        sessionToken = f.read().strip()

    if sessionToken == "":
        sys.exit("Session token is empty.")
    
    # fetch the day's input contents
    input_contents = get_input(day, sessionToken)
    
    # if the day's folder is not already created, do so
    folder_name = "day"+str(day)
    if not os.path.isdir(folder_name):
        os.mkdir(folder_name)
    else:
        print("Directory for day ", day, " exists")
    
    f1 = os.path.join(os.getcwd(), folder_name, "part1.py")
    f2 = os.path.join(os.getcwd(), folder_name, "part2.py")

    if not os.path.isfile(f1):
        with open(f1, "w"): pass
    if not os.path.isfile(f2):
        with open(f2, "w"): pass
    
    with open(os.path.join(os.getcwd(), "day"+str(day), "input"), "w") as f:
        f.write(input_contents)