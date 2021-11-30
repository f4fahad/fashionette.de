import time
from selenium.webdriver.common.by import By

class LoginPage:
    popup_banner_id = "uc-btn-accept-banner"
    button_loginPage_class = "header__user-icon"
    textbox_email_name = "email"
    textbox_password_class = "login__password"
    button_login_class = "btn__submit"
    link_logout_linktext = "Logout"

    button_personalData_xpath = "/html/body/div[3]/div[2]/div/div[1]/div[2]/div/ul/li[2]/div/a"
    button_editData_class = "account--address__action--update"
    textbox_firstName_name = "firstName"
    textbox_lastName_name = "lastName"
    button_saveData_class = "account--address__action--save"
    textbox_firstName_class = "account__content__column--customer"
    text_UserInfo_class = "account__firstname"




    def __init__(self, setup):
        self.driver = setup

    def clickPopupBanner(self):
        self.driver.find_element(By.ID, self.popup_banner_id).click()

    def clickLoginPage(self):
        self.driver.find_element(By.CLASS_NAME, self.button_loginPage_class).click()

    def setUserName(self, username):
        time.sleep(1)
        self.driver.find_element(By.NAME, self.textbox_email_name).clear()
        self.driver.find_element(By.NAME, self.textbox_email_name).send_keys(username)

    def setPassword(self, password):
        time.sleep(2)
        self.driver.find_element(By.CLASS_NAME, self.textbox_password_class).clear()
        self.driver.find_element(By.CLASS_NAME, self.textbox_password_class).send_keys(password)

    def clickLogin(self):
        self.driver.find_element(By.CLASS_NAME, self.button_login_class).click()

    def clickLogout(self):
        self.driver.find_element(By.LINK_TEXT, self.link_logout_linktext).click()

    def clickPersonalData(self):
        self.driver.find_element(By.XPATH, self.button_personalData_xpath).click()

    def clickEditData(self):
        self.driver.find_element(By.CLASS_NAME, self.button_editData_class).click()

    def setFirstName(self, firstName):
        time.sleep(1)
        self.driver.find_element(By.NAME, self.textbox_firstName_name).clear()
        self.driver.find_element(By.NAME, self.textbox_firstName_name).send_keys(firstName)

    def setLastName(self, lastName):
        time.sleep(1)
        self.driver.find_element(By.NAME, self.textbox_lastName_name).clear()
        self.driver.find_element(By.NAME, self.textbox_lastName_name).send_keys(lastName)

    def clickUserInfoSave(self):
        self.driver.find_element(By.CLASS_NAME, self.button_saveData_class).click()

    def getUserInfo(self):
        FirstNameElement = self.driver.find_element(By.CLASS_NAME, self.text_UserInfo_class)
        return FirstNameElement.text
