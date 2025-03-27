# Functions are not properly implemented, this is just an example

from behave import *

@given(u'I launch browser')
def step_impl(context):
    assert True, 'Test passed!'

@when(u'I launch Application')
def step_impl(context):
    assert True, 'Test passed!'


@when(u'enter valid username and password')
def step_impl(context):
    assert True, 'Test passed!'


@when(u'click on login')
def step_impl(context):
    assert True, 'Test passed!'


@then(u'User must login to the Dashboard Page')
def step_impl(context):
    assert True, 'Test passed!'


@when(u'I navigate to Search Page')
def step_impl(context):
    assert True, 'Test passed!'


@then(u'Search page should be displayed')
def step_impl(context):
    assert True, 'Test passed!'


@when(u'navigate to advanced Search page')
def step_impl(context):
    assert True, 'Test passed!'


@then(u'advanced search page should be displayed')
def step_impl(context):
    assert True, 'Test passed!'
