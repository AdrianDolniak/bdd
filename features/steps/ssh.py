from behave import *
import paramiko
from hamcrest import *


@given(u'the connection is set with remote host')
def step_impl(context):
    context = paramiko.SSHClient()
    context.load_system_host_keys()
    context.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    context.connect("localhost", port=22, username="adi", password="adi!")
    stdin, stdout, stderr = context.exec_command("hostname")
    output = stdout.read()
    print (output)
    assert_that(output, contains_string("adi-vmware"))


@when(u'we check if there is a connection')
def step_impl(context):
    raise NotImplementedError(u'STEP: When we check if there is a connection')


@when(u'we check if remote machine has 4 cores')
def step_impl(context):
    raise NotImplementedError(u'STEP: When we check if remote machine has 4 cores')


@when(u'we execute command "ping -c1 8.8.8.8"')
def step_impl(context):
    raise NotImplementedError(u'STEP: When we execute command "ping -c1 8.8.8.8"')


@then(u'the response contain phrase "adi-vmware"')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then the response contain phrase "adi-vmware"')


@then(u'the response is "4"')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then the response is "4"')


@then(u'the response contain phrase "1 received"')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then the response contain phrase "1 received"')
