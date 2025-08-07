from behave import *
from pages.carousel_action import ValidCarouselAction
from utilities.configReader import ConfigReader

@given(u'the user is on the homepage for carousel testing')
def step_impl(context):
    # raise NotImplementedError(u'STEP: Given the user is on the homepage for carousel testing')
    context.case1 = ValidCarouselAction(context.driver,context.logger)
    config_obj = ConfigReader()
    context.driver.get(config_obj.get_website())

@when(u'the user clicks on the banner carousel')
def step_impl(context):
    # raise NotImplementedError(u'STEP: When the user clicks on the banner carousel')
    context.case1.click_banner_carousel_action()

@when(u'the user is navigated to the product page')
def step_impl(context):
    # raise NotImplementedError(u'STEP: When the user is navigated to the product page')
    context.case1.verify_product_page_action()

@when(u'the user clicks on the color dropdown')
def step_impl(context):
    # raise NotImplementedError(u'STEP: When the user clicks on the color dropdown')
    context.case1.click_color_dropdown_action()

@when(u'the color dropdown should be displayed')
def step_impl(context):
    # raise NotImplementedError(u'STEP: When the color dropdown should be displayed')
    context.case1.verify_color_dropdown()

@when(u'the user scrolls and selects the pink color option')
def step_impl(context):
    # raise NotImplementedError(u'STEP: When the user scrolls and selects the pink color option')
    context.case1.scroll_click_pink_option()

@when(u'the pink color option should be selected')
def step_impl(context):
    # raise NotImplementedError(u'STEP: When the pink color option should be selected')
    context.case1.verify_pink_option_action()

@when(u'the user hovers and clicks on the product')
def step_impl(context):
    # raise NotImplementedError(u'STEP: When the user hovers and clicks on the product')
    context.case1.hover_click_product_action()

@when(u'the size guide should be visible')
def step_impl(context):
    # raise NotImplementedError(u'STEP: Then the size guide should be visible')
    context.case1.verify_size_guide_action()

@then(u'the user clicks on "Add to Cart"')
def step_impl(context):
    # raise NotImplementedError(u'STEP: When the user clicks on "Add to Cart"')
    context.case1.click_add_to_cart()
