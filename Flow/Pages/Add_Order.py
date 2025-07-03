# Import necessary modules
import logging
import time

from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By

from Flow.Bases.Base_class import baseclass
from Flow.Utilities.Utils import utils


# Class for automating the "Add Order" functionality
class Add_Order(baseclass):
    # Logger setup
    logs = utils.logger(loglevel=logging.INFO)

    # Constructor to initialize WebDriver and base class
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # XPath locators for various fields in the "Add Order" page
    select_dropdown_items = "//div[@class='ant-select-item-option-content']"
    select_project_type = "//input[@id='projectType']"
    select_catalog = "//div[@class='ant-select-item-option-content'][normalize-space() = '{}']"
    select_work_type = "//input[@id='workType']"
    select_project = "//div[@class='ant-select-item-option-content'][normalize-space()= '{}']"
    select_order_name = "//input[@id='name']"
    select_order_type = "//input[@id='orderType']"
    select_POC = "//div[@class='ant-select-item-option-content'][normalize-space()='{}']"
    select_account_manager = "//input[@id='assigneeId']"
    select_manager = "//span[normalize-space()='{}']"
    select_client_name = "//input[@id='clientId']"
    select_demo = "//span[@class='capitalize'][normalize-space()='{}']"
    select_poc_name = "//input[@id='employeeId']"
    select_poc = "//div[@name='{}']//div[@class='ant-select-item-option-content']"
    select_client_work_type = "//div[@class='ant-select-selection-overflow']"
    select_client_catalog = "//div[@class='ant-select-item ant-select-item-option ant-select-item-option-active']//div[@class='ant-select-item-option-content'][normalize-space()='{}']"
    select_tat = "//input[@id='turnAroundTime']"
    select_all_dates = "//td[@title]"
    select_date = "//td[@title='{}']" #Date_Format = "YYY-MM-DD"
    select_ok = "//span[normalize-space()='OK']"
    select_cut_paste = "//span[@title='Enabled']"
    cut_paste_select = "(//div[@class='ant-select-item-option-content'][normalize-space()='{}'])[1]"
    select_AI_Editor = "(//span[@title='Disabled'])[1]"
    AI_Editor_select = "//div[contains(text(),'{}')]"
    select_enable_copyscape = "(//span[@title='Disabled'])[2]"
    enable_copyscape_select = "(//div[@class='ant-select-item-option-content'][normalize-space()='{}'])[3]"
    select_AI_Checker = "(//span[@title='Disabled'])[3]"
    AI_Checker_select = "(//div[@class='ant-select-item-option-content'][normalize-space()='{}'])[4]"
    select_sku = "//input[@id='skuCount']"
    select_description = "//textarea[@id='description']"
    select_next = "//button[@type='submit']"

    # ---- Wait Methods ----
    # These ensure the elements are ready before interaction
    def wait_dropdown_items(self):
        self.wait_for_presence_of_all_elements(By.XPATH, self.select_dropdown_items)

    def wait_project_type(self):
        self.wait_for_presence_of_element(By.XPATH, self.select_project_type)

    def wait_catalog(self):
        self.wait_for_clickability_of_element(By.XPATH, self.select_catalog)

    def wait_work_type(self):
        self.wait_for_presence_of_element(By.XPATH, self.select_work_type)

    def wait_project(self):
        self.wait_for_clickability_of_element(By.XPATH, self.select_project)

    def wait_order_name(self):
        self.wait_for_visibility_of_element(By.XPATH, self.select_order_name)

    def wait_order_type(self):
        self.wait_for_presence_of_element(By.XPATH, self.select_order_type)

    def wait_POC(self):
        self.wait_for_clickability_of_element(By.XPATH, self.select_POC)

    def wait_account_manager(self):
        self.wait_for_presence_of_element(By.XPATH, self.select_account_manager)

    def wait_manager(self):
        self.wait_for_clickability_of_element(By.XPATH, self.select_manager)

    def wait_client_name(self):
        self.wait_for_presence_of_element(By.XPATH, self.select_client_name)

    def wait_demo(self):
        self.wait_for_clickability_of_element(By.XPATH, self.select_demo)

    def wait_poc_name(self):
        self.wait_for_presence_of_element(By.XPATH, self.select_poc_name)

    def wait_poc(self):
        self.wait_for_clickability_of_element(By.XPATH, self.select_poc)

    def wait_client_work_type(self):
        self.wait_for_clickability_of_element(By.XPATH, self.select_client_work_type)

    def wait_client_catalog(self):
        self.wait_for_presence_of_element(By.XPATH, self.select_client_catalog)

    def wait_tat(self):
        self.wait_for_clickability_of_element(By.XPATH, self.select_tat)

    def wait_all_dates(self):
        self.wait_for_clickability_of_element(By.XPATH, self.select_all_dates)

    def wait_date(self):
        self.wait_for_clickability_of_element(By.XPATH, self.select_date)

    def wait_ok(self):
        self.wait_for_clickability_of_element(By.XPATH, self.select_ok)

    def wait_cut_paste(self):
        self.wait_for_clickability_of_element(By.XPATH, self.select_cut_paste)

    def wait_cut_paste_select(self):
        self.wait_for_clickability_of_element(By.XPATH, self.cut_paste_select)

    def wait_ai_editor(self):
        self.wait_for_clickability_of_element(By.XPATH, self.select_AI_Editor)

    def wait_ai_editor_select(self):
        self.wait_for_clickability_of_element(By.XPATH, self.AI_Editor_select)

    def wait_enable_copyscape(self):
        self.wait_for_clickability_of_element(By.XPATH, self.select_enable_copyscape)

    def wait_enable_copyscape_select(self):
        self.wait_for_clickability_of_element(By.XPATH, self.enable_copyscape_select)

    def wait_ai_checker(self):
        self.wait_for_clickability_of_element(By.XPATH, self.select_AI_Checker)

    def wait_ai_checker_select(self):
        self.wait_for_clickability_of_element(By.XPATH, self.AI_Checker_select)

    def wait_sku(self):
        self.wait_for_visibility_of_element(By.XPATH, self.select_sku)

    def wait_description(self):
        self.wait_for_visibility_of_element(By.XPATH, self.select_description)

    def wait_next(self):
        self.wait_for_clickability_of_element(By.XPATH, self.select_next)

    # ---- Getter Methods ----
    # These return web elements to perform actions on them
    def get_dropdown_items(self):
        return self.driver.find_elements(By.XPATH, self.select_dropdown_items)

    def get_project_type(self):
        return self.driver.find_element(By.XPATH, self.select_project_type)

    def get_catalog(self, project_type):
        return self.driver.find_element(By.XPATH, self.select_catalog.format(project_type))

    def get_work_type(self):
        return self.driver.find_element(By.XPATH, self.select_work_type)

    def get_project(self, work_type):
        return self.driver.find_element(By.XPATH, self.select_project.format(work_type))

    def get_order_name(self):
        return self.driver.find_element(By.XPATH, self.select_order_name)

    def get_order_type(self):
        return self.driver.find_element(By.XPATH, self.select_order_type)

    def get_POC(self, order_type):
        return self.driver.find_element(By.XPATH, self.select_POC.format(order_type))

    def get_account_manager(self):
        return self.driver.find_element(By.XPATH, self.select_account_manager)

    def get_manager(self, account_manager):
        return self.driver.find_element(By.XPATH, self.select_manager.format(account_manager))

    def get_client_name(self):
        return self.driver.find_element(By.XPATH, self.select_client_name)

    def get_demo(self, client_name):
        return self.driver.find_element(By.XPATH, self.select_demo.format(client_name))

    def get_poc_name(self):
        return self.driver.find_element(By.XPATH, self.select_poc_name)

    def get_poc(self, poc_name):
        return self.driver.find_element(By.XPATH, self.select_poc.format(poc_name))

    def get_client_work_type(self):
        return self.driver.find_element(By.XPATH, self.select_client_work_type)

    def get_client_catalog(self, client_work_type):
        return self.driver.find_element(By.XPATH, self.select_client_catalog.format(client_work_type))

    def get_tat(self):
        return self.driver.find_element(By.XPATH, self.select_tat)

    def get_all_dates(self):
        return self.driver.find_elements(By.XPATH, self.select_all_dates)

    def get_date(self, date):
        return self.driver.find_element(By.XPATH, self.select_date.format(date))

    def get_ok(self):
        return self.driver.find_element(By.XPATH, self.select_ok)

    def get_cut_paste(self):
        return self.driver.find_element(By.XPATH, self.select_cut_paste)

    def get_cut_paste_select(self, cut_paste_select):
        return self.driver.find_element(By.XPATH, self.cut_paste_select.format(cut_paste_select))

    def get_ai_editor(self):
        return self.driver.find_element(By.XPATH, self.select_AI_Editor)

    def get_ai_editor_select(self, ai_editor_type):
        return self.driver.find_element(By.XPATH, self.AI_Editor_select.format(ai_editor_type))

    def get_enable_copyscape(self):
        return self.driver.find_element(By.XPATH, self.select_enable_copyscape)

    def get_enable_copyscape_select(self, copyscape_type):
        return self.driver.find_element(By.XPATH, self.enable_copyscape_select.format(copyscape_type))

    def get_ai_checker(self):
        return self.driver.find_element(By.XPATH, self.select_AI_Checker)

    def get_ai_checker_select(self, ai_checker_type):
        return self.driver.find_element(By.XPATH, self.AI_Checker_select.format(ai_checker_type))

    def get_sku(self):
        return self.driver.find_element(By.XPATH, self.select_sku)

    def get_description(self):
        return self.driver.find_element(By.XPATH, self.select_description)

    def get_next(self):
        return self.driver.find_element(By.XPATH, self.select_next)

    # Reusable method to safely select an option by visible text from any open dropdown
    def select_dropdown_item(self, option_text):
        self.wait_dropdown_items()
        for option in self.get_dropdown_items():
            if option.text.strip() == option_text:
                option.click()
                return
        raise NoSuchElementException(f"Option '{option_text}' not found in dropdown.")

    # ---- Action Methods ----
    # These methods perform complete actions using wait and getter methods
    def project_type(self, project_type):
        """Selects a project type from the dropdown list"""
        self.wait_project_type()
        self.get_project_type().click() # Open dropdown
        time.sleep(2)
        self.select_dropdown_item(project_type)  # Select item

    def work_type(self, work_type):
        """Selects a work type based on the selected project type"""
        self.wait_work_type()
        self.get_work_type().click()
        time.sleep(2)
        self.select_dropdown_item(work_type)  # Select item

    def order_name(self, order_name):
        """Inputs a custom order name into the text field"""
        self.wait_order_name()
        self.get_order_name().send_keys(order_name)

    def order_type(self, order_type):
        """Selects the order type from a dropdown and corresponding POC"""
        self.wait_order_type()
        self.get_order_type().click()
        time.sleep(2)
        self.select_dropdown_item(order_type)  # Select item

    def account_manager(self, account_manager):
        """Assigns an account manager by selecting from a dropdown"""
        self.wait_account_manager()
        self.get_account_manager().click()
        time.sleep(2)
        self.select_dropdown_item(account_manager)  # Select item

    def client_name(self, client_name):
        """Selects the client name from suggestions"""
        self.wait_client_name()
        self.get_client_name().click()
        time.sleep(2)
        self.select_dropdown_item(client_name)  # Select item

    def poc_name(self, poc_name):
        """Selects the POC name associated with the client"""
        self.wait_poc_name()
        self.get_poc_name().click()
        time.sleep(2)
        self.select_dropdown_item(poc_name)  # Select item

    def client_work_type(self, client_work_type):
        """Selects the client-specific work type from dropdown"""
        self.wait_client_work_type()
        self.get_client_work_type().click()
        time.sleep(2)
        self.select_dropdown_item(client_work_type)  # Select item

    def tat(self, date):
        """Selects Turn Around Time (TAT) from calendar widget"""
        self.wait_tat()
        self.get_tat().click()
        time.sleep(2)
        day = str(date.day)
        for elem in self.get_all_dates():
            if elem.text.strip() == day:
                elem.click()
                break
        else:
            raise NoSuchElementException(f"TAT date '{date}' not found in calendar.")

        self.wait_ok()
        self.get_ok().click()

    def cut_paste(self, cut_paste_type):
        """Selects the cut_paste from the dropdown"""
        self.wait_cut_paste()
        self.get_cut_paste().click()
        time.sleep(2)
        self.select_dropdown_item(cut_paste_type)

    def ai_editor(self, ai_editor_select):
        """Selects an AI editor from the dropdown"""
        self.wait_ai_editor()
        self.get_ai_editor().click()
        time.sleep(2)
        self.select_dropdown_item(ai_editor_select)

    def enable_copyscape(self, copyscape_type):
        """Selects the enable copyscape from the dropdown"""
        self.wait_enable_copyscape()
        self.get_enable_copyscape().click()
        time.sleep(2)
        self.select_dropdown_item(copyscape_type)

    def ai_checker(self, ai_checker_type):
        """Selects an AI checker from the dropdown"""
        self.wait_ai_checker()
        self.get_ai_checker().click()
        time.sleep(2)
        self.select_dropdown_item(ai_checker_type)

    def no_of_sku(self, sku_number):
        """Inputs a custom order name into the text field"""
        self.wait_sku()
        self.get_sku().send_keys(sku_number)

    def description(self, description):
        """Fills in the project description text area"""
        self.wait_description()
        self.get_description().send_keys(description)

    def next(self):
        """Clicks on the 'Next' button to proceed to the next page or section"""
        self.wait_next()
        self.get_next().click()

    def common_steps(self, order_name, order_type, account_manager,
                     client_name, poc_name, client_work_type, tat, description):
        """Common Steps Shared Across All Flows"""
        # Enter a unique order name
        self.order_name(order_name)
        self.logs.info("Order Name Entered")

        # Select order type and POC
        self.order_type(order_type)
        self.logs.info("Order Type Selected")

        # Assign an account manager to the order
        self.account_manager(account_manager)
        self.logs.info("Account Manager Selected")

        # Select client name
        self.client_name(client_name)
        self.logs.info("Client Name Selected")

        # Assign a POC for the client
        self.poc_name(poc_name)
        self.logs.info("POC Name Selected")

        # Choose the work type specific to this client
        self.client_work_type(client_work_type)
        self.logs.info("Client Work Type Selected")

        # Select the expected TAT date
        self.tat(tat)
        self.logs.info("TAT Selected")

        # Add description about the order for context
        self.description(description)
        self.logs.info("Description Entered")

    try:
        # ----- COMPOSITE FLOW -----
        def add_order(self, project_type, work_type, order_name, order_type,
              account_manager, client_name, poc_name,
              client_work_type, tat, desc_text, ai_editor=None, cut_paste=None,
              enable_copyscape=None, ai_checker=None, no_of_sku = None):
            """
            Full workflow to fill and submit the 'Add Order' form
            Accepts all required input values as parameters
            """

            # Select project type
            self.project_type(project_type)
            self.logs.info("Project Type Selected")

            order = project_type.strip().lower()

            if order == "cataloging":

                # Select work type based on project type
                self.work_type(work_type)
                self.logs.info("Work Type Selected")

                # Call the common steps method
                self.common_steps(order_name, order_type, account_manager, client_name, poc_name, client_work_type, tat,desc_text)

                # Scroll the page
                self.page_scroll()

                # Select the cut_paste type
                self.cut_paste(cut_paste)
                self.logs.info("Cut Paste Selected")

                # Enter the number of sku's to be added
                self.no_of_sku(no_of_sku)
                self.logs.info("No Of Sku Entered")

            elif order == "content":

                # Select work type based on project type
                self.work_type(work_type)
                self.logs.info("Work Type Selected")

                # Call the common steps method
                self.common_steps(order_name, order_type, account_manager, client_name, poc_name, client_work_type, tat, desc_text)

                # Select the AI Editor
                self.ai_editor(ai_editor)
                self.logs.info("AI Editor Selected")

                # Scroll the page
                self.page_scroll()

                # Select the cut_paste type
                self.cut_paste(cut_paste)
                self.logs.info("Cut Paste Selected")

                # Select the Enable Copyscape
                self.enable_copyscape(enable_copyscape)
                self.logs.info("Enable Copyscape Selected")

                # Select the AI Checker
                self.ai_checker(ai_checker)
                self.logs.info("AI Checker Selected")


            elif project_type.strip().lower() == "other task":
                # Call the common steps method
                self.common_steps(order_name, order_type, account_manager,
                                  client_name, poc_name, client_work_type, tat, desc_text)

                # Enter the number of sku's to be added
                self.no_of_sku(no_of_sku)
                self.logs.info("No Of Sku Entered")


            # Click on Next to complete the page/form
            self.next()
            self.logs.info("Next Button Clicked")

    except NoSuchElementException as e:
        raise e