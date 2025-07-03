# Importing required modules
import logging
from selenium.webdriver.common.by import By
from Flow.Bases.Base_class import baseclass
from Flow.Utilities.Utils import utils


# This class handles the process of uploading and submitting a file (SKU template) on a web form
class UploadFile(baseclass):
    # Initialize a logger instance for this class
    logs = utils.logger(loglevel=logging.INFO)

    # Constructor: Inherits the baseclass and stores driver instance
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # ---------- LOCATORS ----------
    # XPath for file upload input field (third file input on the page)
    upload_file = "(//input[@type = 'file' and @name = 'file'])[3]"

    # XPath for the submit button after file upload
    submit = "//button[@type='submit']"

    # (Optional) Previously included download template functionality (currently commented)
    # download_file = "//span[normalize-space()='Download Sample SKU Editor Template']"

    # ---------- WAIT METHODS ----------

    def wait_upload_file(self):
        """Waits until the file input field is present in the DOM"""
        self.wait_for_presence_of_element(By.XPATH, self.upload_file)

    def wait_submit(self):
        """Waits until the submit button becomes clickable"""
        self.wait_for_clickability_of_element(By.XPATH, self.submit)

    # ---------- GET METHODS ----------

    def get_upload_file(self):
        """Fetches the WebElement for the upload input"""
        return self.driver.find_element(By.XPATH, self.upload_file)

    def get_submit(self):
        """Fetches the WebElement for the submit button"""
        return self.driver.find_element(By.XPATH, self.submit)

    # ---------- FILE ACTIONS ----------

    def send_upload_file(self, project_type):
        """
        Scrolls to the file input field and sends the local file path to simulate file upload.
        This method directly interacts with the OS file system path.
        """
        file_input = self.get_upload_file()

        # Scroll to the element to ensure it's in the viewport
        self.driver.execute_script("arguments[0].scrollIntoView(true);", file_input)

        # Choose file path based on project type
        if project_type.lower() == "cataloging":
            # Sends the local file path to the <input type="file"> element
            file_input.send_keys(r"C:\Users\Admin\Downloads\sku-template.xlsx")
        elif project_type.lower() == "content":
            # Sends the local file path to the <input type="file"> element
            file_input.send_keys(r"C:\Users\Admin\Downloads\TASK-BULK-UPLOAD-TEMPLATE.xlsx")
        else:
            raise ValueError(f"Unsupported project type for file upload: {project_type}")


    def click_submit(self):
        """Clicks on the submit button to complete the upload process"""
        self.get_submit().click()

    # ---------- HIGH-LEVEL METHOD ----------

    def uploadfile(self, project_type):
        """
        Full workflow:
        1. Wait for upload field to be present
        2. Send file path to the upload input
        3. Wait for submit button and click it
        Logs are generated after each successful action for traceability.
        """
        # self.wait_download_file()         # (Optional: if download template feature is needed)
        # self.click_download_file()
        # time.sleep(5)                     # Allow file to download

        self.wait_upload_file()
        self.send_upload_file(project_type)
        self.logs.info("File uploaded")

        self.wait_submit()
        self.click_submit()
        self.logs.info("File submitted")
