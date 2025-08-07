from behave import *
from pages.sort_price_carousel_action import SortPriceCarouselAction
from utilities.configReader import ConfigReader

@given(u'the user is on the homepage with carousel fully visible')
def step_impl(context):
    # raise NotImplementedError(u'STEP: Given the user is on the homepage with carousel fully visible')
    context.case7 = SortPriceCarouselAction(context.driver,context.logger)
    config_obj = ConfigReader()
    context.driver.get(config_obj.get_website())

@when(u'the user initiates product discovery by clicking on a banner carousel')
def step_impl(context):
    # raise NotImplementedError(u'STEP: When the user initiates product discovery by clicking on a banner carousel')
    context.case7.click_banner_carousel_action()

@when(u'the product detail page is displayed clearly')
def step_impl(context):
    # raise NotImplementedError(u'STEP: When the product detail page is displayed clearly')
    context.case7.verify_product_page_action()

@when(u'the user applies a price-based filter to refine the product list')
def step_impl(context):
    # raise NotImplementedError(u'STEP: When the user applies a price-based filter to refine the product list')
    context.case7.select_filter_price_action()

@when(u'the product grid should update to reflect the selected price range')
def step_impl(context):
    # raise NotImplementedError(u'STEP: When the product grid should update to reflect the selected price range')
    context.case7.verify_price_click_action()

@when(u'the user hovers over and click the second product from the filtered results')
def step_impl(context):
    # raise NotImplementedError(u'STEP: When the user hovers over and click the second product from the filtered results')
    context.case7.hover_click_second_product()

@when(u'the size guide should be shown for the selected item')
def step_impl(context):
    # raise NotImplementedError(u'STEP: When the size guide should be shown for the selected item')
    context.case7.verify_size_guide_action()

@then(u'the user scrolls down to the section showcasing similar products')
def step_impl(context):
    # raise NotImplementedError(u'STEP: When the user scrolls down to the section showcasing similar products')
    context.case7.scroll_till_similar_product()
