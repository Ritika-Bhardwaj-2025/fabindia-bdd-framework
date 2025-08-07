from behave import *
from pages.fantastic_last_product_action import FantasticLastProductAction
from utilities.configReader import ConfigReader

@given(u'the user is on the homepage for fantastic finds product')
def step_impl(context):
    # raise NotImplementedError(u'STEP: Given the user is on the homepage for fantastic finds product')
    context.case4 = FantasticLastProductAction(context.driver, context.logger)
    config_obj = ConfigReader()
    context.driver.get(config_obj.get_website())

@when(u'the user scrolls to the Fantastic Finds on the homepage')
def step_impl(context):
    # raise NotImplementedError(u'STEP: When the user scrolls to the Fantastic Finds on the homepage')
    context.case4.scroll_fantastic_finds()

@when(u'the user navigates through the carousel using the right arrow')
def step_impl(context):
    # raise NotImplementedError(u'STEP: When the user navigates through the carousel using the right arrow')
    context.case4.click_right_arrow()

@when(u'the user selects the fourth product from the displayed list')
def step_impl(context):
    # raise NotImplementedError(u'STEP: When the user selects the fourth product from the displayed list')
    context.case4.click_fourth_product()

@then(u'the product detail view opens with relevant information')
def step_impl(context):
    # raise NotImplementedError(u'STEP: Then the product detail view opens with relevant information')
    context.case4.verify_product_page()