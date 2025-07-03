# Import necessary modules
import logging
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from Flow.Bases.Base_class import baseclass
from Flow.Utilities.Utils import utils

class submit(baseclass):
    logs = utils.logger(loglevel=logging.INFO)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # ---------- LOCATORS ----------
    team = "//span[contains(text(),'{}')]"
    calender = "//div[@class='ant-picker-input']"
    all_dates = "//div[@class='ant-picker-cell-inner']"
    dates = "//div[@class='ant-picker-cell-inner'][normalize-space()='{}']"
    ok = "//span[normalize-space()='OK']"
    submit = "//button[@type='submit']"

    # ---------- WAIT METHODS ----------
    def wait_team(self, assign_team):
        formatted_xpath = self.team.format(assign_team)
        self.wait_for_clickability_of_element(By.XPATH, formatted_xpath)

    def wait_calender(self):
        self.wait_for_clickability_of_element(By.XPATH, self.calender)

    def wait_all_dates(self):
        self.wait_for_clickability_of_element(By.XPATH, self.all_dates)

    def wait_date(self, date):
        self.wait_for_clickability_of_element(By.XPATH, self.dates.format(date))

    def wait_ok(self):
        self.wait_for_clickability_of_element(By.XPATH, self.ok)

    def wait_submit(self):
        self.wait_for_clickability_of_element(By.XPATH, self.submit)

    # ---------- GET METHODS ----------
    def get_team(self, assign):
        return self.driver.find_element(By.XPATH, self.team.format(assign))

    def get_calender(self):
        return self.driver.find_element(By.XPATH, self.calender)

    def get_all_dates(self):
        return self.driver.find_elements(By.XPATH, self.all_dates)

    def get_date(self, date):
        xpath = self.dates.format(date)
        return self.driver.find_element(By.XPATH, xpath)

    def get_ok(self):
        return self.driver.find_element(By.XPATH, self.ok)

    def get_submit(self):
        return self.driver.find_element(By.XPATH, self.submit)

    # ---------- ACTION METHODS ----------
    def click_team(self,assign):
        self.wait_team(assign)
        self.get_team(assign).click()

    def click_date(self, date):
        self.wait_calender()
        self.get_calender().click()

        self.wait_all_dates()
        all_dates = self.get_all_dates()
        if all_dates:
            ActionChains(self.driver).click(all_dates[0]).perform()

        self.wait_date(date)
        date_element = self.get_date(date)
        if date_element.is_displayed():
            date_element.click()

    def submit_prod(self, assign_team, date):
        """
        Automates Cataloguer selection, calendar date picking, and order submission.
        Fix: Converts float dates like 30.0 → "30" to match actual calendar values.
        """
        self.click_team(assign_team)
        self.logs.info("Clicked on Cataloguer")

        # Fix: Convert float to string without decimals
        date_str = str(int(date)) if isinstance(date, float) else str(date)

        self.click_date(date_str)
        self.logs.info("Selected the date from calendar")

        self.wait_ok()
        self.get_ok().click()
        self.logs.info("Clicked on OK to confirm date selection")

        self.wait_submit()
        self.get_submit().click()
        self.logs.info("Clicked on Submit to complete the process")