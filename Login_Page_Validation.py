from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

service = Service(r"D:\Windows\chromedriver.exe")
driver = webdriver.Chrome(service=service)
driver.get("https://app-staging.nokodr.com/super/apps/auth/v1/index.html#/login")
driver.find_element(By.XPATH, "//button[text()='Email or Phone']").click()
driver.find_element(By.XPATH, "//button[text()='Password or Otp']").click()
email_input = driver.find_element(By.XPATH, "//input[@type='text']")
email_input.send_keys("testuser@example.com")
password_input = driver.find_element(By.XPATH, "//input[@type='password']")
password_input.send_keys("Password@123")
driver.find_element(By.XPATH, "//button[text()='Log IN']").click()
try:
    success_message = driver.find_element(By.CLASS_NAME, "success").text
    print("Login Success:", success_message)
except:
    error_message = driver.find_element(By.CLASS_NAME, "error").text
    print("Login Error:", error_message)
driver.quit()
