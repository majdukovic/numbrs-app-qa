"""
Created on May 10, 2020

@author: Mate Ajdukovic
"""

from appium.webdriver.common.mobileby import MobileBy

from page_objects.page import Page


class OnboardingPage(Page):
    """ Class contains elements from Onboarding page """

    def __init__(self, driver):
        super(OnboardingPage, self).__init__(driver)
        self.os = str(self.driver.desired_capabilities['platformName']).lower()

    # Android
    login_button_android = (MobileBy.ID, 'com.centralway.numbrs:id/login_button')

    # iOS
    login_button_ios = (MobileBy.ACCESSIBILITY_ID, 'LOG IN')

    def open_login_button(self):
        """
        Click on Login button
        :return: None
        """
        el = self.wait_for_element_present(*getattr(self, 'login_button_' + self.os))
        el.click()
