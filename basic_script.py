#automation script using Selenium & Navigate to a noKodr platform

from selenium import webdriver

service = Service(r"D:\Windows\chromedriver.exe")
driver = webdriver.Chrome(service=service)

driver.get("https://app-staging.nokodr.com/")

driver.implicitly_wait(5)

driver.quit()
