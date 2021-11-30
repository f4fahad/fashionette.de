import time
import pytest
from pageObjects.LoginPage import LoginPage
from pageObjects.Checkout import checkoutProcess
from utilities.readProperties import ReadConfig
from utilities.customLogger import logGen

class TestSuite2:
    baseURL = ReadConfig.getApplicationURL()
    voucher = ReadConfig.getVoucher()
    loger = logGen.loggen()

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
            self.co.clickRedeemVoc()
            self.co.setVoucher(self.voucher)
            self.co.clickApplyRedeem()
            time.sleep(2)
            verifyVoucher = self.co.getVoucherPrice()

            if verifyVoucher != "-£0":
                self.loger.info("************ Voucher is successfully applied **************")
                assert True
                self.driver.close()
            else:
                self.loger.info("************ Voucher is not applied **************")
                self.driver.save_screenshot(".\\Screenshots\\" + "voucher.png")
                assert False
                self.driver.close()

        else:
            self.loger.info("************ AddingProduct to Cart Failed **************")
            self.driver.save_screenshot(".\\Screenshots\\" + "AddingProduct.png")
            assert False
            self.driver.close()