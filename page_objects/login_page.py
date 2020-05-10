"""
Created on May 10, 2020

@author: Mate Ajdukovic
"""

from appium.webdriver.common.mobileby import MobileBy

from page_objects.page import Page


class LoginPage(Page):
    """ Class contains elements from Login page """

    def __init__(self, driver):
        super(LoginPage, self).__init__(driver)
        self.os = str(self.driver.desired_capabilities['platformName']).lower()

    # Android
    username_field_android = (MobileBy.ID, 'com.centralway.numbrs:id/login_field')
    password_field_android = (MobileBy.ID, 'com.centralway.numbrs:id/password_field')
    login_button_android = (MobileBy.ID, 'com.centralway.numbrs:id/login_button')
    invalid_login_message_android  = (MobileBy.ID, 'com.centralway.numbrs:id/invalid_login_message')

    # iOS
    username_field_ios = (MobileBy.ACCESSIBILITY_ID, 'Email address')
    password_field_ios = (MobileBy.ACCESSIBILITY_ID, 'Password')
    login_button_ios = (MobileBy.ACCESSIBILITY_ID, 'LOG IN')
    invalid_login_message_ios = (MobileBy.ACCESSIBILITY_ID, 'Ivalid login')

    def login_with_credentials(self, username, password):
        """
        Login with credentials
        :param username: string - username that will be used for logging in
        :param password: string - password that will be used for logging in
        :return: None
        """
        el = self.wait_for_element_present(*getattr(self, 'username_field_' + self.os))
        el.click()
        el.send_keys(username)
        el = self.wait_for_element_present(*getattr(self, 'password_field_' + self.os))
        el.send_keys(password)
        self.click_login_button()

    def get_invalid_login_message(self):
        """
        Get element text
        :return: Invalid login message
        :rtype: string
        """
        el_text = self.get_element_text(*getattr(self, 'invalid_login_message_' + self.os))
        return el_text

    def click_login_button(self):
        """
        Click on Login button
        :return: None
        """
        el = self.wait_for_element_present(*getattr(self, 'login_button_' + self.os))
        el.click()
