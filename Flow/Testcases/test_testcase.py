import time
import pytest

# Importing Page Object Model (POM) classes for each page/screen
from Flow.Pages.Add_Order import Add_Order  # Handles filling out the Add Order form
from Flow.Pages.Assign_Users import Assignee  # Handles assigning tasks via Bulk Assign
from Flow.Pages.Billing_details import Billing  # Handles entering billing information
from Flow.Pages.Order import Order  # Handles clicking the 'Add Order' button
from Flow.Pages.Send import Send  # Handles sending notification for submission
from Flow.Pages.Submit_For_Production import submit  # Handles Cataloguer selection and date submission
from Flow.Pages.Upload_File import UploadFile  # Handles uploading SKU files
from Flow.Pages.login import Login  # Handles login functionality

# Utility class for logging and reading data from Excel
from Flow.Utilities.Utils import utils

# Load test data from Excel file and Sheet1 into result_data list
# Each row from Excel is passed as parameters to the test
result_data = utils.read_xlsx("D:\\Automation\\Rubick_Assignment\\Flow\\Testdata\\Test_data.xlsx", "Sheet1")


# Base test class using PyTest's fixture for setup
@pytest.mark.usefixtures("setup")
class TestCase:

    # Test is run with each row of Excel data (parameterized)
    @pytest.mark.parametrize(
        ("username", "password", "project_type", "work_type", "order_name", "order_type", "account_manager", "client_name", "poc_name", "client_work_type", "tat", "ai_editor",
         "cut_paste" , "enable_copyscape", "ai_checker", "no_of_sku", "desc_text", "project_price", "sku_price", "sku_freelancer_price", "word_price", "word_freelancer_price",
         "assign_team", "date", "flow_type", "role", "role_tat", "specific_date", "specific_tat_i", "specific_date_i", "role_assignee_user", "number_of_tasks"),
        result_data
    )
    def test_login(self, username, password, project_type, work_type, order_name, order_type, account_manager, client_name, poc_name, client_work_type, tat, ai_editor, cut_paste,
                   enable_copyscape, ai_checker, no_of_sku,desc_text, project_price, sku_price, sku_freelancer_price, word_price, word_freelancer_price, assign_team, date, flow_type,
                   role, role_tat, specific_date, specific_tat_i, specific_date_i, role_assignee_user, number_of_tasks):
        # Step 1: Login to the application
        self.lp = Login(self.driver)
        self.lp.get_login(username, password)
        time.sleep(5) # Wait for dashboard to load after login

        # Step 2: Click "Add Order" button
        self.add = Order(self.driver)
        self.add.click_add_order()
        time.sleep(5)  # Wait for Add Order form to load

        # Step 3: Fill out and submit order creation form
        self.order = Add_Order(self.driver)
        self.order.add_order(
            project_type, work_type, order_name, order_type,
            account_manager, client_name, poc_name,
            client_work_type, tat, desc_text,
            ai_editor, cut_paste, enable_copyscape, ai_checker, no_of_sku
        )
        time.sleep(5)  # Wait for next screen transition

        # Step 4: Upload SKU file
        self.upload = UploadFile(self.driver)
        self.upload.uploadfile(project_type)
        time.sleep(5) # Wait for upload confirmation

        # Step 5: Enter billing details and proceed
        self.bill = Billing(self.driver)
        self.bill.price(project_type, project_price, sku_price, sku_freelancer_price, word_price, word_freelancer_price)
        time.sleep(5) # Wait for next page transition

        # # Step 6: Send order for production
        # self.send = Send(self.driver)
        # self.send.send()
        # time.sleep(5) # Wait for cataloguer selection screen
        #
        # # Step 7: Select Cataloguer and Date, then Submit for Production
        # self.submit = submit(self.driver)
        # self.submit.submit_prod(assign_team, date)
        # time.sleep(5)  # Wait for order submission confirmation
        #
        # # Step 8: Assign the task to a user using bulk assign
        # self.assign = Assignee(self.driver)
        # self.assign.assigning(flow_type, role, role_tat, specific_date, specific_tat_i, specific_date_i, role_assignee_user, number_of_tasks)
        # time.sleep(5) # Wait for SKU Viewer to reload

        # Step 9: Complete the order by clicking Edit and Submit
        # self.complete = Complete(self.driver)
        # self.complete.completed()
        # time.sleep(5) # Final confirmation and completion