from behave import *
from pages.sort_filter_carousel_action import SortValidCarousel
from utilities.configReader import ConfigReader

@given(u'the user is on the homepage with carousel visible')
def step_impl(context):
    # raise NotImplementedError(u'STEP: Given the user is on the homepage with carousel visible')
    context.case2 = SortValidCarousel(context.driver, context.logger)
    config_obj = ConfigReader()
    context.driver.get(config_obj.get_website())

@when(u'the user clicks on a banner carousel to begin product exploration')
def step_impl(context):
    # raise NotImplementedError(u'STEP: When the user clicks on a banner carousel to begin product exploration')
    context.case2.click_banner_carousel_action()

@when(u'the product detail page is displayed')
def step_impl(context):
    # raise NotImplementedError(u'STEP: When the product detail page is displayed')
    context.case2.verify_product_page_action()

@when(u'the user applies the "Bestseller" filter from the available options')
def step_impl(context):
    # raise NotImplementedError(u'STEP: When the user applies the "Bestseller" filter from the available options')
    context.case2.select_filter_bestseller_action()

@when(u'the product list should update to show bestseller items')
def step_impl(context):
    # raise NotImplementedError(u'STEP: When the product list should update to show bestseller items')
    context.case2.verify_bestseller_click_action()

@when(u'the user hovers over and selects the second product from the filtered results')
def step_impl(context):
    # raise NotImplementedError(u'STEP: When the user hovers over and selects the second product from the filtered results')
    context.case2.hover_click_second_product()

@when(u'the size guide should be shown for the selected product')
def step_impl(context):
    # raise NotImplementedError(u'STEP: When the size guide should be shown for the selected product')
    context.case2.verify_size_guide_action()

@when(u'the user scrolls down to the "Similar Products" section')
def step_impl(context):
    # raise NotImplementedError(u'STEP: When the user scrolls down to the "Similar Products" section')
    context.case2.scroll_till_similar_product()

@when(u'the user clicks on the first item in the similar products list')
def step_impl(context):
    # raise NotImplementedError(u'STEP: When the user clicks on the first item in the similar products list')
    context.case2.click_first_similar_product()

@then(u'the detail page for the selected similar product should be displayed')
def step_impl(context):
    # raise NotImplementedError(u'STEP: Then the detail page for the selected similar product should be displayed')
    context.case2.verify_similar_product_page()