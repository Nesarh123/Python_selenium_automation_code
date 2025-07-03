# Importing necessary modules
import logging
import time
from selenium.webdriver.common.by import By
from selenium.common.exceptions import StaleElementReferenceException
from Flow.Bases.Base_class import baseclass
from Flow.Utilities.Utils import utils


# Login class inherits from baseclass for reusing common Selenium methods
class Login(baseclass):
    # Initializing the logger for this class with INFO level
    logs = utils.logger(loglevel=logging.INFO)

    # Constructor to initialize the WebDriver instance
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators for login-related web elements (in XPath)
    login = "//div[@class='flex h-full items-center']"
    email = "//input[@id='username']"
    password = "//input[@id='password']"
    proceed = "//button[normalize-space()='Continue']"
    demo = "(//button[@class])[2]"

    # Waits until the login element is clickable
    def wait_login(self):
        self.wait_for_clickability_of_element(By.XPATH, self.login)

    def get_click_login(self):
        return self.driver.find_element(By.XPATH, self.login)

    def wait_email(self):
        self.wait_for_visibility_of_element(By.XPATH, self.email)

    def get_email(self):
        return self.driver.find_element(By.XPATH, self.email)

    def wait_password(self):
        self.wait_for_visibility_of_element(By.XPATH, self.password)

    def get_password(self):
        return self.driver.find_element(By.XPATH, self.password)

    def wait_proceed(self):
        self.wait_for_clickability_of_element(By.XPATH, self.proceed)

    def get_proceed(self):
        return self.driver.find_element(By.XPATH, self.proceed)

    # Updated wait_demo to return the clickable element
    def wait_demo(self):
        self.wait_for_clickability_of_element(By.XPATH, self.demo)

    def get_demo(self):
        return self.driver.find_element(By.XPATH, self.demo)

    # Complete login process using given username and password
    def get_login(self, username, password):
        self.wait_login()
        self.get_click_login().click()
        self.logs.info("clicked on login")

        self.wait_email()
        self.get_email().send_keys(username)
        self.logs.info("username entered")

        self.wait_password()
        self.get_password().send_keys(password)
        self.logs.info("password entered")

        self.wait_proceed()
        self.get_proceed().click()
        self.logs.info("clicked on proceed")

        try:
            self.wait_demo()
            self.get_demo().click()
            self.logs.info("clicked on demo")
        except StaleElementReferenceException:
            self.logs.warning("StaleElementReferenceException: Retrying demo button click...")
            time.sleep(1)
            self.wait_demo()
            self.get_demo().click()
            self.logs.info("Retried and clicked on demo")






