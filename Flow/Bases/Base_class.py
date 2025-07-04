# Importing standard modules required for waits and delays
import time
from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Base class containing common reusable utility functions for Selenium-based automation.
# All test page objects will inherit from this base class.
class baseclass:
    def __init__(self, driver):
        """
        Constructor that initializes the WebDriver instance.
        This driver will be used throughout the derived classes to interact with the browser.
        """
        self.driver = driver

    # -------------------------------------
    # Method: page_scroll
    # -------------------------------------
    def page_scroll(self):
        """
        Scrolls vertically to the bottom of the web page until no further scroll height changes.
        Useful for pages that implement infinite scrolling or lazy-loading of data.
        """

        # Scroll to the bottom of the page and capture the height
        pager_element = self.driver.execute_script(
            "window.scrollTo(0, document.body.scrollHeight); return document.body.scrollHeight;")

        match = False

        # Keep scrolling until the page height stops increasing
        while not match:
            last_count = pager_element  # Save previous height
            time.sleep(2)  # Give time for content to load
            pager_element = self.driver.execute_script(
                "window.scrollTo(0, document.body.scrollHeight); return document.body.scrollHeight;")

            # Break the loop if scroll height hasn’t changed
            if last_count == pager_element:
                match = True

    # -------------------------------------
    # Optional: page_wide_scroll (commented)
    # -------------------------------------
    def page_wide_scroll(self):
        """
        Scrolls horizontally to the far right of the web page until no further scroll width changes.
        Useful for pages with horizontal scrollable containers like tables or SKU editors.
        """
        match = False

        last_scroll_width = 0

        while not match:
            # Scroll to the far right
            current_scroll_width = self.driver.execute_script(
                "window.scrollTo(document.body.scrollWidth, 0); return document.body.scrollWidth;")

            if current_scroll_width == last_scroll_width:
                match = True
            else:
                last_scroll_width = current_scroll_width
                time.sleep(2)  # Allow time for lazy-loaded content
    # -------------------------------------
    # Method: wait_for_presence_of_element
    # -------------------------------------
    def wait_for_presence_of_element(self, locator_type, locator_value):
        """
        Waits until the element is present in the DOM, regardless of its visibility.
        Args:
            locator_type: Type of locator (e.g., By.XPATH, By.ID)
            locator_value: The actual locator string
        Returns:
            WebElement once it's located in the DOM
        """
        wait = WebDriverWait(self.driver, 60)
        return wait.until(EC.presence_of_element_located((locator_type, locator_value)))

    # -------------------------------------
    # Method: wait_for_visibility_of_element
    # -------------------------------------
    def wait_for_visibility_of_element(self, locator_type, locator_value):
        """
        Waits until the element is both present and visible on the page.
        Useful to ensure the element can be interacted with.
        Args:
            locator_type: Type of locator (e.g., By.XPATH, By.CSS_SELECTOR)
            locator_value: The locator string
        Returns:
            WebElement when it is visible
        """
        wait = WebDriverWait(self.driver, 60)
        return wait.until(EC.visibility_of_element_located((locator_type, locator_value)))

    # -------------------------------------
    # Method: wait_for_clickability_of_element
    # -------------------------------------
    def wait_for_clickability_of_element(self, locator_type, locator_value):
        """
        Waits until the element is visible and enabled (i.e., ready to be clicked).
        Args:
            locator_type: Type of locator
            locator_value: The locator string
        Returns:
            WebElement once it's clickable
        """
        wait = WebDriverWait(self.driver, 60)
        return wait.until(EC.element_to_be_clickable((locator_type, locator_value)))

    # -------------------------------------
    # Method: wait_for_presence_of_all_elements
    # -------------------------------------
    def wait_for_presence_of_all_elements(self, locator_type, locator_value):
        """
        Waits until the element is visible and enabled (i.e., ready to be clicked).
        Args:
            locator_type: Type of locator
            locator_value: The locator string
        Returns:
            WebElement once it's clickable
        """
        wait = WebDriverWait(self.driver, 60)
        return wait.until(EC.presence_of_all_elements_located((locator_type, locator_value)))

    # -------------------------------------
    # Method: is_element_present
    # -------------------------------------
    def is_element_present(self, locator_type, locator_value):
        """
         Utility method to check if a web element is present on the page
       Args:
            locator_type: Type of locator
            locator_value: The locator string
        Returns:
            WebElement is present on the page
        """
        try:
            # Try to locate the element using the specified locator strategy
            self.driver.find_element(locator_type, locator_value)
            return True # Element is found, return True
        except:
            return False # Element is not found, return False

    # -------------------------------------
    # Method: window_handle
    # -------------------------------------
    def window_handle(self):
        """
        Handles switching control to the newly opened browser window or tab.
        Returns:
            The handle of the new child window
        Behavior:
            - Finds all window handles
            - Switches control to the first child that is not the current window
        """
        parent = self.driver.current_window_handle  # Get the main window handle
        all_handles = self.driver.window_handles     # Get all open window handles

        # Loop through the handles and switch to the new one (if found)
        for handle in all_handles:
            if handle != parent:
                self.driver.switch_to.window(handle)
                return handle
                break

        # If no new handle is found, control stays on parent
        self.driver.switch_to.window(parent)
