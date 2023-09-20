from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

chrome_path = "C:\\Users\\Lenovo\\.cache\\selenium\\chromedriver\\win64\\117.0.5938.88\\chromedriver.exe"
# Use ChromeDriverManager to automatically download and manage Chrome WebDriver
driver = webdriver.Chrome()
pip = webdriver.Chrome(driver.service.path)
