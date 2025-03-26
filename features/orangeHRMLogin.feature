Feature: OrangeHRM Login Feature
    Scenario: Login to OrangeHRM using valid parameters
        Given I Launch Chrome browser
        When I Open OrangeHRM homepage
        Then Enter username "Admin" and password "admin123"
        And Click on Login button
        Then User must successfully login to Dashboard Page

    Scenario Outline: Login to OrangeHRM using valid parameters
        Given I Launch Chrome browser
        When I Open OrangeHRM homepage
        Then Enter username "<username>" and password "<password>"
        And Click on Login button
        Then User must successfully login to Dashboard Page

    Examples:
        |username|password|
        |Admin   |admin   |
        |Admin   |admin123|
        |Admin   |adm     |
        |Admin   |admin1  |