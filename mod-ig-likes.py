import sys
import os
import time
import requests
import random
from getuseragent import UserAgent

os.system("clear || cls")
os.system("xdg-open https://github.com/Sammy750-cyber")
class color:
    RED='\033[91m'
    YELLOW='\033[93m'
    UNDERLINE='\033[4m'
    GREEN='\033[92m'
    BLUE='\033[94m'
    PURPLE='\033[95m'
    BOLD='\033[1m'
    DARKCYAN='\033[36m'
    BLACK='\033[84m'
    END='\033[0m'



logo= (f"""{color.GREEN}
███████╗ ██████╗██╗    ██╗██╗  ██╗ █████╗  ██████╗██╗  ██╗
██╔════╝██╔════╝██║    ██║██║  ██║██╔══██╗██╔════╝██║ ██╔╝
███████╗██║     ██║ █╗ ██║███████║███████║██║     █████╔╝ 
╚════██║██║     ██║███╗██║██╔══██║██╔══██║██║     ██╔═██╗ 
███████║╚██████╗╚███╔███╔╝██║  ██║██║  ██║╚██████╗██║  ██╗
╚══════╝ ╚═════╝ ╚══╝╚══╝ ╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝ {color.END}
{color.BOLD}{color.BLUE}==============================================={color.END}
{color.BLUE}[{color.END}{color.BOLD}{color.PURPLE}={color.END}{color.BLUE}]{color.END}  {color.YELLOW}DEVELOPER{color.END}     {color.BOLD}:{color.END}  {color.GREEN} SCWhack {color.END}
{color.BLUE}[{color.END}{color.BOLD}{color.PURPLE}={color.END}{color.BLUE}]{color.END}  {color.YELLOW}GITHUB{color.END}        {color.BOLD}:{color.END}  {color.GREEN} Sammy750-cyber {color.END}
{color.BLUE}[{color.END}{color.BOLD}{color.PURPLE}={color.END}{color.BLUE}]{color.END}  {color.YELLOW}VERSION{color.END}       {color.BOLD}:{color.END}  {color.GREEN} 1.0 {color.END}
{color.BLUE}[{color.END}{color.BOLD}{color.PURPLE}={color.END}{color.BLUE}]{color.END}  {color.YELLOW}TELEGRAM{color.END}      {color.BOLD}:{color.END}  {color.GREEN} NOGROUPYET {color.END}
{color.BLUE}[{color.END}{color.BOLD}{color.PURPLE}={color.END}{color.BLUE}]{color.END}  {color.YELLOW}TOOL'S NAME{color.END}   {color.BOLD}:{color.END}  {color.GREEN} INSTAGRAM_LIKES {color.END}
{color.BLUE}[{color.END}{color.BOLD}{color.PURPLE}={color.END}{color.BLUE}]{color.END}  {color.YELLOW}STATUS{color.END}        {color.BOLD}:{color.END}  {color.GREEN} FREE {color.END}
{color.BOLD}{color.BLUE}==============================================={color.END}
{color.BLUE}[{color.END}{color.PURPLE}01/A{color.END}{color.BLUE}]{color.END} {color.GREEN} Start {color.END}
{color.BLUE}[{color.END}{color.PURPLE}02/B{color.END}{color.BLUE}]{color.END} {color.GREEN} Contact Developer {color.END}
{color.BLUE}[{color.END}{color.PURPLE}03/C{color.END}{color.BLUE}]{color.END} {color.GREEN} More Tools {color.END}
{color.BLUE}[{color.END}{color.PURPLE}{color.RED}04/X{color.END}{color.BLUE}]{color.END} {color.GREEN} {color.RED}Exit Programme {color.END}
{color.BOLD}{color.BLUE}==============================================={color.END}
""")

for i in logo:
    sys.stdout.write(i)
    sys.stdout.flush()
    time.sleep(0.0001) 
user_input=input(f"{color.BLUE}{color.BOLD}[{color.GREEN}>{color.BLUE}]{color.END} {color.GREEN}CHOOSE: ")
user_input=user_input.replace(' ','')

if user_input == "1" or user_input == "01" or user_input == "a" or user_input == "A":
    ua = UserAgent("ios").Random()
    print(f"{color.BOLD}{color.BLUE}==============================================={color.END}")
    user=input(f"{color.BLUE}{color.BOLD}[{color.GREEN}+{color.BLUE}]{color.END} {color.GREEN}IG-USERNAME: ")
    link=input(f"{color.BLUE}{color.BOLD}[{color.GREEN}>{color.BLUE}]{color.END} {color.GREEN}POST-URL: ")
    res=requests.post('https://api.likesjet.com/freeboost/7',json={"instagram_username":user,"link":link,"email":f"whisper{random.randint(100000,999999)}@gmail.com"},headers={"Host": "api.likesjet.com","content-length": "137","sec-ch-ua": "\"Google Chrome\";v\u003d\"119\", \"Chromium\";v\u003d\"119\", \"Not?A_Brand\";v\u003d\"24\"","accept": "application/json, text/plain, */*","content-type": "application/json","sec-ch-ua-mobile": "?1","user-agent":ua,"sec-ch-ua-platform": "\"Android\"","origin": "https://likesjet.com","sec-fetch-site": "same-site","sec-fetch-mode": "cors","sec-fetch-dest": "empty","referer": "https://likesjet.com/","accept-language": "en-XA,en;q\u003d0.9,ar-XB;q\u003d0.8,ar;q\u003d0.7,en-GB;q\u003d0.6,en-US;q\u003d0.5"}).json()
    print(f"{color.BOLD}{color.BLUE}==============================================={color.END}")
    print(res['message'])
elif user_input == "2" or user_input == "02" or user_input == "b" or user_input == "B":
    os.system("xdg-open https://t.me/+X4IQQe35aZI0Yzg8")
elif user_input == "3" or user_input == "03" or user_input == "c" or user_input == "C":
    os.system("xdg-open https://github.com/Sammy750-cyber")
elif user_input == "4" or user_input == "04" or user_input == "d" or user_input == "D":
    sys.exit()
