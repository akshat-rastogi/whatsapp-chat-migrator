import os
import time
import emoji
from dateutil.parser import parse
from whatsapp import browserAutomation
import config as cfg

# Read constants from config file
chatsFolder = cfg.chatsFolder
restoredFolder = cfg.restoredFolder

# STEP 1: VALIDATION
# validations to check if the chats folder exist, 
#   folder to store restored chats exist
#   and chrome driver exists
if not os.path.exists(chatsFolder):
    raise Exception("Chat folder do not exist. Terminating")

if not os.path.exists(restoredFolder):
    try:
        os.mkdir(restoredFolder)
    except OSError:
        raise Exception("Creation of the directory %s failed" % restoredFolder)
else:
    print ("Successfully created the directory %s to store restored chats.\n" % restoredFolder)


# Ask if the contact exist, create driver and open whatsapp web
print("Create the Groups/Contact in whatsapp with the following names: \n")

for file in os.listdir(chatsFolder):
    filename = 'B-{}'.format(str(file[19:-4]))
    print(filename)
print("\n")

continue_process = input("Have you created all the groups ? (y/n):")

# If the anwwer is no then terminate script
if continue_process[0].lower() == 'y':
    print('Restoring Backup')
else:
    print('Terminating')
    exit()



# STEP 2: OPEN BROWSER 
whatsapp = browserAutomation()
whatsapp.openBrowser('https://web.whatsapp.com')



# STEP 3: IMPORT CHATS

# Helper function to see if the string is of type date
def is_date(string, fuzzy=False):
    """
    Return whether the string can be interpreted as a date.

    :param string: str, string to check for date
    :param fuzzy: bool, ignore unknown tokens in string if True
    """
    try:
        parse(string, fuzzy=fuzzy)
        return True

    except ValueError:
        return False


# Iterate through all the files and send messages in whatsapp
for file in os.listdir(chatsFolder):
    filename = 'B-{}'.format(str(file[19:-4]))
    whatsapp.selectContact(filename.strip())
    # Strips the newline character from the end of message
    message_file = open(chatsFolder+file, 'r') 
    Lines = message_file.readlines()    
    message = ""    
    for line in Lines:
        if is_date(line[0:8]):
            #  replace emoji in msg with black
            whatsapp.sendMessage(emoji.demojize(message, delimiters=("", "")))
            message = line   
        else:
            message = message + line
    
    os.rename(chatsFolder+file, restoredFolder+filename)
