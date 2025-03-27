Feature: OrangeHRM Search

Background: Common Steps
    Given I launch browser
    When I launch Application
    And enter valid username and password
    And click on login

Scenario: Login to HRM Application
    Then User must login to the Dashboard Page

Scenario: Search user page
    When I navigate to Search Page
    Then Search page should be displayed

Scenario: Advanced user Search
    When navigate to advanced Search page
    Then advanced search page should be displayed



