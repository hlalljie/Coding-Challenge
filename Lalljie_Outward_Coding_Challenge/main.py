'''
Outward Coding Challenge Pt.1

Created on Jan 25, 2019

@author: Hayden lalljie
'''
#imports
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException 

# open Firefox
driver = webdriver.Firefox()
def main(): 
    
    search = SearchTest() #initialize a SearchTest object   
    search_value_list = [2613243, 123456] #values to test
    search.ValidateSearchValueList(search_value_list) #call function to test
    
# Conducts a test on the search functionality based on the given sku
#ValidateSearchValue to validate w/ one sku ValidateSearchValueList to validate w/ a list of search values
class SearchTest:
    
    # Performs search using the given value and prints the validity of value
    def ValidateSearchValue(self, search_value):    
        self.search_value = search_value
        driver.get("https://www.westelm.com")   #navigates to westelm homepage
        # finds search field and enters search value
        search_bar = driver.find_element_by_id("search-field")
        search_bar.send_keys(self.search_value)
        search_bar.send_keys(Keys.RETURN)
        if self.ValidateURL():  #check that url is correct
            if self.ValidateImage():
                print(str(self.search_value) + " is a valid sku.")
            else:
                self.TestFail()
        else:
            self.TestFail()
    
    # Checks the validity of multiple values in a list
    def ValidateSearchValueList(self, search_values):
        for value in search_values:
            self.ValidateSearchValue(value)
            
    # Returns true if url contains correct sku value and is a 'products' page
    def ValidateURL(self):
        time.sleep(5)  #wait for page to load
        url = driver.current_url
        # checks if url conatins the sku and the word 'products'
        if str(self.search_value) in url and "products" in url:
            return True           
        return False    #implicit else
    
    # Returns True if product image object exists
    def ValidateImage(self):
        time.sleep(5)   #wait for page to load
        try:
            driver.find_element_by_id("pipHeroAnchor")  #image holder for product image
        except NoSuchElementException:
            return False
        return True
    
    # Takes Screenshot and sends prints msg for failed test    
    def TestFail(self):
        driver.save_screenshot(str(self.search_value) + ".png")
        print(str(self.search_value) + " is an invalid sku.")
    
main()