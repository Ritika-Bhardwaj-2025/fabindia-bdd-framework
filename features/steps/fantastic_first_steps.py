from behave import *
from pages.fantastic_first_product_action import FantasticFirstProductAction
from utilities.configReader import ConfigReader

@given(u'the user is on the homepage for fantastic finds first product')
def step_impl(context):
    # raise NotImplementedError(u'STEP: Given the user is on the homepage for fantastic finds first product')
    context.case3 = FantasticFirstProductAction(context.driver, context.logger)
    config_obj = ConfigReader()
    context.driver.get(config_obj.get_website())

@when(u'the user scrolls to the Fantastic Finds section on the homepage')
def step_impl(context):
    # raise NotImplementedError(u'STEP: When the user scrolls to the Fantastic Finds section on the homepage')
    context.case3.scroll_fantastic_finds()

@when(u'the user selects the first product from the showcased items')
def step_impl(context):
    # raise NotImplementedError(u'STEP: When the user selects the first product from the showcased items')
    context.case3.click_first_product()

@when(u'the product detail page should be displayed')
def step_impl(context):
    # raise NotImplementedError(u'STEP: When the product detail page should be displayed')
    context.case3.verify_product_page()

@when(u'the user hovers over the third product and click the product')
def step_impl(context):
    # raise NotImplementedError(u'STEP: When the user hovers over the third product and click the product')
    context.case3.hover_click_third_product()

@then(u'the size guide should appear for the selected product')
def step_impl(context):
    # raise NotImplementedError(u'STEP: Then the size guide should appear for the selected product')
    context.case3.verify_select_size_action()