import time
import pytest
from pageObjects.LoginPage import LoginPage
from pageObjects.AddCustomerPage import AddCustomer
from pageObjects.SearchCustomerPage import SearchCustomer
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen


class Test_SearchCustomerByName_005:
    baseURL = ReadConfig.getApplicationURL()
    usermail = ReadConfig.getUserMail()
    password = ReadConfig.getPassword()
    logger = LogGen.loggen()  # Logger

    @pytest.mark.regression
    def test_searchCustomerByName(self, setup):
        self.logger.info("************* SearchCustomerByName_005 **********")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        # LOGIN
        self.lp = LoginPage(self.driver)
        self.lp.setUserMail(self.usermail)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        self.logger.info("************* Login successful **********")

        # ADD THE CUSTOMER
        self.logger.info("******* Starting Search Customer By Name **********")
        self.addcust = AddCustomer(self.driver)
        self.addcust.clickOnCustomersMenu()
        self.addcust.clickOnCustomerMenuItem()

        # SEARCH THE CUSTOMER
        self.logger.info("************* Searching customer by Name **********")
        search_cust = SearchCustomer(self.driver)
        search_cust.setFirstName("Victoria")
        search_cust.setLastName("Terces")
        search_cust.clickSearch()
        time.sleep(5)
        status = search_cust.searchCustomerByName("Victoria Terces")
        assert True == status
        self.logger.info("***************  TC_SearchCustomerByName_005 Finished  *********** ")
        self.driver.close()
