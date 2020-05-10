"""
Created on May 10, 2020

@author: Mate Ajdukovic
"""

from selenium.webdriver.common.by import By

from page_objects.page import Page


class LoginPage(Page):
    """ Class contains elements from Login page """

    def __init__(self, driver):
        super(LoginPage, self).__init__(driver)

    # Locators
    username_field = (By.ID, 'username')
    password_field = (By.ID, 'password')
    login_button = (By.ID, 'login_button')
    invalid_login_message  = (By.ID, 'invalid_login_message')


    def login_with_credentials(self, username, password):
        """
        Login with credentials
        :param username: string - username that will be used for logging in
        :param password: string - password that will be used for logging in
        :return: None
        """
        el = self.wait_for_element_present(self.username_field)
        el.click()
        el.send_keys(username)
        el = self.wait_for_element_present(self.password_field)
        el.send_keys(password)
        self.click_login_button()

    def get_invalid_login_message(self):
        """
        Get element text
        :return: Invalid login message
        :rtype: string
        """
        el_text = self.get_element_text(self.invalid_login_message)
        return el_text

    def click_login_button(self):
        """
        Click on Login button
        :return: None
        """
        el = self.wait_for_element_present(self.login_button)
        el.click()
