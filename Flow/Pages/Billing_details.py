# Importing necessary modules
import logging
from selenium.webdriver.common.by import By
from Flow.Bases.Base_class import baseclass
from Flow.Utilities.Utils import utils


# Billing class handles the pricing screen actions in the billing module
class Billing(baseclass):
    # Initialize the logger with INFO level
    logs = utils.logger(loglevel = logging.INFO)

    # Constructor to initialize WebDriver and call parent constructor
    def __init__(self, driver):
        super().__init__(driver)  # Initialize baseclass with driver
        self.driver = driver      # Set local driver instance
        self.select_pricing = None # Track which pricing user selects

    # XPath locators for web elements related to pricing
    select_project_level = "//div[contains(text(),'Project Level Pricing')]"
    select_sku_level = "//div[contains(text(),'SKU Level Pricing')]"
    select_word_level = "//div[contains(text(),'Word Level Pricing')]"
    enter_project_price = "//input[@id='totalProjectBilling']"
    enter_sku_price = "//input[@id='companyPricePerSku']"
    enter_sku_freelancer_price = "//input[@id='freelancerPricePerSku']"
    enter_client_price = "//input[@id='companyPricePerWord']"
    enter_word_freelancer_price = "//input[@id='companyPricePerWord']"
    next = "//span[normalize-space()='Next']"

    # Wait Methods
    # Waits until the "Project Level Pricing" option is clickable
    def wait_project(self):
        self.wait_for_clickability_of_element(By.XPATH, self.select_project_level)

    # Waits until the "SKU Level Pricing" option is clickable
    def wait_sku(self):
        self.wait_for_clickability_of_element(By.XPATH, self.select_sku_level)

    # Waits until the "Word Level Pricing" option is clickable
    def wait_word(self):
        self.wait_for_clickability_of_element(By.XPATH, self.select_word_level)

    # Waits until the price input field for "Total Project Revenue" is visible
    def wait_project_price(self):
        self.wait_for_visibility_of_element(By.XPATH, self.enter_project_price)

    # Waits until the price input field for "Price Per SKU" is visible
    def wait_sku_price(self):
        self.wait_for_visibility_of_element(By.XPATH, self.enter_sku_price)

    # Waits until the price input field for "Freelancer Price Per SKU" is visible
    def wait_sku_freelancer_price(self):
        self.wait_for_visibility_of_element(By.XPATH, self.enter_sku_freelancer_price)

    # Waits until the price input field for "Client Price Per Word" is visible
    def wait_client_price(self):
        self.wait_for_visibility_of_element(By.XPATH, self.enter_client_price)

    # Waits until the price input field for "Freelancer Price Per Word" is visible
    def wait_word_freelancer_price(self):
        self.wait_for_visibility_of_element(By.XPATH, self.enter_word_freelancer_price)

    # Waits until the "Next" button is visible
    def wait_next(self):
        self.wait_for_visibility_of_element(By.XPATH, self.next)

    # Get Methods
    # Returns the "Project Level Pricing" web element
    def get_project(self):
        return self.driver.find_element(By.XPATH, self.select_project_level)

    # Returns the "SKU Level Pricing" web element
    def get_sku(self):
        return self.driver.find_element(By.XPATH, self.select_sku_level)

    # Returns the "Word Level Pricing" web element
    def get_word(self):
        return self.driver.find_element(By.XPATH, self.select_word_level)

    # Returns the price input field for "Total Project Revenue"
    def get_project_price(self):
        return self.driver.find_element(By.XPATH, self.enter_project_price)

    # Returns the price input field for "Price Per SKU" is visible
    def get_sku_price(self):
        return self.driver.find_element(By.XPATH, self.enter_sku_price)

    # Returns the price input field for "Freelancer Price Per SKU"
    def get_sku_freelancer_price(self):
        return self.driver.find_element(By.XPATH, self.enter_sku_freelancer_price)

    # Returns the price input field for "Client Price Per Word"
    def get_client_price(self):
        return self.driver.find_element(By.XPATH, self.enter_client_price)

    # Returns the price input field for "Freelancer Price Per Word"
    def get_word_freelancer_price(self):
        return self.driver.find_element(By.XPATH, self.enter_word_freelancer_price)

    # Returns the "Next" button web element
    def get_next(self):
        return self.driver.find_element(By.XPATH, self.next)

    # Action Methods
    # Project Pricing Method

    def project_pricing(self, project_price):
        self.select_pricing = "project"  # Assign the select_pricing to project
        self.wait_project()  # Wait for the "Project Level Pricing" option to appear
        self.get_project().click()  # Click on "Project Level Pricing"
        self.logs.info("Clicked on Project Level Pricing")

        self.wait_project_price()  # Wait for "Total Project Revenue" input field to be visible
        self.get_project_price().send_keys(project_price)  # Enter the given price
        self.logs.info("Entered price for Project Level Pricing")

    def sku_pricing(self, sku_price, sku_freelancer_price):
        self.select_pricing = "sku"  # Assign the select_pricing to sku
        self.wait_sku() # Wait for the "SKU Level Pricing" option to appear
        self.get_sku().click()  # Click on "SKU Level Pricing"
        self.logs.info("Clicked on Sku Level Pricing")

        self.wait_sku_price() # Wait for "Price Per SKU" input field
        self.get_sku_price().send_keys(sku_price) # Enter the "Price Per SKU"
        self.logs.info("Entered price on Sku Level Pricing")

        self.wait_sku_freelancer_price() # Wait for "Freelancer Price Per SKU" input field to be visible
        self.get_sku_freelancer_price().send_keys(sku_freelancer_price)  # Enter the "Freelancer Price Per SKU"
        self.logs.info("Entered price on Freelancer Sku Level Pricing")

    def word_pricing(self, word_price, word_freelancer_price):
        self.select_pricing = "word"  # Assign the select_pricing to word
        self.wait_word() # Wait for the "Word Level Pricing" option to appear
        self.get_word().click()   # Click on "Word Level Pricing"
        self.logs.info("Clicked on Word Level Pricing")

        self.wait_client_price() # Wait for the "Client Price Per Word" option to appear
        self.get_client_price().send_keys(word_price) # Enter the "Client Price Per Word"
        self.logs.info("Entered price on Word Level Pricing")

        self.wait_word_freelancer_price() # Wait for the "Client Price Per Word" option to appear
        self.get_word_freelancer_price().send_keys(word_freelancer_price) # Enter the "Client Price Per Word"
        self.logs.info("Entered price on Freelancer Word Level Pricing")

    # Performs the complete pricing flow
    def price(self, project_type, project_price, sku_price, sku_freelancer_price, word_price, word_freelancer_price):
        try:
            # Automatically determine which pricing element is available
            if self.is_element_present(By.XPATH, self.select_project_level):
                self.select_pricing = "project"
            elif self.is_element_present(By.XPATH, self.select_sku_level):
                self.select_pricing = "sku"
            elif self.is_element_present(By.XPATH, self.select_word_level):
                self.select_pricing = "word"
            else:
                self.logs.error("No valid pricing method found on screen")
                raise ValueError("No valid pricing method found on screen")

            if project_type.lower() == "cataloging" or project_type.lower() == "other task":
                if self.select_pricing == "project":
                    self.project_pricing(project_price)
                elif self.select_pricing == "sku":
                    self.sku_pricing(sku_price, sku_freelancer_price)
                else:
                    self.logs.error("Selected pricing is not available")
                    raise ValueError

            elif project_type.lower() == "content":
                if self.select_pricing == "project":
                    self.project_pricing(project_price)
                elif self.select_pricing == "sku":
                    self.sku_pricing(sku_price, sku_freelancer_price)
                elif self.select_pricing == "word":
                    self.word_pricing(word_price, word_freelancer_price)
                else:
                    self.logs.error("Selected pricing is not available")
                    raise ValueError

            self.wait_next() # Wait till the next button is clickable
            self.get_next().click() # Click on next button
            self.logs.info("Clicked on Next button")

        except Exception as e:
            raise e