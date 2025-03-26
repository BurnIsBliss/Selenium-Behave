from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

@given(u'Launch Chrome browser')
def launchBrowser(context):
    context.driver = webdriver.Chrome()

@when(u'Open OrangeHRM homepage')
def openHomePage(context):
    context.driver.get('https://opensource-demo.orangehrmlive.com/')
    time.sleep(10)

@then(u'Verify the logo present in Page')
def verifyLogo(context):
    status = context.driver.find_element(By.CSS_SELECTOR, 'img[alt="company-branding"]').is_displayed()
    assert status is True

@then(u'Close the browser')
def closeBrowser(context):
    context.driver.quit()