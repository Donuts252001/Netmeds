from selenium import webdriver
import os
import constant


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
        
    def fitness(self):
        fit=self.find_element_by_css_selector('a[href="/non-prescriptions/fitness"]')
        print(fit)
        fit.click()
        
        
    def filters(self):
        close=self.find_element_by_id("webklipper-publisher-widget-container-notification-close")
        close.click()
        sports=self.find_element_by_css_selector('a[ href="https://www.netmeds.com/non-prescriptions/fitness/sports-supplements"]')
        print("sports",sports)
        sports.click()
        pincode=self.find_element_by_id("delivery_details")
        pincode.click()
        enterpin=self.find_element_by_id("rel_pincode")
        enterpin.send_keys('421201')
        sorting=self.find_element_by_css_selector("div[class='sort-option']")
        sorts=sorting.find_elements_by_css_selector('*')
        for sort in sorts:
            print(sort)
        self.execute_script("window.scrollTo(0,500)")
    
    def lowtohigh(self):
        sorting=self.find_element_by_css_selector("div[class='sort-option']")
        sorts=sorting.find_elements_by_css_selector('*')
        for sort in sorts:
            print(sort)
            
        
    def products(self):
        self.find_element_by_xpath('//*[@id="algolia_hits"]/div/div/ol/li[1]')
        addcart=self.find_element_by_css_selector('button[title="ADD TO CART"]')
        addcart.click()
        cart=self.find_element_by_id("minicart_btn")
        cart.click()
        proceed=self.find_element_by_class_name("process-checkout")
        proceed.click()
        # uploading=self.find_element_by_xpath("/html/body/app-root/app-checkout/div/main/section/div/app-upload-rx/div[1]/div/div[1]/div[1]/div[3]/div/form/button")
        # uploading.click()
        # gallery=self.find_element_by_xpath("/html/body/app-root/app-checkout/div/main/section/div/app-upload-rx/div[5]/div/div/div[2]/form/div/ul/li/label/input")
        # gallery.click()
    
    def confirm(self):
        consult=self.find_element_by_id("externaldoctr")
        consult.click()
        list=self.find_elements("*")
        for i in list:
            if i.innerHTML.strip()=="Review Order":
                i.click()
        
        