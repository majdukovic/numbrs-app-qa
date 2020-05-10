"""
Created on May 10, 2020

@author: Mate Ajdukovic
"""

from appium.webdriver.common.mobileby import MobileBy

from page_objects.page import Page


class HomePage(Page):
    """ Class contains elements from Home page """

    def __init__(self, driver):
        super(HomePage, self).__init__(driver)
        self.os = str(self.driver.desired_capabilities['platformName']).lower()

    # Android
    account_button_android = (MobileBy.ID, 'com.centralway.numbrs:id/account_button')

    # iOS
    account_button_ios = (MobileBy.ACCESSIBILITY_ID, 'Account')

    def is_displayed_account_button(self):
        """
        Check if Account button is displayed
        :return: True if Account button is displayed, else False
        :rtype: boolean
        """
        el_visible = self.is_element_visible(*getattr(self, 'account_button_' + self.os))
        return el_visible
