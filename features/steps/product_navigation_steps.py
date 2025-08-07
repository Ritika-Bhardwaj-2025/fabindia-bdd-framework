from behave import *
from pages.product_navigation_action import ProductNavigationAction
from utilities.configReader import ConfigReader

@given(u'the user is on the FabIndia homepage and banner loaded')
def step_impl(context):
    # raise NotImplementedError(u'STEP: Given the user is on the FabIndia homepage and banner loaded')
    context.case14 = ProductNavigationAction(context.driver,context.logger)
    config_obj = ConfigReader()
    context.driver.get(config_obj.get_website())

@when(u'the user clicks on a banner carousel')
def step_impl(context):
    # raise NotImplementedError(u'STEP: When the user clicks on a banner carousel')
    context.case14.click_banner_carousel_action()

@when(u'the user verifies the product page')
def step_impl(context):
    # raise NotImplementedError(u'STEP: When the user verifies the product page')
    context.case14.verify_product_page_action()

@when(u'the user hovers over and clicks on a product')
def step_impl(context):
    # raise NotImplementedError(u'STEP: When the user hovers over and clicks on a product')
    context.case14.hover_click_product_action()

@when(u'the user verifies the size guide')
def step_impl(context):
    # raise NotImplementedError(u'STEP: When the user verifies the size guide')
    context.case14.verify_size_guide_action()

@then(u'the user clicks on "Add to Cart" and verify')
def step_impl(context):
    # raise NotImplementedError(u'STEP: Then the user clicks on "Add to Cart" and verify')
    context.case14.click_add_to_cart()
