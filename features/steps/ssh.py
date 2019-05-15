from behave import *
import paramiko

# Givens

@given(u'the connection is set with remote host')
def step_impl(context):
    context = paramiko.SSHClient()
    context.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    context.connect("127.0.0.1", port=22, username="adi", password="adi!")


# Whens

@when(u'we execute command "uname -a"')
def step_impl(context):
    raise NotImplementedError(u'STEP: When we execute command "uname -a"')


@when(u'we execute command "nproc"')
def step_impl(context):
    raise NotImplementedError(u'STEP: When we execute command "nproc"')


@when(u'we execute command "hostname"')
def step_impl(context):
    raise NotImplementedError(u'STEP: When we execute command "hostname"')


@when(u'we execute command "ping -c1 8.8.8.8"')
def step_impl(context):
    raise NotImplementedError(u'STEP: When we execute command "ping -c1 8.8.8.8"')


# Thens

@then(u'the response contain phrase "adi-vmware"')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then the response contain phrase "adi-vmware"')


@then(u'the response is "4"')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then the response is "4"')


@then(u'the response contain phrase "1 received"')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then the response contain phrase "1 received"')

