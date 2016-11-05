from selenium import webdriver
import os
from Task1.data import commons
from Task1.pop.mainPage import MainPage
import unittest
import time


class MedTest(unittest.TestCase):

    def setUp(self):
        configFile = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), 'data', 'credentials.json')
        form = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), 'data', 'expenceInfoiceDataForm.json')
        self.credentials = commons.loadJson(configFile)
        self.form = commons.loadJson(form)
        self.greenNotificationWindow = '223, 240, 216'

        options = webdriver.ChromeOptions()
        options.add_experimental_option("excludeSwitches", ["ignore-certificate-errors"])
        chromedriver = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), 'data', 'chromedriver.exe')

        self.driver = webdriver.Chrome(chromedriver, chrome_options=options)
        self.mainPage = MainPage(self.driver)
        self.mainPage.navigateToPage('https://cloud.mediusflow.com/rndQA/LocalAccount/')

    def tearDown(self):
        time.sleep(5)
        self.driver.quit()

    def test01(self):
        self.mainPage.loginToPage(self.credentials['login'], self.credentials['password'])
        self.mainPage.navigateToTab()
        self.mainPage.fillForm(self.form)
        currentWindowColor = self.mainPage.getNotificationColorValue()
        assert self.greenNotificationWindow in currentWindowColor, \
            "The color of notification window is '{0}' while it should be '{1}'".format(currentWindowColor,
                                                                                        self.greenNotificationWindow)
