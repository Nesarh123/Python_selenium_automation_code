# Importing necessary modules
import logging
import time
from selenium.common import NoSuchElementException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from Flow.Bases.Base_class import baseclass
from Flow.Utilities.Utils import utils


# Assignee class for automating the task of bulk assigning SKUs
class Assignee(baseclass):
    # Initialize logger with INFO level
    logs = utils.logger(loglevel=logging.INFO)

    # Constructor to initialize the driver and parent class
    def __init__(self, driver):
        super().__init__(driver)  # Call base class constructor
        self.driver = driver      # Set local driver

    double_click = "//tbody/tr[2]/td"
    assign = "//span[normalize-space()='Assign Users']"

    # XPath locators for various UI elements used in the bulk assign flow
    bulk_assign = "//span[normalize-space()='Bulk Assign']"
    selected_tasks = "//input[@id='numberOfSelectedTasks']"
    assignee_role = "//input[@id='{}']" #Format Example: editor
    tat = "//input[@id='{}']" # Format Example: editor-TAT
    date = "//div[@class='ant-picker-cell-inner'][normalize-space()='{}']" # Format Example: 30
    bulk_assign_button = "(//span[contains(text(),'Bulk Assign')])[2]"

    # XPath locators for various UI elements used in the individual assign flow
    roles = "(//input[contains(@id,'rc_select')])"
    tat_i = "//input[@value='{} - 12:00 AM']" #Format Example: 30 Jul 2025
    date_i = "//td[@title='{}']//div[@class='ant-picker-cell-inner']" #Format Example: 2025-07-30
    submit_button = "//span[normalize-space()='Submit']"

    #XPath locators common for both assign flow
    assignee_user = "//div[@name='{}']//div[@class='ant-select-item-option-content']" #Format Example: editor h
    all_dates = "//div[@class='ant-picker-cell-inner']"
    ok_button = "//span[normalize-space()='OK']"

    #Wait Methods
    def wait_double_click(self):
        self.wait_for_clickability_of_element(By.XPATH, self.double_click)

    def wait_assign(self):
        self.wait_for_clickability_of_element(By.XPATH, self.assign)

    def wait_bulk_assign(self):
        self.wait_for_clickability_of_element(By.XPATH, self.bulk_assign)

    def wait_selected_tasks(self):
        self.wait_for_visibility_of_element(By.XPATH, self.selected_tasks)

    def wait_assignee_role(self, role):
        self.wait_for_clickability_of_element(By.XPATH, self.assignee_role.format(role))

    def wait_tat(self, role_tat):
        self.wait_for_clickability_of_element(By.XPATH, self.tat.format(role_tat))

    def wait_date(self):
        self.wait_for_clickability_of_element(By.XPATH, self.date)

    def wait_bulk_assign_button(self):
        self.wait_for_clickability_of_element(By.XPATH, self.bulk_assign_button)

    def wait_roles(self):
        self.wait_for_presence_of_all_elements(By.XPATH, self.roles)

    def wait_tat_i(self):
        self.wait_for_clickability_of_element(By.XPATH, self.tat_i)

    def wait_date_i(self):
        self.wait_for_clickability_of_element(By.XPATH, self.date_i)

    def wait_submit_button(self):
        self.wait_for_clickability_of_element(By.XPATH, self.submit_button)

    def wait_assignee_user(self, user):
        self.wait_for_clickability_of_element(By.XPATH, self.assignee_user.format(user))

    def wait_all_dates(self):
        self.wait_for_clickability_of_element(By.XPATH, self.all_dates)

    def wait_ok(self):
        self.wait_for_clickability_of_element(By.XPATH, self.ok_button)

    #Get_Methods
    def get_double_click(self):
        return self.driver.find_element(By.XPATH, self.double_click)

    def get_assign(self):
        return self.driver.find_element(By.XPATH, self.assign)

    def get_bulk_assign(self):
        return self.driver.find_element(By.XPATH, self.bulk_assign)

    def get_selected_tasks(self):
        return self.driver.find_element(By.XPATH, self.selected_tasks)

    def get_assignee_role(self, role):
        return self.driver.find_element(By.XPATH, self.assignee_role.format(role))

    def get_tat(self, role_tat):
        return self.driver.find_element(By.XPATH, self.tat.format(role_tat))

    def get_date(self, specific_date):
        return self.driver.find_element(By.XPATH, self.date.format(specific_date))

    def get_bulk_assign_button(self):
        return self.driver.find_element(By.XPATH, self.bulk_assign_button)

    def get_roles(self):
        return self.driver.find_elements(By.XPATH, self.roles)

    def get_tat_i(self, specific_tat_i):
        return self.driver.find_element(By.XPATH, self.tat_i.format(specific_tat_i))

    def get_date_i(self, specific_date_i):
        return self.driver.find_element(By.XPATH, self.date_i.format(specific_date_i))

    def get_submit_button(self):
        return self.driver.find_element(By.XPATH, self.submit_button)

    def get_assignee_user(self, role_assignee_user):
        return self.driver.find_element(By.XPATH, self.assignee_user.format(role_assignee_user))

    def get_all_dates(self):
        return self.driver.find_element(By.XPATH, self.all_dates)

    def get_ok(self):
        return self.driver.find_element(By.XPATH, self.ok_button)

    # ---- Action Methods ----
    # These methods perform complete actions using wait and getter methods
    def double_clicked(self):
        """Double-click on the tab"""
        self.wait_double_click()
        dc = self.get_double_click()
        ActionChains(self.driver).double_click(dc).perform()
        self.logs.info("Clicked the tab")

    def assigned(self):
        """Click on Assign Users tab"""
        self.wait_assign()
        self.get_assign().click()
        self.logs.info("Clicked on Assign Users")

    def bulk_assigned (self):
        """Click on Bulk Assign tab"""
        self.wait_bulk_assign()
        self.get_bulk_assign().click()
        self.logs.info("Clicked on Bulk Assign Users")

    def enter_number_of_tasks(self, number):
        """Enter the number of tasks"""
        self.wait_selected_tasks()
        self.get_selected_tasks().send_keys(number)
        self.logs.info("Entered the number of tasks")

    def editor(self, role, user):
        """Assigning the task to an assignee"""
        self.wait_assignee_role(role)
        self.get_assignee_role(role).click()
        time.sleep(2)
        self.wait_assignee_user(user)
        self.get_assignee_user(user).click()
        self.logs.info("Task has been assigned")

    def user_tat(self, role_tat, date):
        """Assigning the TAT"""
        self.wait_tat(role_tat)
        self.get_tat(role_tat).click()
        time.sleep(2)
        # Handle both int and datetime.date objects
        try:
            day = str(date.day)
        except AttributeError:
            day = str(date)
        # Loop through calendar elements and select the matching date
        elements = self.driver.find_elements(By.XPATH, self.all_dates)
        for elem in elements:
            if elem.text.strip() == day:
                elem.click()
                break
        else:
            raise NoSuchElementException(f"TAT date '{day}' not found in calendar.")
        self.wait_ok()
        self.get_ok().click()
        self.logs.info("TAT has been assigned")

    def click_bulk_assign(self):
        self.wait_bulk_assign_button()
        self.get_bulk_assign_button().click()

    def role_indi(self):
        """Clicks on every 3rd input field (indexes 3, 6, 9, ...) matching the rc_select pattern."""
        self.wait_roles()
        elements = self.get_roles()

        for i in range(2, len(elements), 3):  # Indexes 2, 5, 8, ...
            try:
                elem = elements[i]
                self.driver.execute_script("arguments[0].scrollIntoView(true);", elem)
                elem.click()
                time.sleep(0.5)
            except Exception as e:
                self.logs.warning(f"Failed to click element at index {i + 1}: {e}")

    #Then perform the same script as def editor(self, role, user):

    def tat_indi(self, role_tat_i, date):
        """Assigning the tat for individual user"""
        self.wait_tat_i()
        self.get_tat_i(role_tat_i).click()
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
        self.logs.info("TAT has been assigned for individual user")

    def submit(self):
        self.wait_submit_button()
        self.get_submit_button().click()


    # Decide if the user click on bulk assign or assigns individually
    def assigning(self, flow_type, role, role_tat, specific_date, specific_tat_i, specific_date_i, role_assignee_user, number_of_tasks):
        if flow_type == 'bulk_assign':
            self.logs.info("Initiating Bulk Assign Flow")
            self.bulk_assign_flow(role, role_tat, specific_date, role_assignee_user, number_of_tasks)

        elif flow_type == 'individual_assign':
            self.logs.info("Initiating Individual Assign Flow")
            self.individual_assign_flow(role,specific_date_i, specific_tat_i, role_assignee_user)

    # Bulk Assign Flow
    def bulk_assign_flow(self, role, role_tat, specific_date, role_assignee_user, number_of_tasks):
        self.double_clicked()
        self.assigned()
        self.bulk_assigned()
        self.enter_number_of_tasks(number_of_tasks)
        self.editor(role, role_assignee_user)
        self.user_tat(role_tat, specific_date)
        self.click_bulk_assign()

    # Individual Assign Flow
    def individual_assign_flow(self, role, date_i, tat_i, role_assignee_user):
        self.double_clicked()
        self.assigned()
        self.role_indi()
        self.editor(role, role_assignee_user)
        self.tat_indi(date_i, tat_i)