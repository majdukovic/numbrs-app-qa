"""
Created on May 10, 2020

@author: Mate Ajdukovic
"""

from selenium.webdriver.common.by import By

from page_objects.page import Page


class HomePage(Page):
    """ Class contains elements from Home page """

    def __init__(self, driver):
        super(HomePage, self).__init__(driver)

    # Locators
    account_button = (By.ID, 'login')

    def is_displayed_account_button(self):
        """
        Check if Account button is displayed
        :return: True if Account button is displayed, else False
        :rtype: boolean
        """
        el_visible = self.is_element_visible(self.account_button)
        return el_visible
