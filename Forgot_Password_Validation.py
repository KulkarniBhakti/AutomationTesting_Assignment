from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

service = Service(r"D:\Windows\chromedriver.exe")
driver = webdriver.Chrome(service=service)
driver.get("https://app-staging.nokodr.com/super/apps/auth/v1/index.html#/login")
driver.find_element(By.XPATH, "//button[text()='Email or Phone']").click()
email_phone_input = driver.find_element(By.XPATH, "//input[@type='text']")
email_phone_input.send_keys("registereduser@example.com")
driver.find_element(By.XPATH, "//button[text()='Submit']").click()
try:
    success_message = driver.find_element(By.CLASS_NAME, "success").text
    print("Forgot Password Success:", success_message)
except:
    error_message = driver.find_element(By.CLASS_NAME, "error").text
    print("Forgot Password Error:", error_message)
driver.quit()
