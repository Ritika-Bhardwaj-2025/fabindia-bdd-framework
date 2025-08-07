from behave import *
from pages.carousel_right_function_action import CarouselRightFunctionAction
from utilities.configReader import ConfigReader

@given(u'the user is viewing the homepage banner section')
def step_impl(context):
    # raise NotImplementedError(u'STEP: Given the user is viewing the homepage banner section')
    context.case5 = CarouselRightFunctionAction(context.driver, context.logger)
    config_obj = ConfigReader()
    context.driver.get(config_obj.get_website())

@when(u'the initial banner should be visible')
def step_impl(context):
    # raise NotImplementedError(u'STEP: Given the initial banner should be visible')
    context.logger.info("Verifying carousel right function")
    context.case5.verify_banner_loaded()

@when(u'the user taps the right navigation arrow once')
def step_impl(context):
    # raise NotImplementedError(u'STEP: When the user taps the right navigation arrow once')
    context.case5.click_right_arrow()

@when(u'the banner should update to the next item')
def step_impl(context):
    # raise NotImplementedError(u'STEP: When the banner should update to the next item')
    context.case5.verify_banner_loaded()

@when(u'the user taps the right navigation arrow again')
def step_impl(context):
    # raise NotImplementedError(u'STEP: When the user taps the right navigation arrow again')
    context.case5.click_right_arrow()

@when(u'the banner should refresh with a new image')
def step_impl(context):
    # raise NotImplementedError(u'STEP: When the banner should refresh with a new image')
    context.case5.verify_banner_loaded()

@when(u'the user continues by clicking the right arrow two more times')
def step_impl(context):
    # raise NotImplementedError(u'STEP: When the user continues by clicking the right arrow two more times')
    context.case5.click_right_arrow()

@when(u'the final banner in the sequence should be displayed')
def step_impl(context):
    # raise NotImplementedError(u'STEP: When the final banner in the sequence should be displayed')
    context.case5.click_right_arrow()

@then(u'the previous banner should reappear')
def step_impl(context):
    # raise NotImplementedError(u'STEP: Then the previous banner should reappear')
    context.case5.verify_banner_loaded()
    context.logger.info("Successfully verified carousel right function")