import sys
import shutil
import os
import requests
from dotenv import load_dotenv
from colorama import Fore
from datetime import datetime


def download_input(year, day):
    try:
        load_dotenv()
        COOKIE = os.getenv("COOKIE")
        URL = f"https://adventofcode.com/20{year}/day/{str(int(day))}/input"
        USER_AGENT = "https://github.com/martinhova01/advent-of-code by mrhova46@gmail.com"
        headers = {"User-Agent": USER_AGENT}
        
        response = requests.get(URL, cookies={"session": COOKIE}, headers=headers)
        response.raise_for_status()

        dest = f"{year}/{day}/input.txt" 
        with open(dest, "w") as f:
            f.write(response.content.decode())
        print(f"{Fore.GREEN}Input downloaded successfully{Fore.WHITE}")
        
    except requests.exceptions.RequestException as e:
        print(f"{Fore.RED}An error occurred while downloading the file: {e}{Fore.WHITE}")
        
        file = f"{year}/{day}/input.txt"
        if not os.path.isfile(file):
            with open(file, "w") as f:
                pass
        print("Empty input file created.")
        
def copy_template_file():
    source = "template.py"
    dest = f"{year}/{day}/main.py"
    if os.path.isfile(dest):
        print("Template file already exists.")
    else:
        shutil.copy(source, dest)
        print("Template file copied into folder.")

if __name__ == "__main__":
    year, day = None, None
    if len(sys.argv) == 1:
        now = datetime.now()
        year = str(now.year)[2:]
        day = now.day
    elif len(sys.argv) == 3:
        year = sys.argv[1]
        day = sys.argv[2]
    else:
        print("Usage: python3 create_template.py <year> <day>")
        print("Use no arguments for today.")
        sys.exit(1)
        
    if len(str(day)) == 1:
        day = "0" + str(day)
        
    os.makedirs(f"{year}/{day}", exist_ok=True)
    
    file = f"{year}/{day}/testinput.txt"
    if not os.path.isfile(file):
        with open(file, "w") as f:
            pass
        
    file = f"{year}/{day}/input.txt"
    if os.path.isfile(file):
        print("Input file already exists.")
    else:
        download_input(year, day)
    
    copy_template_file()
    