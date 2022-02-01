from selenium.webdriver.common.by import By


class MainPageLocator(object):
    ADD_PHOTO = (By.NAME, 'addPhoto')
    IMAGE = (By.CLASS_NAME, 'image_selenium')


class LoginPageLocator(object):
    SUBMIT_BUTTON = (By.NAME, 'submit_button')
    REGISTER_LINK = (By.NAME, 'register')


class RegisterPageLocator(object):
    SUBMIT_BUTTON = (By.NAME, 'submit_button')


class AddPhotoPageLocator(object):
    SUBMIT_BUTTON = (By.NAME, 'submit_button')
    ADD_PHOTO_BUTTON = (By.NAME, 'addPhoto')


class AddCommentPageLocator(object):
    SUBMIT_BUTTON = (By.NAME, 'submit_button')