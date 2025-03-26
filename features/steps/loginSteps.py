from selenium import webdriver
from selenium.webdriver.common.by import By
from behave import *

@given(u'I Launch Chrome browser')
def openChrome(context):
    context.driver = webdriver.Chrome()


@when(u'I Open OrangeHRM homepage')
def goToURL(context):
    context.driver.get('https://opensource-demo.orangehrmlive.com/web/index.php/auth/login')

@then(u'Enter username "{user}" and password "{password}"')
def enterCredentials(context, user, password):
    context.driver.implicitly_wait(10)
    context.driver.find_element(By.CSS_SELECTOR, 'input[name="username"]').send_keys(user)
    context.driver.find_element(By.CSS_SELECTOR, 'input[name="password"]').send_keys(password)


@then(u'Click on Login button')
def loginButton(context):
    context.driver.implicitly_wait(10)
    context.driver.find_element(By.CSS_SELECTOR, 'button').click()


@then(u'User must successfully login to Dashboard Page')
def dashboardVerify(context):
    try:
        status = context.driver.find_element(By.CSS_SELECTOR, 'span > h6').is_displayed()
    except:
        context.driver.quit()
        assert False, 'Test failed!'
    assert status is True, 'Test, passed!'
    context.driver.quit()