import os
import time
from selenium import webdriver 
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC 
from selenium.webdriver.common.keys import Keys 
from selenium.webdriver.common.by import By 
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import config as cfg

class browserAutomation:
    def __init__(self):
        self.__binaryLocation = cfg.binaryLocation
        if not os.path.isfile(cfg.driverPath):
            raise Exception("Chrome driver deos not exist")
        self.__driverPath = cfg.driverPath
        self.__wait = None
    
    def openBrowser(self, url):
        """
        Returns a driver object
        
        :param binaryLocation: str, absolute path to chrome binary
        :param driverPath: str, absolute path to chrome driver
        """
        cap = DesiredCapabilities.CHROME
        cap = {'binary_location': self.__binaryLocation}
        driver = webdriver.Chrome(desired_capabilities=cap, executable_path=self.__driverPath)
        driver.get(url)
        self.__wait = WebDriverWait(driver, 600)


    def selectContact(self, contactname):
        """
        Selects a contact/group from whatsapp with the given name.
        
        :param groupname: str, string to select
        """
        target = '"'+contactname+'"'
        x_arg = '//span[contains(@title,' + target + ')]'
        title = self.__wait.until(EC.presence_of_element_located(( By.XPATH, x_arg)))
        title.click()
        print(target)


    def sendMessage(self, string):
        """
        Sends a message on the selected group.
        
        :param string: str, string to send
        """
        inp_xpath = '//div[@class="_3FRCZ copyable-text selectable-text"][@dir="ltr"][@data-tab="1"]'
        input_box = self.__wait.until(EC.presence_of_element_located(( By.XPATH, inp_xpath)))
        input_box.send_keys(string + Keys.ENTER)
        time.sleep(2)

