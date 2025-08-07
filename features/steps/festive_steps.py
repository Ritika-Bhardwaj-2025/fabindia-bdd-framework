from behave import *
from pages.festive_action import FestiveAction
from utilities.configReader import ConfigReader

@given(u'the user is on the homepage with banner carousel visible')
def step_impl(context):
    # raise NotImplementedError(u'STEP: Given the user is on the homepage with banner carousel visible')
    context.case8 = FestiveAction(context.driver, context.logger)
    config_obj = ConfigReader()
    context.driver.get(config_obj.get_website())

@when(u'the user advances the carousel by clicking the right arrow')
def step_impl(context):
    # raise NotImplementedError(u'STEP: When the user advances the carousel by clicking the right arrow')
    context.logger.info("Verifying festive collection url function")
    context.case8.click_right_arrow()

@when(u'the user click the right arrow twice')
def step_impl(context):
    # raise NotImplementedError(u'STEP: When the user click the right arrow twice')
    context.case8.click_right_arrow()

@when(u'the user selects the third banner from the carousel')
def step_impl(context):
    # raise NotImplementedError(u'STEP: When the user selects the third banner from the carousel')
    context.case8.click_third_banner()

@when(u'the corresponding product detail page should be displayed')
def step_impl(context):
    # raise NotImplementedError(u'STEP: When the corresponding product detail page should be displayed')
    context.case8.verify_product_page()

@then(u'the URL should reflect the correct product information')
def step_impl(context):
    # raise NotImplementedError(u'STEP: Then the URL should reflect the correct product information')
    context.case8.verify_url_page_action()