# Import required modules
import logging
from selenium.webdriver.common.by import By
from Flow.Bases.Base_class import baseclass
from Flow.Utilities.Utils import utils


# Order class handles interactions on the main order listing page, specifically for adding a new order.
class Order(baseclass):
    # Logger instance initialized with INFO level for debugging and reporting
    logs = utils.logger(loglevel=logging.INFO)

    # Constructor: accepts the Selenium WebDriver instance
    def __init__(self, driver):
        super().__init__(driver)  # Call to baseclass constructor for utility methods
        self.driver = driver      # Assign driver for local use in this class

    # ----- LOCATOR -----
    # XPath to locate the 'Add Order' button on the page
    add_order = "(//button)[2]"  # Assumes the second button on the page is 'Add Order'

    # ----- WAIT METHOD -----
    def wait_add_order(self):
        """
        Waits until the 'Add Order' button becomes clickable.
        Prevents script failure due to timing or loading issues.
        """
        self.wait_for_clickability_of_element(By.XPATH, self.add_order)

    # ----- GETTER METHOD -----
    def get_add_order(self):
        """
        Returns the WebElement of the 'Add Order' button.
        Used for performing click or visibility actions.
        """
        return self.driver.find_element(By.XPATH, self.add_order)

    # ----- ACTION METHOD -----
    def click_add_order(self):
        """
        Performs click action on the 'Add Order' button.
        Logs the action for reporting/debugging purposes.
        """
        self.get_add_order().click()
        self.logs.info("Clicked on Add Order")


