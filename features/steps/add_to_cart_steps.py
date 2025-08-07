from behave import *
from pages.add_to_wishlist_action import AddToWishlistAction
from utilities.configReader import ConfigReader

@given(u'the user is on the homepage for add to wishlist feature')
def step_impl(context):
    # raise NotImplementedError(u'STEP: Given the user is on the homepage for add to wishlist feature')
    context.case9 = AddToWishlistAction(context.driver, context.logger)
    config_obj = ConfigReader()
    context.driver.get(config_obj.get_website())

@when(u'the user clicks on the first banner carousel')
def step_impl(context):
    # raise NotImplementedError(u'STEP: When the user clicks on the first banner carousel')
    context.case9.click_banner_carousel_action()

@when(u'the user is navigated to the second product page')
def step_impl(context):
    # raise NotImplementedError(u'STEP: When the user is navigated to the second product page')
    context.case9.verify_product_page_action()

@when(u'the user hovers and clicks on the second product')
def step_impl(context):
    # raise NotImplementedError(u'STEP: When the user hovers and clicks on the second product')
    context.case9.hover_click_second_product()

@when(u'the user clicks on "Add to Wishlist" icon')
def step_impl(context):
    # raise NotImplementedError(u'STEP: When the user clicks on "Add to Wishlist" icon')
    context.case9.click_add_to_wishlist()

@then(u'the user should be redirected to the login page')
def step_impl(context):
    # raise NotImplementedError(u'STEP: Then the user should be redirected to the login page')
    context.case9.verify_login_page()