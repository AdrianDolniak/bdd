from selenium import webdriver


def before_tag(context, web):
    context.driver = webdriver.Firefox()
    context.driver.implicitly_wait(10)
    context.driver.maximize_window()


def after_tag(context, web):
    context.driver.quit()