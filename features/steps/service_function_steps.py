from behave import *
from pages.service_function_action import ServiceFunctionAction
from utilities.configReader import ConfigReader

@given(u'the user is on the FabIndia and website loaded')
def step_impl(context):
    # raise NotImplementedError(u'STEP: Given the user is on the FabIndia and website loaded')
    context.case12 = ServiceFunctionAction(context.driver, context.logger)
    config_obj = ConfigReader()
    context.driver.get(config_obj.get_website())

@when(u'the user hovers over the "Services" section')
def step_impl(context):
    # raise NotImplementedError(u'STEP: When the user hovers over the "Services" section')
    context.case12.hover_on_service()

@when(u'the user clicks on the "Qutumb" service option')
def step_impl(context):
    # raise NotImplementedError(u'STEP: When the user clicks on the "Qutumb" service option')
    context.case12.click_qutumb_service_option()

@when(u'the user scrolls to the contact section')
def step_impl(context):
    # raise NotImplementedError(u'STEP: When the user scrolls to the contact section')
    context.case12.scroll_to_contact_section()

@when(u'the user clicks on the contact banner')
def step_impl(context):
    # raise NotImplementedError(u'STEP: When the user clicks on the contact banner')
    context.case12.click_contact_banner()

@when(u'the user scrolls to the form section')
def step_impl(context):
    # raise NotImplementedError(u'STEP: When the user scrolls to the form section')
    context.case12.scroll_to_form_section()

@when(u'the user enters their full name')
def step_impl(context):
    # raise NotImplementedError(u'STEP: When the user enters their full name')
    context.case12.enter_full_name()

@when(u'the user enters their phone number')
def step_impl(context):
    # raise NotImplementedError(u'STEP: When the user enters their phone number')
    context.case12.enter_phone_number()

@then(u'the user clicks on "Generate OTP"')
def step_impl(context):
    # raise NotImplementedError(u'STEP: When the user clicks on "Generate OTP"')
    context.case12.click_generate_otp()
