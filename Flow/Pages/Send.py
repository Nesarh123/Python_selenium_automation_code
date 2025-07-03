# Import required modules for logging and web element interaction
import logging
from selenium.webdriver.common.by import By
from Flow.Bases.Base_class import baseclass
from Flow.Utilities.Utils import utils


# The Send class is responsible for handling notification-related actions,
# specifically clicking the "Send Notification" button in the UI.
class Send(baseclass):
    # Initialize logger to track actions and debugging information
    logs = utils.logger(loglevel=logging.INFO)

    # Constructor: initializes the WebDriver and inherits base utility methods
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # ----- LOCATOR -----
    # XPath to locate the 'Send Notification' button
    send_button = "//span[@class='send-notification-btn']"

    # ----- WAIT METHOD -----
    def wait_send_button(self):
        """
        Waits until the 'Send' button is clickable.
        Prevents interaction errors due to slow loading or animations.
        """
        self.wait_for_clickability_of_element(By.XPATH, self.send_button)

    # ----- GETTER METHOD -----
    def get_send_button(self):
        """
        Retrieves the WebElement for the 'Send' button.
        """
        return self.driver.find_element(By.XPATH, self.send_button)

    # ----- ACTION METHOD -----
    def send(self):
        """
        Clicks the 'Send' button to trigger the notification action.
        Logs the action for traceability in test execution reports.
        """
        self.get_send_button().click()
        self.logs.info("Send Button Clicked")