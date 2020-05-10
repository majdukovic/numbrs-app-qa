"""
Created on May 10, 2020

@author: Mate Ajdukovic
"""

from selenium.webdriver.common.by import By

from page_objects.page import Page


class OnboardingPage(Page):
    """ Class contains elements from Onboarding page """

    def __init__(self, driver):
        super(OnboardingPage, self).__init__(driver)

    # Locators
    login_button = (By.ID, 'login_button')


    def open_login_button(self):
        """
        Click on Login button
        :return: None
        """
        el = self.wait_for_element_present(self.login_button)
        el.click()
