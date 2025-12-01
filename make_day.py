# -*- coding: utf-8 -*-
"""
Created on Sun Nov 30 21:58:39 2025

@author: kthem
"""

#!/usr/bin/env python3
import requests
import sys
import os

    
def get_input(day):
    url = "https://adventofcode.com/2025/day/"+str(day)+"/input"
    headers = {'Cookie': 'session='+sessionToken }
    r = requests.get(url, headers=headers)
 
    if r.status_code == 200:
        return r.text 
    else:
        sys.exit(f"/api/alerts response: {r.status_code}: {r.reason} \n{r.content}")
        
if __name__ == "main":
    day = sys.argv[1]
    sessionToken = ""
    
    with open("token_info") as f:
        sessionToken = f.read().strip()

    if sessionToken == "":
        sys.exit("Session token is empty.")
    
    # fetch the day's input contents
    input_contents = get_input(day)
    
    # if the day's folder is not already created, do so
    folder_name = "day"+str(day)
    if not os.path.isdir(folder_name):
        os.mkdir(folder_name)
    
    os.chdir(folder_name)
    
    with open("input", "w") as f:
        f.write(input_contents)