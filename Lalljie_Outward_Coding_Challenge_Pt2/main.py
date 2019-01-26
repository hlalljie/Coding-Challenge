'''
Outward Coding Challenge Pt.2

Created on Jan 25, 2019

@author: Hayden Lalljie
'''
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import ElementNotInteractableException
from selenium.webdriver.support.select import Select
from selenium.webdriver.firefox.options import Options

# Disables location notification 
options = Options()
options.set_preference("dom.webnotifications.enabled", False)
options.set_preference("geo.enabled", False)
driver = webdriver.Firefox(firefox_options=options)

def main():
    ValidateStore("Arizona")
    ValidateStore("Texas")
    
def ValidateStore(store_location):    
    # Navigates to westelm store locator page
    driver.get("https://www.westelm.com/customer-service/store-locator.html?cm_sp=SuperNav-_-Stores")
    time.sleep(2)   #wait for possible popup to appear
    # Clicks out of popup
    try:
        driver.find_element_by_class_name("stickyOverlayMinimizeButton").click()
    except NoSuchElementException and ElementNotInteractableException:
        pass
    # Circumvent endless search for location by entering random search and clicking back to all stores
    address_bar = driver.find_element_by_id("address-text")
    address_bar.send_keys("abcd")   #no result search criteria
    address_bar.send_keys(Keys.RETURN)
    time.sleep(2)   #wait for page to load
    driver.find_element_by_xpath(("//a[@class='c-store-locator__map-search-toggle-link js-toggle-store-map-list']")).click()
    # Find the state in list
    select = Select(driver.find_element_by_id('state-list-selector'))
    select.select_by_visible_text(store_location)
    # Count and print the number of results in the United States drop down
    loc_list = driver.find_elements_by_xpath("//ul[@class = 'c-store-locator__directory-tab-content-stores filtered-results-list']/li[@class = 'c-store-locator__directory-tab-content-store v2-list-item']")
    print("Selecting " + store_location + " in the Store locator gave " + str(len(loc_list)) + " results.")
    
main()