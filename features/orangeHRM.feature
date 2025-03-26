Feature: OrangeHRM Logo
    Scenario: Logo presence of OrangeHRM in Home Page
        Given Launch Chrome browser
        When Open OrangeHRM homepage
        Then Verify the logo present in Page
        And Close the browser