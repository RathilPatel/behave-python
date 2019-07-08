import time
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys



@when('visit url "{url}"')
def step(context, url):
    context.browser.get(url)

@when('field with name "{selector}" is given "{value}"')
def step(context, selector, value):
    elem = context.browser.find_element_by_name(selector)
    elem.send_keys(value)
    elem.submit()
    time.sleep(5)

@when('field with id "{selector}" is given "{value}"')
def step(context, selector, value):
    elem = context.browser.find_element_by_id(selector)
    elem.send_keys(value)


@when('button clicked with id "{selector}"')
def step(context, selector):
    elem = context.browser.find_element_by_id(selector)
    elem.click()
    time.sleep(5)

@when('wait')
def step(context):
    time.sleep(10)


@when('button clicked with path "{selector}"')
def step(context, selector):
    elem = context.browser.find_element_by_xpath(selector)
    elem.click()
    time.sleep(5)

@then('title becomes "{title}"')
def step(context, title):
    assert context.browser.title == title

@when('mouse move to')
def step(context):
    time.sleep(15)
    action = ActionChains(context.browser)
    action.move_by_offset(500,50)
    action.context_click()
    action.send_keys("browserstack")
    action.send_keys(Keys.RETURN)
    action.perform()
    print("Function Done ")

@then(u'page contains "{body}"')
def step(context, body):
    assert body in context.browser.page_source
