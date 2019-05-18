# -*- coding: utf-8 -*-
from behave import *
from hamcrest import *

# Givens
@given(u'the user is on the home page of the portal wp.pl')
def step_impl(context):
    context.driver.get('https://www.wp.pl/')


@given(u'the logging page to the e-mail account is displayed')
def step_impl(context):
    context.driver.get('https://profil.wp.pl/login.html?zaloguj=poczta')


# Whens
@when(u'the user login to the e-mail account')
def step_impl(context):
    context.driver.get('https://profil.wp.pl/login.html?zaloguj=poczta')
    context.driver.find_element_by_xpath('//*[@id="login"]').send_keys('testerwsb_t1')
    context.driver.find_element_by_xpath('//*[@id="password"]').send_keys('adam1234')
    context.driver.find_element_by_xpath('//*[@id="btnSubmit"]').click()


@when(u'the user enter valid username and wrong password')
def step_impl(context):
    context.driver.find_element_by_xpath('//*[@id="login"]').send_keys('testerwsb_t1')
    context.driver.find_element_by_xpath('//*[@id="password"]').send_keys('adam1235')
    context.driver.find_element_by_xpath('//*[@id="btnSubmit"]').click()


# Thens
@then(u'the user will see a word "Odebrane on the page')
def step_impl(context):
    odebrane = context.driver.find_element_by_xpath('//*[@id="folder-1"]/div[2]')
    assert_that(odebrane, 'Odebrane')


@then(u'the warning is shown "Wrong username or password"')
def step_impl(context):
    title = context.driver.find_element_by_xpath('//*[@id="login-error-message"]/h1')
    assert_that(title.text, contains_string(u'Niestety podany login lub hasło jest błędne.'))

