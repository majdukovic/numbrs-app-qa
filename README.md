# numbrs-app-qa


This repository contains login test cases for __Android__, __iOS__ and __Web__ platform.

On **master** branch test cases are for Android/iOS platform using Appium framework, Python and nosetests as test runner.

On **selenium-tests** branch, test cases are for Web platform using Selenium framework and Python and nosetests as test runner.

__Page Object Model__ design pattern is used in this project, meaning each page that exists in the application has it's own class which contains locators for each element on the page and actions we can do on these elements (e.g. click element, get element text, check if element is displayed, etc.). 
