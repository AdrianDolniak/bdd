from behave import *
from hamcrest import *

# givens
@given(u'we open the terminal')
def step_impl(context):
    pass

# whens
@when(u'we check the connection with remote host')
def step_impl(context):
    stdin, stdout, stderr = context.ssh.exec_command("uname -a")
    context.output = stdout.read()


@when(u'we check if the remote machine has 4 cores processor')
def step_impl(context):
    stdin, stdout, stderr = context.ssh.exec_command("nproc")
    context.output = stdout.read()


@when(u'we check if the remote machine has internet connection')
def step_impl(context):
    stdin, stdout, stderr = context.ssh.exec_command("ping -c1 8.8.8.8")
    context.output = stdout.read()

# thens
@then(u'the response should contain a phrase "adi-vmware"')
def step_impl(context):
    assert_that(context.output, contains_string("adi-vmware"))


@then(u'the response should be "4"')
def step_impl(context):
    assert_that(context.output, contains_string("4"))


@then(u'the response should contain phrase "1 received"')
def step_impl(context):
    assert_that(context.output, contains_string("1 received"))