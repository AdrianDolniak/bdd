from behave import *

# Givens

@given(u'the user is logged on the e-mail account')
def step_impl(context):
    raise NotImplementedError(u'STEP: Given the user is logged on the e-mail account')

@given(u'the logging page is displayed')
def step_impl(context):
    raise NotImplementedError(u'STEP: Given the logging page is displayed')


# Whens

@when(u'the user looks for a word "Odebrane" on the page')
def step_impl(context):
    raise NotImplementedError(u'STEP: When the user looks for a word "Odebrane" on the page')

@when(u'the user enter valid username and wrong password')
def step_impl(context):
    raise NotImplementedError(u'STEP: When the user enter valid username and wrong password')


# Thens

@then(u'the user sees a word "Odebrane on the page')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then the user sees a word "Odebrane on the page')

@then(u'the warning is shown "Wrong username or password"')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then the warning is shown "Wrong username or password"')
