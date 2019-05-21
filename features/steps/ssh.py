from behave import *
import paramiko
from hamcrest import *

# givens
@given(u'we open the terminal')
def step_impl(context):
    pass

# whens
@when(u'we check the connection with remote host')
def step_impl(context):
    ssh = paramiko.SSHClient()
    ssh.load_system_host_keys()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect("localhost", port=22, username="adi", password="adi!", allow_agent=False, look_for_keys=False)
    stdin, stdout, stderr = ssh.exec_command("uname -a")
    context.output = stdout.read()


@when(u'we check if the remote machine has 4 cores processor')
def step_impl(context):
    ssh = paramiko.SSHClient()
    ssh.load_system_host_keys()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect("localhost", port=22, username="adi", password="adi!", allow_agent=False, look_for_keys=False)
    stdin, stdout, stderr = ssh.exec_command("nproc")
    context.output = stdout.read()


@when(u'we check if the remote machine has internet connection')
def step_impl(context):
    ssh = paramiko.SSHClient()
    ssh.load_system_host_keys()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect("localhost", port=22, username="adi", password="adi!", allow_agent=False, look_for_keys=False)
    stdin, stdout, stderr = ssh.exec_command("ping -c1 8.8.8.8")
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