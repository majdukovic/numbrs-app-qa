# -*- coding: utf-8 -*-
"""
Created on May 10, 2020

@author: Mate Ajdukovic
"""

from selenium import webdriver


class BaseTest:
    """
    This class deals with starting Selenium session with Chrome browser and setting Numbrs app to the initial state
    All test classes extend this class
    """

    def setup(self):
        """
        Create driver instance with desired capabilities which will be used through tests suite
        """
        url = "https://www.numbrs.com/en-uk/"

        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get(url=url)

    def teardown(self):
        """
        Quit driver session and close app
        """
        self.driver.quit()
