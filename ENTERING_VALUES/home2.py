from encodings import search_function
from selenium import webdriver
import os
from  selenium.webdriver.common.keys import  Keys

class Home2(webdriver.Edge):
    def __init__(self,driver_path=r"C:/Users/vaish/Desktop/Self Learning/Cloud/DEVOPS/SELENIUM",teardown=False):
        self.teardown=teardown
        self.driver_path=driver_path
        os.environ['PATH']+=self.driver_path
        
        options=webdriver.EdgeOptions()
        options.add_experimental_option('excludeSwitches',['enable-logging'])
        super(Home2, self).__init__(options=options)
        self.implicitly_wait(10)
        self.maximize_window()
        
    def __exit__(self, *args):
        if self.teardown==False:
            self.quit()
            
    def search(self):
        searchbox=self.find_element_by_id('search')
        searchbox.click()
        searchbox.send_keys('Sanitiser')
        searchbox.send_keys(Keys.ENTER)
    
    