import time
import unittest
from selenium import webdriver
import page


class LoginTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(r"E:\operadriver\chromedriver.exe")
        self.driver.get('http://127.0.0.1:8000/')

    def test_1login(self):
        login = page.LoginPage(self.driver)
        time.sleep(3)
        login.search_username = "admin"
        login.search_password = "haslo"
        time.sleep(3)
        login.click_login()
        time.sleep(3)
        assert login.is_login()

    def test_2register(self):
        login = page.LoginPage(self.driver)
        login.click_register()
        time.sleep(3)
        register = page.RegisterPage(self.driver)
        time.sleep(3)
        register.search_username = "test_username"
        register.search_name = "test_name"
        register.search_lname = "test_lname"
        register.search_mail = "test_mail@gmail.com"
        register.search_password = "tset_password"
        register.search_password1 = "tset_password"
        time.sleep(3)
        register.click_submit()
        time.sleep(3)
        assert register.is_registered()

    def test_3add_photo(self):
        login = page.LoginPage(self.driver)
        time.sleep(3)
        login.search_username = "admin"
        login.search_password = "haslo"
        time.sleep(3)
        login.click_login()
        time.sleep(3)
        main = page.MainPage(self.driver)
        main.click_add_photo()
        time.sleep(3)
        add_photo = page.AddPhotoPage(self.driver)
        add_photo.search_title = "test_title"
        add_photo.search_description = "test_description"
        add_photo.search_image = r"C:\Users\thein\Desktop\test.jpg"
        time.sleep(3)
        add_photo.click_submit()
        assert main.is_title()

    def test_4add_comment(self):
        login = page.LoginPage(self.driver)
        time.sleep(3)
        login.search_username = "admin"
        login.search_password = "haslo"
        time.sleep(3)
        login.click_login()
        time.sleep(3)
        main = page.MainPage(self.driver)
        main.click_first_image()
        time.sleep(3)
        comment = page.AddCommentPage(self.driver)
        comment.search_content = "test_comment"
        comment.click_submit()
        time.sleep(3)
        assert comment.find_test_comment()

    def tearDown(self):
        self.driver.close()


if __name__ == '__main__':
    unittest.main()
