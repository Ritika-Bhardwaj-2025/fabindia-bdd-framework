from behave import *
from pages.home_living_action import HomeLivingActions
from utilities.configReader import ConfigReader

@given(u'the user is on the FabIndia homepage and nav bar is loaded')
def step_impl(context):
    # raise NotImplementedError(u'STEP: Given the user is on the FabIndia homepage and nav bar is loaded')
    context.case16 = HomeLivingActions(context.driver,context.logger)
    config_obj = ConfigReader()
    context.driver.get(config_obj.get_website())

@when(u'the user hovers over the "Home & Living" section')
def step_impl(context):
    # raise NotImplementedError(u'STEP: When the user hovers over the "Home & Living" section')
    context.case16.hover_home_living()

@when(u'the user clicks on "Lamps & Lanterns"')
def step_impl(context):
    # raise NotImplementedError(u'STEP: When the user clicks on "Lamps & Lanterns"')
    context.case16.click_lamps_lanterns()

@when(u'the user opens the filter dropdown')
def step_impl(context):
    # raise NotImplementedError(u'STEP: When the user opens the filter dropdown')
    context.case16.click_dropdown()

@when(u'the user selects the "Multicolor" option')
def step_impl(context):
    # raise NotImplementedError(u'STEP: When the user selects the "Multicolor" option')
    context.case16.select_multicolor_option()

@when(u'the user clicks on the first product in the filtered list')
def step_impl(context):
    # raise NotImplementedError(u'STEP: When the user clicks on the first product in the filtered list')
    context.case16.click_first_product()

@then(u'the user clicks on "Add to Cart" and verify button')
def step_impl(context):
    # raise NotImplementedError(u'STEP: Then the user clicks on "Add to Cart" and verify button')
    context.case16.click_add_to_cart()