from locator import *
from element import BasePageElement


class SearchUsername(BasePageElement):
    locator = "username"


class SearchPassword(BasePageElement):
    locator = "password"


class SearchPassword1(BasePageElement):
    locator = "password1"


class SearchPassword2(BasePageElement):
    locator = "password2"


class SearchName(BasePageElement):
    locator = "first_name"


class SearchLastName(BasePageElement):
    locator = "last_name"


class SearchMail(BasePageElement):
    locator = "email"


class SearchTitle(BasePageElement):
    locator = "title"


class SearchDescription(BasePageElement):
    locator = "description"


class SearchImage(BasePageElement):
    locator = "image"


class SearchContent(BasePageElement):
    locator = "content"


class BasePage(object):
    def __init__(self, driver):
        self.driver = driver


class MainPage(BasePage):

    def is_title(self):
        return "HomePage" in self.driver.title

    def click_add_photo(self):
        element = self.driver.find_element(*MainPageLocator.ADD_PHOTO)
        element.click()

    def click_first_image(self):
        element = self.driver.find_element(*MainPageLocator.IMAGE)
        element.click()

class LoginPage(BasePage):

    search_username = SearchUsername()
    search_password = SearchPassword()

    def is_login(self):
        return 'Profile' in self.driver.page_source

    def click_login(self):
        element = self.driver.find_element(*LoginPageLocator.SUBMIT_BUTTON)
        element.click()

    def click_register(self):
        element = self.driver.find_element(*LoginPageLocator.REGISTER_LINK)
        element.click()


class RegisterPage(BasePage):

    search_username = SearchUsername()
    search_name = SearchName()
    search_lname = SearchLastName()
    search_mail = SearchMail()
    search_password = SearchPassword1()
    search_password1 = SearchPassword2()

    def click_submit(self):
        element = self.driver.find_element(*RegisterPageLocator.SUBMIT_BUTTON)
        element.click()

    def is_registered(self):
        return 'LoginPage' in self.driver.title


class AddPhotoPage(BasePage):
    search_title = SearchTitle()
    search_description = SearchDescription()
    search_image = SearchImage()

    def click_submit(self):
        element = self.driver.find_element(*RegisterPageLocator.SUBMIT_BUTTON)
        element.click()


class AddCommentPage(BasePage):
    search_content = SearchContent()

    def click_submit(self):
        element = self.driver.find_element(*AddCommentPageLocator.SUBMIT_BUTTON)
        element.click()

    def find_test_comment(self):
        return "test_comment" in self.driver.page_source
