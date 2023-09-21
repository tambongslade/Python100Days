from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
option = Options()
option.add_argument("--window-size=1980,1080")
chrome_path = "D:\\Drivers\\chromedriver.exe"
# Use ChromeDriverManager to automatically download and manage Chrome WebDriver
driver = webdriver.Chrome(option)
driver.get("http://google.com")



