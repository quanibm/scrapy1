
import os
from selenium import webdriver
from scrapy.selector import Selector

# driver = os.path.join(os.path.abspath("."), '../driver/chromedriver')

browser = webdriver.Chrome(executable_path=os.path.join(os.path.abspath("."), '../driver/chromedriver'))


browser.get("http://1331gg.com/")
browser.find_element_by_tag_name('input').send_keys("11111")
# browser.find_element_by_class_name(".SignFlow-accountInput.Input-wrapper input[name='username']").send_keys("09561333006")
# browser.find_element_by_class_name(".Input-wrapper input[name='password']").send_keys("20120...")
# browser.find_element_by_class_name(".Button.SignFlow-submitButton.Button--primary.Button--blue").click()

# browser.find_element_by_id()


t_selector = Selector(text=browser.page_source)
print(browser.page_source)