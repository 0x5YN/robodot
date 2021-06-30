import requests
import sys
import getopt
from termcolor import colored


url = ""
output = ""
start = False
op = False

def Help():
    print("Options:\n\t-u     : Target Url\n\t-o     : Output Results in File <path>\n\t-h     : Show Helps")
    
    
def ascii_art():
    print(""" ___   ___   ___   ___   ___   ___   ___  
|   | |   |   | | |   |   | | |   |   |   
|-+-  |   |   +-  |   |   + | |   |   +   
|  \  |   |   | | |   |   | | |   |   |   
       ---   ---   ---   ---   ---        """)
    print(colored("Coded by: 0x5YN\n" , "blue" , attrs=["bold"]))
    
def chk_url(url):
    urllen = len(url) - 1
    if(url[urllen] == "/"):
        pass
    else:
        url = url + "/"
        
    if(url.find("http") == -1):
        url = "https://" + url
    
    return url

def add_robot(url):
    url = url + "robots.txt"
    return url

def chk_robot(url):
    res = requests.get(url)
    if(res.status_code == 200):
        if(res.text.find("User-agent: *")):
            print(colored("[✔] Robots.txt File Found!\n" , "cyan"))
            rfile = open("rbs.txt" , "w")
            rfile.write(res.text)
            print("[*] Robots.txt File:")
            print(res.text)
            print("________________________________________________\n")
        else:
            print(colored("[✘] Can't Find Robots.txt File    " , "red" , attrs=["bold"]))
    else:
        print(colored("[✘] Can't Find Robots.txt File    CODE:"+str(res.status_code) , "red"))
        start == False

def chk_pathes(url , op ,output):
    rf = open("rbs.txt")
    lines = rf.readlines()
    for line in lines:
        if(line.find("Disallow") == 0):
            path = line.strip("Disallow: ")
            path = path.strip("\n")
            url = ourl.strip("/") + path
            res = requests.get(url)
            if(res.status_code == 200):
                st = "[+] " + url + "     CODE:200"
                print(colored(st , "cyan"))
                if(op == True):
                    ofile = open(output , "a")
                    ofile.write(st + "\n")
            else:
                st = "--> " + url + "     CODE:" + str(res.status_code)
                print(st)
                if(op == True):
                    ofile = open(output , "a")
                    ofile.write(st + "\n")
     

args = sys.argv[1:]

try:
    opts , args = getopt.getopt(args , "u:o:h")
except:
    Help()
    
for opt , arg in opts:
    if opt in ["-u"]:
         url = arg
         start = True
    elif opt in ["-o"]:
        output = arg
        start = True
        op = True
    elif opt in ["-h"]:
        start = False
        Help()
        
if(start == True):
    ascii_art()
    ourl = chk_url(url)
    url = ourl
    url = add_robot(url)               
    chk_robot(url)
    chk_pathes(ourl , op , output)
        
               
elif(start == False):
    Help()
    
