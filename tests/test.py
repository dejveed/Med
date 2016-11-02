from selenium import webdriver

options = webdriver.ChromeOptions()
options.add_experimental_option("excludeSwitches", ["ignore-certificate-errors"])
chromedriver = "C:/Users/dejveed/PycharmProjects/Medius/chromedriver.exe"
driver = webdriver.Chrome(chromedriver, chrome_options=options)

driver.get('https://cloud.mediusflow.com/rndQA/LocalAccount/')
