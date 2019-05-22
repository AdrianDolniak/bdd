from selenium import webdriver
import paramiko


def before_all(context):
    # -- SET LOG LEVEL: behave --logging-level=ERROR ...
    # on behave command-line or in "behave.ini".
    context.config.setup_logging()


def before_tag(context, tag):
    if tag == "web":
        # choose the browser
        context.driver = webdriver.Firefox()
        # context.driver = webdriver.Chrome()
        context.driver.implicitly_wait(10)
        context.driver.maximize_window()
    else:
        context.ssh = paramiko.SSHClient()
        context.ssh.load_system_host_keys()
        context.ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        context.ssh.connect("localhost", port=22, username="adi",
                            password="adi!", allow_agent=False,
                            look_for_keys=False)


def after_tag(context, tag):
    if tag == "web":
        context.driver.quit()
    else:
        context.ssh.close()
