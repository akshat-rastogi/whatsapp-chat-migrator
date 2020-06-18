# Whatspp Chat Migrator

A small script to send message from files exported from whatsapp.

## Requirements

The script was executed in the following environment:

1. Python - (version 3.7.7)
2. Pip - (pip 20.0.2)
3. Selenium - (for browser automation)
4. <a href="https://www.google.com/chrome/">Chrome Browser</a> + <a href="https://chromedriver.storage.googleapis.com/index.html">Chromedriver</a>  

The os used to run the script was Ubuntu 20.04 
(But script is not dependent on OS)

## Installation

#### 1. Python Bindings for Selenium:
```
pip3 install selenium
```
Note: You should install python and pip before installing selenium.

#### 2. Install Chrome browser

You can find the link to download chrome browser from the link below:
<a href="https://www.google.com/chrome/">https://www.google.com/chrome</a> 

#### 3. Download and Extact the chromedriver

You can find the link to download chrome browser from the link below:
<a href="https://chromedriver.storage.googleapis.com/index.html">https://chromedriver.storage.googleapis.com/index.html</a>  

You need to be careful about the version you are going to download. 
The version for chromedriver has to be same as the version of chrome browser. 


## Execution 

Execution is very simple. 

#### 1. You need to set the paths properly in config.py file. You will need to add the paths for the following:

```
# These paths are from my local machine and you will need to change them accordingly. 

# Path for Google Chrome
binaryLocation="/usr/bin/google-chrome-stable"  

# Path for chromedriver that you must downloaded before
driverPath="/home/ubuntu/Desktop/projects/whatsapp-chat-migrator/chromedriver"

# Folder containing the chat backups 
chatsFolder="/home/ubuntu/Desktop/projects/whatsapp-chat-migrator/exports/"

# Once the chat is restored, it will be moved to the restored folder.
restoredFolder="/home/ubuntu/Desktop/projects/whatsapp-chat-migrator/restored/"
```

#### 2. Exceute the code  

```
python3 index.py
```
After you will execute the code, the code is supposed to open an instance of Chrome browser in automation mode automatically. 

The browser will load whatsapp web and will show a QR code. 
You have to scan the code from your phone.

And that's it, now wait for the automation magic !! 

## Using a different browser

If you wish to use a different browser, make sure you download the correct driver for the browser:

```
Chrome:   https://sites.google.com/a/chromium.org/chromedriver/downloads
Edge:     https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/
Firefox:  https://github.com/mozilla/geckodriver/releases
Safari:   https://webkit.org/blog/6900/webdriver-support-in-safari-10/
```

Also, you will have to change a little piece of code in <code>openBrowser()</code> function of whatsapp.py to add support for the browser you want to use.

## Reference:

https://www.selenium.dev/
