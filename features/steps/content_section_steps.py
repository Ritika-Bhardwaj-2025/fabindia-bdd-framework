from behave import *
from pages.content_section_action import ContentSectionAction
from utilities.configReader import ConfigReader

@given(u'the user is on the homepage for content scrolling')
def step_impl(context):
    # raise NotImplementedError(u'STEP: Given the user is on the homepage for content scrolling')
    context.case10 = ContentSectionAction(context.driver, context.logger)
    config_obj = ConfigReader()
    context.driver.get(config_obj.get_website())

@when(u'the user scrolls down to the featured content area')
def step_impl(context):
    # raise NotImplementedError(u'STEP: When the user scrolls down to the featured content area')
    context.case10.scroll_till_section()

@when(u'the user hovers over the interactive content section')
def step_impl(context):
    # raise NotImplementedError(u'STEP: When the user hovers over the interactive content section')
    context.case10.hover_content_section()

@then(u'the user continues scrolling to the women\'s collection and verify it')
def step_impl(context):
    # raise NotImplementedError(u'STEP: Then the user continues scrolling to the women\'s collection and verify it')
    context.case10.scroll_women_collection()