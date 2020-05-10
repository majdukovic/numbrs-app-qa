# -*- coding: utf-8 -*-
"""
Created on May 10, 2020

@author: Mate Ajdukovic
"""
from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException, TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class Page:
    """
    This class contains methods for checking if element is displayed, getting element text, etc.
    All page classes extend this class
    """
    def __init__(self, driver):
        """
        Constructor
        """
        self.driver = driver

    def wait_for_element_present(self, locator, wait_time=10):
        """
        Wait for element to be displayed
        :param locator: Locator of the element that needs to be found
        :param wait_time: Time to wait for the element. 10 seconds by default
        :return: Element, if element is found
        :rtype: object
        """
        ignored_exceptions = (NoSuchElementException, StaleElementReferenceException)
        wait = WebDriverWait(driver=self.driver, timeout=wait_time, ignored_exceptions=ignored_exceptions)
        el = wait.until(EC.presence_of_element_located(locator), message=":".join(locator) + " element not visible")
        return el

    def is_element_visible(self, locator, wait_time=10):
        """
        Wait for element to be visible
        :param locator: Locator of the element that needs to be found
        :param wait_time: Time to wait for the element. 10 seconds by default
        :return: Element, if element is found
        :rtype: object
        """
        try:
            wait = WebDriverWait(driver=self.driver, timeout=wait_time)
            wait.until(EC.visibility_of_element_located(locator), message=":".join(locator) + " element not visible")
            return True
        except TimeoutException:
            return False

    def get_element_text(self, locator, wait_time=15):
        """
        Get element text
        :param locator: Locator of the element that needs to be found
        :param wait_time: Time to wait for the element. 15 seconds by default
        :return: Element text, if element is found
        :rtype: string
        """
        os = str(self.driver.desired_capabilities['platformName']).lower()
        if os == 'android':
            wait = WebDriverWait(self.driver, wait_time)
            el = wait.until(EC.visibility_of_element_located(locator), message=":".join(locator) + " element not visible")
            return el.get_attribute('text')
        else:
            wait = WebDriverWait(self.driver, wait_time)
            el = wait.until(EC.visibility_of_element_located(locator), message=":".join(locator) + " element not visible")
            return el.get_attribute('name')
