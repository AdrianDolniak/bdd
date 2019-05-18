from behave import *
import paramiko
from hamcrest import *

# givens
@given(u'the connection is set with remote host')
def step_impl(context):
    pass


# whens
@when(u'we check if there is a connection with remote host')
def step_impl(context):
    pass


@when(u'we check if remote machine has 4 cores')
def step_impl(context):
    pass


@when(u'we check if remote machine has internet connection')
def step_impl(context):
    pass

# thens
@then(u'the response contain phrase "adi-vmware"')
def step_impl(context):
    ssh = paramiko.SSHClient()
    ssh.load_system_host_keys()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect("localhost", port=22, username="adi", password="adi!", allow_agent=False, look_for_keys=False)
    stdin, stdout, stderr = ssh.exec_command("uname -a")
    output = stdout.read()
    print (output)
    assert_that(output, contains_string("adi-vmware"))

@then(u'the response is "4"')
def step_impl(context):
    ssh = paramiko.SSHClient()
    ssh.load_system_host_keys()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect("localhost", port=22, username="adi", password="adi!", allow_agent=False, look_for_keys=False)
    stdin, stdout, stderr = ssh.exec_command("nproc")
    output = stdout.read()
    print (output)
    assert_that(output, contains_string("4"))

@then(u'the response contain phrase "1 received"')
def step_impl(context):
    ssh = paramiko.SSHClient()
    ssh.load_system_host_keys()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect("localhost", port=22, username="adi", password="adi!", allow_agent=False, look_for_keys=False)
    stdin, stdout, stderr = ssh.exec_command("ping -c1 8.8.8.8")
    output = stdout.read()
    print (output)
    assert_that(output, contains_string("1 received"))