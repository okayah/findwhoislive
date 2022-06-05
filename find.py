##[ IMPORTS ]##
import requests
import json
from os.path import dirname, join
import webbrowser
from colorama import Fore, init
init()

##[ LOAD FILES ]##
current_dir = dirname(__file__)
config = json.load(open(join(dirname(__file__), "./config.json")))

if config["Load_Streamers_From"] == "github":
    print(Fore.BLUE + 'Loading streamers from Github...\n')
    streamers = requests.get("https://raw.githubusercontent.com/okayah/findwhoislive/main/streamers.json").json()
elif config["Load_Streamers_From"] == "file":
    print(Fore.BLUE + 'Loading streamers from File...\n')
    streamers = json.load(open(join(dirname(__file__), "./streamers.json")))

##[ FUNCTIONS ]##
def isLive(link, category):
    r = requests.get(link)
    if "isLiveBroadcast" in r.content.decode('utf-8'):
        print(Fore.GREEN + '[#]', link, 'is live, their name is ' + streamers[category][link] + '.')
        if config['Open_In_Browser']:
            webbrowser.open(link)
    else:
        print(Fore.RED + '[X]', link, 'is not live.')
        pass

##[ Main Code ]##
print(Fore.LIGHTWHITE_EX+'You can find their SCID @ https://rid.itsdevil.com/')
total = 0
for type in config['Find']:
    if len(streamers[type]) != 0:
        for stream in streamers[type]:
            total += 1
print('Scanning',total,'streamers.')

for type in config['Find']:
    print(Fore.LIGHTWHITE_EX+'\nFinding '+type+' Streamers')
    if len(streamers[type]) != 0:
        for stream in streamers[type]:
            isLive(stream, type)

if config['Open_In_Browser']:
    print(Fore.LIGHTWHITE_EX+'\nOpened all streamers that are live currently!')
input(Fore.LIGHTWHITE_EX+'Press enter to close.')