from behave import *
from pages.product_bestseller_action import ProductBestsellerAction
from utilities.configReader import ConfigReader

@given(u'the user is on the FabIndia homepage and homepage is loaded')
def step_impl(context):
    # raise NotImplementedError(u'STEP: Given the user is on the FabIndia homepage and homepage is loaded')
    context.case15 = ProductBestsellerAction(context.driver, context.logger)
    config_obj = ConfigReader()
    context.driver.get(config_obj.get_website())

@when(u'the user clicks on a first banner carousel')
def step_impl(context):
    # raise NotImplementedError(u'STEP: When the user clicks on a first banner carousel')
    context.case15.click_banner_carousel_action()

@when(u'the user verifies the product page heading')
def step_impl(context):
    # raise NotImplementedError(u'STEP: When the user verifies the product page heading')
    context.case15.verify_product_page_action()

@when(u'the user selects the "Bestseller" filter')
def step_impl(context):
    # raise NotImplementedError(u'STEP: When the user selects the "Bestseller" filter')
    context.case15.select_filter_bestseller_action()

@when(u'the user verifies the filtered bestseller products')
def step_impl(context):
    # raise NotImplementedError(u'STEP: When the user verifies the filtered bestseller products')
    context.case15.verify_bestseller_click_action()

@when(u'the user hovers over and clicks on the second product')
def step_impl(context):
    # raise NotImplementedError(u'STEP: When the user hovers over and clicks on the second product')
    context.case15.hover_click_second_product()

@then(u'the user verifies the size guide')
def step_impl(context):
    # raise NotImplementedError(u'STEP: Then the user verifies the size guide')
    context.case15.verify_size_guide_action()
