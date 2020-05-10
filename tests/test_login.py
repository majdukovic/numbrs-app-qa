# -*- coding: utf-8 -*-
"""
Created on May 10, 2020

@author: Mate Ajdukovic
"""

from nose.tools import assert_true

from base_test import BaseTest
from page_objects.onboarding_page import OnboardingPage
from page_objects.login_page import LoginPage
from page_objects.home_page import HomePage


class TestLogin(BaseTest):
    """
    Test suite deals with testing login feature
    """

    def test_01_login_with_valid_credentials(self):
        """
        Login with existing user and verify account button is displayed user's username is displayed.
        """
        onboarding_page = OnboardingPage(self.driver)
        login_page = LoginPage(self.driver)
        home_page = HomePage(self.driver)

        "Login details"
        username = "valid@username.com"
        password = "ValidPassword"

        "Login with valid username and password"
        onboarding_page.open_login_button()
        login_page.login_with_credentials(username=username, password=password)

        "Verify that account button is displayed"
        account_button_displayed = home_page.is_displayed_account_button()
        assert_true(account_button_displayed, "Account button is not displayed")
        print("User successfully logged in. Account button is displayed.")

    def test_02_login_with_invalid_username_valid_password(self):
        """
        Login with invalid username and valid password.
        Verify user is not logged in and correct message is displayed.
        """
        onboarding_page = OnboardingPage(self.driver)
        login_page = LoginPage(self.driver)

        "Login details"
        username = "fake@username.com"
        password = "ValidPassword"

        "Login with invalid username and valid password"
        onboarding_page.open_login_button()
        login_page.login_with_credentials(username=username, password=password)

        "Verify user is not logged in, message for invalid login is displayed"
        invalid_login_message = login_page.get_invalid_login_message()
        assert_true(invalid_login_message == "Incorrect credentials", "Incorrect credentials message is not displayed.")
        print("Incorrect credentials message is displayed.")

    def test_03_login_with_valid_username_invalid_password(self):
        """
        Login with valid username and invalid password.
        Verify user is not logged in and correct message is displayed.
        """
        onboarding_page = OnboardingPage(self.driver)
        login_page = LoginPage(self.driver)

        "Login details"
        username = "valid@username.com"
        password = "FakePassword"

        "Login with valid username and invalid password"
        onboarding_page.open_login_button()
        login_page.login_with_credentials(username=username, password=password)

        "Verify user is not logged in, message for invalid login is displayed"
        invalid_login_message = login_page.get_invalid_login_message()
        assert_true(invalid_login_message == "Incorrect credentials", "Incorrect credentials message is not displayed.")
        print("Incorrect credentials message is displayed.")


    def test_04_login_with_empty_credentials(self):
        """
        Login with empty credentials.
        Verify user is not logged in and correct message is displayed.
        """
        onboarding_page = OnboardingPage(self.driver)
        login_page = LoginPage(self.driver)

        "Login with empty credentials"
        onboarding_page.open_login_button()
        login_page.click_login_button()

        "Verify user is not logged in, message for invalid login is displayed"
        invalid_login_message = login_page.get_invalid_login_message()
        assert_true(invalid_login_message == "Incorrect credentials", "Incorrect credentials message is not displayed.")
        print("Incorrect credentials message is displayed.")

    def test_05_login_with_valid_username_invalid_password_three_times(self):
        """
        Login with valid username and invalid password for 3 times.
        Verify user is not logged in and correct message is displayed.
        Verify user's account is locked on 3rd try and locked account message is displayed.
        """
        onboarding_page = OnboardingPage(self.driver)
        login_page = LoginPage(self.driver)

        "Login details"
        username = "valid@username.com"
        password = "FakePassword"

        "Login with valid username and invalid password"
        onboarding_page.open_login_button()
        login_page.login_with_credentials(username=username, password=password)

        "Verify user is not logged in, message for invalid login is displayed"
        invalid_login_message = login_page.get_invalid_login_message()
        assert_true(invalid_login_message == "Incorrect credentials", "Incorrect credentials message is not displayed.")
        print("Incorrect credentials message is displayed.")

        "Login with valid username and invalid password"
        onboarding_page.open_login_button()
        login_page.login_with_credentials(username=username, password=password)

        "Verify user is not logged in, message for invalid login is displayed"
        invalid_login_message = login_page.get_invalid_login_message()
        assert_true(invalid_login_message == "Incorrect credentials", "Incorrect credentials message is not displayed.")
        print("Incorrect credentials message is displayed.")

        "Login with valid username and invalid password"
        onboarding_page.open_login_button()
        login_page.login_with_credentials(username=username, password=password)

        "Verify user is not logged in, message for locked account is displayed"
        locked_account_message = login_page.get_invalid_login_message()
        assert_true(locked_account_message == "Account is locked due to 3 unsussuccessful ", "Account locked message is not displayed.")
        print("Account locked message is displayed.")

    def test_06_sql_injection_login(self):
        """
        Try to login with invalid details using SQL injection.
        Verify user is not logged in and correct message is displayed.
        """
        onboarding_page = OnboardingPage(self.driver)
        login_page = LoginPage(self.driver)

        "Login details"
        username = "'OR' '='"
        password = "'OR' '='"

        "Login with invalid credentials"
        onboarding_page.open_login_button()
        login_page.login_with_credentials(username=username, password=password)

        "Verify user is not logged in, message for invalid login is displayed"
        invalid_login_message = login_page.get_invalid_login_message()
        assert_true(invalid_login_message == "Incorrect credentials", "Incorrect credentials message is not displayed.")
        print("Incorrect credentials message is displayed.")
