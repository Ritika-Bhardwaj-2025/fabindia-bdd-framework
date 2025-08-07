Feature: Product Selection and Add to Cart Flow

    @case1
    Scenario: User selects a product color and adds it to cart
        Given the user is on the homepage for carousel testing
        When the user clicks on the banner carousel
        And the user is navigated to the product page
        And the user clicks on the color dropdown
        And the color dropdown should be displayed
        When the user scrolls and selects the pink color option
        And the pink color option should be selected
        When the user hovers and clicks on the product
        And the size guide should be visible
        Then the user clicks on "Add to Cart"
