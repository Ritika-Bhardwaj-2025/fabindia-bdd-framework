from behave import *
from pages.store_finder_action import StoreFinderAction
from utilities.configReader import ConfigReader

@given(u'the user is on the FabIndia homepage and store icon is fully loaded')
def step_impl(context):
    # raise NotImplementedError(u'STEP: Given the user is on the FabIndia homepage and store icon is fully loaded')
    context.case13 = StoreFinderAction(context.driver, context.logger)
    config_obj = ConfigReader()
    context.driver.get(config_obj.get_website())

@when(u'the user clicks on the store icon')
def step_impl(context):
    # raise NotImplementedError(u'STEP: When the user clicks on the store icon')
    context.case13.click_on_store_icon()

@when(u'the user initiates a store search')
def step_impl(context):
    # raise NotImplementedError(u'STEP: When the user initiates a store search')
    context.case13.search_for_store()

@when(u'the user enters the store name or location in the search bar')
def step_impl(context):
    # raise NotImplementedError(u'STEP: When the user enters the store name or location in the search bar')
    context.case13.send_input_store_search_bar()

@then(u'the user verifies the list of available stores')
def step_impl(context):
    # raise NotImplementedError(u'STEP: Then the user verifies the list of available stores')
    context.case13.verify_stores()