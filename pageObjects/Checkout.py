from selenium import webdriver
from selenium.webdriver.common.by import By

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class checkoutProcess:
    button_handBagCat_xpath = "/html/body/div[3]/div[2]/div[1]/div[3]/div[1]/a"
    button_firstItem_xpath = "/html/body/div[3]/div[2]/div/div[2]/div[1]/div[2]/div[4]/div[1]/div/a/div"
    button_addToCart_xpath = "/html/body/div[3]/div[2]/div/article/div[2]/div[2]/div[3]/form/div[1]/div/div"
    button_cartCount_class = "cart-amount"
    button_cartIcon_class = "header__cart-icon"
    button_ContinueToAddress_ID = "checkout-start"
    textbox_postalCode_name = "billingZipcode"
    textbox_CityName_name = "billingCity"
    textbox_Street_name = "billingStreet"
    textbox_number_name = "billingHnr"
    button_continueToShipping_class = "btn__submit"
    button_UseBillingAddress_xpath = "//*[@id='modal-address-doctor']/div/div/div/div/div/div[1]/div[2]/div[3]/div/div"
    button_contPaymentOpt_class = "btn__submit"

    button_redeemVoc_xpath = "/html/body/div[1]/div[2]/div[1]/div[1]/div/div[2]/div/table/tbody/tr[3]/td"
    textbox_voucherfield_name = "voucherCode"
    button_applyRedeem_xpath = "//*[@id='form-cart-voucher']/div[2]/button"
    text_voucherPrice_xpath = "/html/body/div[1]/div[2]/div[1]/div[1]/div/div[2]/div/table/tbody/tr[3]/td/span"


    def __init__(self, setup):
        self.driver = setup

    def clickCategory(self):
        self.driver.find_element(By.XPATH, self.button_handBagCat_xpath).click()

    def clickFirstItem(self):
        self.driver.find_element(By.XPATH, self.button_firstItem_xpath).click()

    def clickAddToCart(self):
        self.driver.find_element(By.XPATH, self.button_addToCart_xpath).click()

    def clickCartIcon(self):
        self.driver.find_element(By.CLASS_NAME, self.button_cartIcon_class).click()

    def clickContinueToAddress(self):
        self.driver.find_element(By.ID, self.button_ContinueToAddress_ID).click()

    def getCartCount(self):
        value = self.driver.find_element(By.CLASS_NAME, self.button_cartCount_class)
        return value.text

    def setPostalCode(self, postalCode):
        self.driver.find_element(By.NAME, self.textbox_postalCode_name).clear()
        self.driver.find_element(By.NAME, self.textbox_postalCode_name).send_keys(postalCode)

    def setCity(self, city):
        self.driver.find_element(By.NAME, self.textbox_CityName_name).clear()
        self.driver.find_element(By.NAME, self.textbox_CityName_name).send_keys(city)

    def setStreet(self, street):
        self.driver.find_element(By.NAME, self.textbox_Street_name).clear()
        self.driver.find_element(By.NAME, self.textbox_Street_name).send_keys(street)

    def setNumber(self, number):
        self.driver.find_element(By.NAME, self.textbox_number_name).clear()
        self.driver.find_element(By.NAME, self.textbox_number_name).send_keys(number)

    def clickContinueToShip(self):
        self.driver.find_element(By.CLASS_NAME, self.button_continueToShipping_class).click()

    def clickUseThisBilling(self):
        element = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, self.button_UseBillingAddress_xpath)))
        element.click()

    def clickContPaymentOpt(self):
        self.driver.find_element(By.CLASS_NAME, self.button_contPaymentOpt_class).click()

    def clickRedeemVoc(self):
        self.driver.find_element(By.XPATH, self.button_redeemVoc_xpath).click()

    def setVoucher(self, voucher):
        element = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.NAME, self.textbox_voucherfield_name)))
        element.send_keys(voucher)
        # self.driver.find_element(By.NAME, self.textbox_voucherfield_name).clear()
        # self.driver.find_element(By.NAME, self.textbox_voucherfield_name).send_keys(voucher)

    def clickApplyRedeem(self):
        self.driver.find_element(By.XPATH, self.button_applyRedeem_xpath).click()

    def getVoucherPrice(self):
        element = self.driver.find_element(By.XPATH, self.text_voucherPrice_xpath)
        return element.text
        #text format = -£0