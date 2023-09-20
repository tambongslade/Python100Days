from selenium import webdriver
from selenium.webdriver.common.by import By
chrome_option = webdriver.ChromeOptions()
chrome_option.add_experimental_option("detach", True)
driver = webdriver.Chrome(chrome_option)
driver.get("https://www.amazon.com/Skytech-Gaming-PC-Desktop-Windows/dp/B0BXCJVKHF/?_encoding=UTF8&pd_rd_w=Mc4dr&content-id=amzn1.sym.952cfb50-b01e-485f-be6e-00434541418b%3Aamzn1.symc.e5c80209-769f-4ade-a325-2eaec14b8e0e&pf_rd_p=952cfb50-b01e-485f-be6e-00434541418b&pf_rd_r=4GS1WRS91MPP5R4FT2MX&pd_rd_wg=O54SU&pd_rd_r=1ee18bbb-8e76-48a2-99b1-0f7207022588&ref_=pd_gw_ci_mcx_mr_hp_atf_m&th=1")

price_dollar =driver.find_elements(By.CLASS_NAME,value="a-price-whole")