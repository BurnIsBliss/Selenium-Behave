Feature: OrangeHRM Login Feature
    Scenario: Login to OrangeHRM using valid parameters
        Given I Launch Chrome browser
        When I Open OrangeHRM homepage
        Then Enter username "Admin" and password "admin123"
        And Click on Login button
        Then User must successfully login to Dashboard Page
