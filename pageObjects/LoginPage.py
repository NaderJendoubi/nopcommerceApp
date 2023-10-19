from selenium import webdriver
from selenium.webdriver.common.by import By


class LoginPage:
    # Locators
    textbox_usermail_id = "Email"
    textbox_password_id = "Password"
    button_login_xpath = "//button[@class='button-1 login-button']"
    link_logout_linktext = "Logout"

    def __init__(self, driver):
        self.driver = driver

    def setUserMail(self, usermail):
        self.driver.find_element(By.ID, self.textbox_usermail_id).clear()
        self.driver.find_element(By.ID, self.textbox_usermail_id).send_keys(usermail)

    def setPassword(self, password):
        self.driver.find_element(By.ID, self.textbox_password_id).clear()
        self.driver.find_element(By.ID, self.textbox_password_id).send_keys(password)

    def clickLogin(self):
        self.driver.find_element(By.XPATH, self.button_login_xpath).click()

    def clickLogout(self):
        self.driver.find_element(By.LINK_TEXT, self.link_logout_linktext).click()
