# Import necessary modules
import logging
import time

from selenium.webdriver.common.by import By
from Flow.Bases.Base_class import baseclass
from Flow.Utilities.Utils import utils


# Complete class handles the final stage of SKU processing where SKUs are reviewed and submitted.
class Complete(baseclass):
    # Logger instance for tracking execution
    logs = utils.logger(loglevel=logging.INFO)

    # Constructor: initializes the WebDriver and base class
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # ----- XPATH LOCATORS -----
    # Elements used during final completion stage
    edit = "//span[normalize-space()='Edit SKUs']"  # Button to initiate SKU editing
    submit_button = "//span[normalize-space() = 'check_circle']"  # Button to submit SKUs after editing
    left_bar = "//div[@class='bar completed-bar-active left-bar']" # First element of the stage bar element
    middle_bar = "//div[@class='bar middle-bar completed-bar-active']" # Second element of the stage bar element
    right_bar = "//div[@class='bar right-bar completed-bar-active']" # Third element of the stage bar element
    completed_text = "//div[contains(text(),'Completed')]" #Text shown after clicking the submit button
    success_message = "//div[@class = 'description-success']"  # Message shown after successful submission


    # ----- WAIT METHODS -----
    # Ensure elements are ready for interaction before proceeding

    def wait_edit(self):
        """Waits until the 'Edit SKUs' button is clickable"""
        self.wait_for_clickability_of_element(By.XPATH, self.edit)

    def wait_left_bar(self):
        """Waits until the 'left bar' button is present"""
        self.wait_for_presence_of_element(By.XPATH, self.left_bar)

    def wait_middle_bar(self):
        """Waits until the 'middle bar' button is present"""
        self.wait_for_presence_of_element(By.XPATH, self.middle_bar)

    def wait_right_bar(self):
        """Waits until the 'right bar' button is present"""
        self.wait_for_presence_of_element(By.XPATH, self.right_bar)

    def wait_submit_button(self):
        """Waits until the 'Submit' icon is present in the DOM"""
        self.wait_for_presence_of_element(By.XPATH, self.submit_button)

    def wait_success_message(self):
        """Waits until the success message is visible after submission"""
        self.wait_for_visibility_of_element(By.XPATH, self.success_message)

    def wait_task_status(self):
        """Waits until the 'Task Status' button is completed"""
        self.wait_for_clickability_of_element(By.XPATH, self.task_status)


    # ----- GETTER METHODS -----
    # Return the actual WebElement to interact with it

    def get_edit(self):
        """Returns the 'Edit SKUs' button WebElement"""
        return self.driver.find_element(By.XPATH, self.edit)

    def get_left_stage_bar(self):
        """Returns the 'Left Stage Bar' button WebElement"""
        return self.driver.find_element(By.XPATH, self.left_bar)

    def get_middle_bar(self):
        """Returns the 'Middle Stage Bar' button WebElement"""
        return self.driver.find_element(By.XPATH, self.middle_bar)

    def get_right_stage_bar(self):
        """Returns the 'Right Stage Bar' button WebElement"""
        return self.driver.find_element(By.XPATH, self.right_bar)

    def get_submit_button(self):
        """Returns the 'Submit' button WebElement"""
        return self.driver.find_element(By.XPATH, self.submit_button)

    def get_complete_text(self):
        """Returns the 'Complete Text' message WebElement"""
        return self.driver.find_element(By.XPATH, self.completed_text)


    def get_success_message(self):
        """Returns the success message WebElement"""
        return self.driver.find_element(By.XPATH, self.success_message)

    def get_task_status(self):
        """Returns the task status WebElement"""
        return self.driver.find_element(By.XPATH, self.task_status)

    # ----- ACTION METHOD -----
    def perform_submission(self):
        """Clicks the submit button"""
        self.wait_submit_button()
        self.get_submit_button().click()
        self.logs.info("Submit Button Clicked")

    def completed(self):
        """
        Completes the SKU task by:
        1. Clicking 'Edit SKUs'
        2. Scrolling horizontally to reveal stage bars
        3. Looping through each stage (AM -> Cataloger -> AM) and performing submission
        4. Verifying task completion and success message
        """

        # Step 1: Edit SKUs
        self.wait_edit()
        self.get_edit().click()
        self.logs.info("Edit Button Clicked")

        # Step 2: Scroll to ensure all stage bars are visible
        time.sleep(3)
        self.page_wide_scroll()
        time.sleep(3)

        # Step 3: Handle all 3 stages in order
        stages = [
            {"wait": self.wait_left_bar, "get": self.get_left_stage_bar,
             "log": "AM has assigned the task to the cataloger"},
            {"wait": self.wait_middle_bar, "get": self.get_middle_bar,
             "log": "Cataloger has completed the task and clicked on submit button"},
            {"wait": self.wait_right_bar, "get": self.get_right_stage_bar, "log": "AM has approved the task"},
        ]

        for stage in stages:
            try:
                stage["wait"]()  # Wait for stage element
                stage["get"]()  # Get stage element (or click inside if needed)
                self.perform_submission()  # Perform submission action
                self.logs.info(stage["log"])  # Log the stage step
            except Exception as e:
                self.logs.error(f"Stage failed: {stage['log']} | Error: {str(e)}")
                raise

        # Step 4: Verify task completion and success confirmation
        assert self.get_complete_text().is_displayed()
        self.logs.info("The task is completed")

        self.wait_success_message()
        assert self.get_success_message().is_displayed()
        self.logs.info("Success Message Displayed")