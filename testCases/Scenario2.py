import time
from pageObjects.LoginPage import LoginPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import logGen

class TestSuite1:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUserEmail()
    password = ReadConfig.getPassword()
    firstName = ReadConfig.getfirstName()
    lastName = ReadConfig.getlastName()
    loger = logGen.loggen()


    def test_homePageTitle(self, setup):
        self.loger.info("***************** test_homePageTitle Test Case running *********************")
        self.driver = setup
        self.driver.maximize_window()
        self.driver.get(self.baseURL)
        actual_title = self.driver.title

        if actual_title == "fashionette | Buy designer handbags, shoes & accessories online":
            self.loger.info("***************** test_homePageTitle Test Case is Passed *********************")
            self.driver.close()
            assert True

        else:
            self.loger.info("***************** test_homePageTitle Test Case is Failed *********************")
            self.driver.save_screenshot(".\\Screenshots\\" + "test_homePageTitle.png")
            self.driver.close()
            assert False



    def test_login(self, setup):
        self.loger.info("************ Verifying Login Test **************")
        self.driver = setup
        self.driver.maximize_window()
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        self.driver.implicitly_wait(10)

        # creating the loginPage object
        self.lp = LoginPage(self.driver)

        # navigating to user page
        self.lp.clickPopupBanner()
        self.lp.clickLoginPage()

        # addling the login credentials
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        act_title = self.driver.title

        if act_title == "Buy designer handbags and accessories online | fashionette":
            self.loger.info("************ Login Test is Passed **************")

            self.loger.info("************ UserName Testing **************")


            #Changing the user name
            self.lp.clickPersonalData()
            self.lp.clickEditData()
            self.driver.implicitly_wait(20)
            self.lp.setFirstName(self.firstName)
            self.lp.setLastName(self.lastName)
            self.lp.clickUserInfoSave()

            time.sleep(1)
            self.driver.refresh()
            actualInfo = self.lp.getUserInfo()

        #verfying the changed
            if self.firstName == actualInfo:
                self.loger.info("************ UserName Test is Passed **************")
                self.driver.close()
                assert True
            else:
                self.loger.info("************ UserName Test is Failed **************")
                self.driver.save_screenshot(".\\Screenshots\\" + "username.png")
                assert False
                self.driver.close()

        else:
            self.loger.info("************ Login Test is Failed **************")
            self.driver.save_screenshot(".\\Screenshots\\" + "LoginTest.png")
            assert False
            self.driver.close()
