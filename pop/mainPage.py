from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

class MainPage(object):
    def __init__(self, driver):
        self.driver = driver
        self.load_page_timeout = 60
        self.wait = WebDriverWait(driver, 20)
        self.usernameField = "//*[@id='username']"
        self.passwordField = "//*[@id='password']"
        self.loginButton = "//*[@id='login-form']/div/button"
        self.createTab = "//*[@id='create-menu']"
        self.expenseInvoiceTab = "//*[@id='create-menu']/ul/li[2]/a"
        self.userTab = "//*[@id='admin-links']/li[5]/a"
        self.currencyField = "//*[@id='currency']/option[2]"
        self.submitButton = "//*[@id='document-creator-settings']/div[1]/a[3]"
        self.alertWindow = "//*[@class='ui-pnotify stack-bar-bottom']/node()"
        self.singleFieldInput = "//*[@id='document-container']/div/article[1]/section[2]/div//*[contains(text(),'{0}')]/..//input"
        self.singleFieldLoader = "//*[@id='document-container']/div/article[1]/section[2]/div//*[contains(text(),'{0}')]/..//div[@class='indicator loader']"



    def navigateToPage(self, URL):
        self.driver.set_page_load_timeout(self.load_page_timeout)
        self.driver.get(URL)

    def loginToPage(self, login, password):
        self.driver.find_element_by_xpath(self.usernameField).send_keys(login)
        self.driver.find_element_by_xpath(self.passwordField).send_keys(password)
        self.driver.find_element_by_xpath(self.loginButton).click()
        self.wait.until(EC.element_to_be_clickable((By.XPATH, self.userTab)))

    def navigateToTab(self):
        self.wait.until(EC.element_to_be_clickable((By.XPATH, self.createTab))).click()
        self.wait.until(EC.element_to_be_clickable((By.XPATH, self.expenseInvoiceTab))).click()

    def fillForm(self, dataForm):
        # There is a bug - Amount fields are not visible before you chose any currency (even no currency!).
        # As a result we need to click and chose no currency before entering the values
        self.wait.until(EC.element_to_be_clickable((By.XPATH, self.currencyField))).click()

        for name, value in dataForm.items():

            # Entering such (a little bit fancy) xPath we can iterate through all the elements in data/table
            singleField = self.driver.find_element_by_xpath(self.singleFieldInput.format(name))

            # Clearing is needed for Amounts - empty value is hardcoded and equals 0.00
            singleField.clear()
            singleField.send_keys(value)

            # For Company and Supplier we need to wait until loader is not visible. In other case there is an error
            self.wait.until(EC.invisibility_of_element_located((By.XPATH, self.singleFieldLoader.format(name))))
        sleep(2)

    def getNotificationColorValue(self):
        self.driver.find_element_by_xpath(self.submitButton).click()
        element = self.wait.until(EC.element_to_be_clickable((By.XPATH, self.alertWindow)))
        return element.value_of_css_property('background-color')
