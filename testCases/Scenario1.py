import time
import pytest
from pageObjects.LoginPage import LoginPage
from pageObjects.Checkout import checkoutProcess
from utilities.readProperties import ReadConfig
from utilities.customLogger import logGen

class TestSuite2:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUserEmail()
    password = ReadConfig.getPassword()
    postalCode = ReadConfig.getPostalCode()
    city = ReadConfig.getCity()
    street = ReadConfig.getStreet()
    number = ReadConfig.getNumber()
    loger = logGen.loggen()

    @pytest.mark.test1
    def test_addingProduct(self, setup):
        self.loger.info("************ Testing AddingProduct to cart TestCase **************")
        self.driver = setup

        #creating objects of POM
        self.lp = LoginPage(self.driver)
        self.co = checkoutProcess(self.driver)

        self.driver.maximize_window()
        self.driver.get(self.baseURL)

        time.sleep(1)
        #adding the item
        self.lp.clickPopupBanner()
        self.co.clickCategory()
        self.co.clickFirstItem()
        self.co.clickAddToCart()

        value = self.co.getCartCount()
        if value != 0:
            self.loger.info("************ AddingProduct to Cart Passed **************")

            self.co.clickCartIcon()
            time.sleep(2)
            self.co.clickContinueToAddress()
            self.lp.setUserName(self.username)
            self.lp.setPassword(self.password)
            self.lp.clickLogin()
            time.sleep(1)
            address_title = self.driver.title
            if address_title == "Address | fashionette":
                self.loger.info("************ Lggin section is Passed **************")
                # setting the address
                self.co.setPostalCode(self.postalCode)
                self.co.setCity(self.city)
                self.co.setStreet(self.street)
                self.co.setNumber(self.number)
                self.co.clickContinueToShip()
                self.co.clickUseThisBilling()
                time.sleep(1)
                shipping_title = self.driver.title
                if shipping_title == "Buy designer handbags and accessories online | fashionette":
                    self.loger.info("************ Adding address is Passed **************")
                    self.co.clickContPaymentOpt()
                    payment_opt_title = self.driver.title
                    if payment_opt_title == "Payment | fashionette":
                        self.loger.info("************ Moved to Payment Option is Passed **************")
                        assert True
                        self.driver.close()
                    else:
                        self.loger.error("************ Moved to Payment Option is Passed **************")
                        self.driver.save_screenshot(".\\Screenshots\\" + "PaymentOption.png")
                        self.driver.close()
                        assert False


                else:
                    self.loger.info("************ Address is Failed **************")
                    self.driver.save_screenshot(".\\Screenshots\\" + "addressSection.png")
                    self.driver.close()
                    assert False

            else:
                self.loger.info("************ Login to Cart Failed **************")
                self.driver.save_screenshot(".\\Screenshots\\" + "Login.png")
                self.driver.close()
                assert False

        else:
            self.loger.info("************ AddingProduct to Cart Failed **************")
            self.driver.save_screenshot(".\\Screenshots\\" + "AddingProduct.png")
            self.driver.close()
            assert False






