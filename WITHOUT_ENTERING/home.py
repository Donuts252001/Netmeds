# from curses import window
from selenium import webdriver
import os
import constant
from selenium.webdriver.common.keys import Keys

class Home(webdriver.Edge):
    def __init__(self, driver_path=r"C:/Users/vaish/Desktop/Self Learning/Cloud/DEVOPS/SELENIUM",teardown=False):
        self.driver_path=driver_path
        self.teardown=teardown
        os.environ['PATH']+=self.driver_path
        
        options=webdriver.EdgeOptions()
        options.add_experimental_option('excludeSwitches',['enable-logging'])
        super(Home,self).__init__(options=options)
        self.implicitly_wait(10)
        self.maximize_window()
        
    def __exit__(self,*args):
        if self.teardown:
            self.quit()
        
    def landing(self):
        self.get(constant.link)
        
    def preq(self):
        pincode=self.find_element_by_id("delivery_details")
        pincode.click()
        enterpin=self.find_element_by_id("rel_pincode")
        enterpin.send_keys('421201')
        print('END')
        
    def searching(self):
        searchbox=self.find_element_by_css_selector(
            'input[name="q"]'
        )
        searchbox.click()
        searchbox.send_keys('Sanitiser')
        searchbox.send_keys(Keys.ENTER)
    
    def collecting(self):
        # self.execute(self.scroll(500))
        allsearch=self.find_element_by_css_selector(
            'ol[id="algolia_hits"]'
        )
        divs=allsearch.find_elements_by_css_selector('*')
        for div in divs:
            name=div.find_element_by_class_name('info').get_attribute('innerHTML').strip()
            print(name)
        
        
    def adding(self):
        addbutton=self.find_element_by_css_selector(
            'button[title="ADD TO CART"]'
        )
        addbutton.click()
        
    def carting(self):
        cart=self.find_element_by_id("minicart_btn")
        cart.click()
    
    def proceeding(self):
        proceed=self.find_element_by_css_selector(
            'button[class="btn-checkout btn btn_to_checkout"]'
        )
        proceed.click()
            
        
        