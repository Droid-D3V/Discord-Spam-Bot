import requests
import time
import sys
import random
import string
import os
from pyfiglet import Figlet
from dotenv import load_dotenv
f = Figlet(font='slant')


load_dotenv()
discord_token =  os.getenv('discord_token')


def confirm():
    e = input("Press [ENTER] to continue")

def clear_screen():
    print("\x1b[2J\x1b[H",end="")




def spam():
    print("Spammed")
    confirm()


def config():
    print("Configs")
    confirm()


def mainmenu():
    while True:
        clear_screen()
        print(f.renderText("DiscordSpam")+"v1.0")
        print("#","="*10,"Main Menu", "="*10, "#")
        print("My dearest retard, what do you want to do?")
        print("1. Spam someone or some channel")
        print("2. Configure the spammer")
        print("3. Quit")
        print("(Enter the number of the action you want to perform)")

        user_r = input(">> ")
        if user_r == "1":
            clear_screen()
            spam()
            

        elif user_r == "2":
            clear_screen()
            config()
            

        elif user_r == "3":
            clear_screen()
            print("Suspended")
            sys.exit()
            break

        else:
            print("You must enter a number from the listed options")





def rand_msg():
    return ''.join(random.choice(string.printable) for i in range(16))

#https://discord.com/api/v8/channels/814958806341255188/messages


headers = {"authorization": discord_token}

channel = "313271128376475649"
runs = 0
effective_msgs = 0
wasted_msgs = 0
delay = 0.37


mainmenu()

while True:
    try:
        payload = {"content": rand_msg()}
        r = requests.post(f"https://discord.com/api/v8/channels/{channel}/messages", data = payload, headers = headers)
        #print(r.status_code, type(r.status_code))
        if r.status_code == 200:
            effective_msgs += 1
        else:
            wasted_msgs += 1

        if runs == 0:
            print("Timer started")
            start_time = time.time()

        runs += 1
        time.sleep(delay)
    except KeyboardInterrupt:
        run_time = time.time() - start_time
        print("#==========")
        print("#STATISTICS")
        print(f"#Total messages sent: {wasted_msgs + effective_msgs}")
        print(f"#Server recieved {effective_msgs} messages")
        print(f"#Server ignored {wasted_msgs} messages")
        print(f"#Average msg/second: {round(effective_msgs/run_time, 2)}")
        print(f"#Recived messages to wasted messages ratio: 1:{round(wasted_msgs/effective_msgs,2)}")
        print(f"#Stopped after running for {round(run_time,2)} seconds")
        sys.exit()
