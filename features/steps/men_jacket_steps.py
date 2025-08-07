from behave import *
from pages.men_jacket_action import MenJacketAction
from utilities.configReader import ConfigReader

@given(u'the user is on the FabIndia homepage')
def step_impl(context):
    context.case11 = MenJacketAction(context.driver, context.logger)
    config_obj = ConfigReader()
    context.driver.get(config_obj.get_website())

@when(u'the user hovers over the "Men" category')
def step_impl(context):
    context.case11.hover_on_men()

@when(u'the user clicks on the "Jacket" option')
def step_impl(context):
    context.case11.click_jacket_option()

@when(u'the user applies the "Size" filter')
def step_impl(context):
    context.case11.click_button_filter_size()

@when(u'the user selects "L" size')
def step_impl(context):
    context.case11.click_l_size_option()

@then(u'the user clicks on the first product in the filtered list')
def step_impl(context):
    context.case11.click_first_product()
