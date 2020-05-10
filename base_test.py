# -*- coding: utf-8 -*-
"""
Created on May 10, 2020

@author: Mate Ajdukovic
"""

from appium import webdriver


class BaseTest:
    """
    This class deals with starting Appium session and setting Numbrs app to the initial state
    All test classes extend this class
    """
    desired_caps = {
          "platformName": "Android",
          "platformVersion": "9.0",
          "automationName": "uiautomator2",
          "deviceName": "Android Emulator",
          "avd": "Pixel_2_API_28",
          "appPackage": "com.centralway.numbrs",
          "appActivity": ".launcher.activities.LauncherActivity"
    }

    def setup(self):
        """
        Create driver instance with desired capabilities which will be used through tests suite
        """
        self.driver = webdriver.Remote(command_executor='http://127.0.0.1:4723/wd/hub',
                                       desired_capabilities=self.desired_caps)

    def teardown(self):
        """
        Quit driver session and close app
        """
        self.driver.quit()
