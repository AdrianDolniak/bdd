from selenium import webdriver
import paramiko


def before_tag(context, web):
    context.driver = webdriver.Firefox()
    context.driver.implicitly_wait(10)
    context.driver.maximize_window()


def after_tag(context, web):
    context.driver.quit()


def before_tag(context, ssh):
    context.ssh = paramiko.SSHClient()
    context.ssh.load_system_host_keys()
    context.ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    context.ssh.connect("localhost", port=22, username="adi", password="adi!", allow_agent=False, look_for_keys=False)


def after_tag(context, ssh):
    context.ssh.close()