#!/usr/bin/env python3
import requests
import sys
import os

    
def get_input(day, token):
    url = "https://adventofcode.com/2025/day/"+str(day)+"/input"
    headers = {'Cookie': 'session=' + token}
    r = requests.get(url, headers=headers)
 
    if r.status_code == 200:
        return r.text 
    else:
        sys.exit(f"/api/alerts response: {r.status_code}: {r.reason} \n{r.content}")
        
if __name__ == "__main__":
    day = sys.argv[1]
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
    
    # place the gathered input into the new folder.
    os.chdir(folder_name)
    with open("input", "w") as f:
        f.write(input_contents)
    with open("part1.py","w"): pass
    with open("part2.py","w"): pass