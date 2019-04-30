from behave import *

password = 'asd123'

@given(u'user is on Poczta Onet website')
def step_impl(context):
    def step_start_page(context):
        context.driver.get('http://poczta.onet.pl/')


@when(u'user fills in the Sign In form and submits it')
def step_impl(context):
    def step_set_login_in(context):
        context.driver.find_element_by_id('f_login').send_keys('behavetest@onet.pl')
        context.driver.find_element_by_id('f_password').send_keys(password)
        context.driver.find_element_by_css_selector('input.loginButton').click()

@then(u'User can see email list')
def step_impl(context):
    def step_valid_login(context):
        context.driver.save_screenshot("screenshot-login.png")
        assert context.driver.find_element_by_id('mailList-list-items')