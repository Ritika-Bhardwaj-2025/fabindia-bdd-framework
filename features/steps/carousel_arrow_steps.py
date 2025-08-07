from behave import *
from pages.carousel_arrow_function_actions import CarouselArrowFunctionAction
from utilities.configReader import ConfigReader

@given(u'the user is on the homepage for carousel arrow function')
def step_impl(context):
    # raise NotImplementedError(u'STEP: Given the user is on the homepage for carousel arrow function')
    context.case6 = CarouselArrowFunctionAction(context.driver,context.logger)
    config_obj = ConfigReader()
    context.driver.get(config_obj.get_website())

@when(u'the user clicks the right arrow on the banner carousel')
def step_impl(context):
    # raise NotImplementedError(u'STEP: When the user clicks the right arrow on the banner carousel')
    context.logger.info("Verifying carousel arrow function")
    context.case6.click_right_arrow()

@when(u'the user clicks the right arrow again')
def step_impl(context):
    # raise NotImplementedError(u'STEP: When the user clicks the right arrow again')
    context.case6.click_right_arrow()

@then(u'the new banner should be loaded')
def step_impl(context):
    # raise NotImplementedError(u'STEP: Then the new banner should be loaded')
    context.case6.verify_banner_loaded()

@when(u'the user clicks the left arrow on the banner carousel')
def step_impl(context):
    # raise NotImplementedError(u'STEP: When the user clicks the left arrow on the banner carousel')
    context.case6.click_left_arrow()

@then(u'the previous banner should be displayed')
def step_impl(context):
    # raise NotImplementedError(u'STEP: Then the previous banner should be displayed')
    context.case6.verify_banner_loaded()
    context.logger.info("Successfully verified carousel arrow function")