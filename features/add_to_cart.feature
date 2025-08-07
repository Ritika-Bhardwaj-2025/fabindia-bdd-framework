Feature: Product Purchase Flow from Banner Carousel

    @case9
    Scenario: User adds a product to wishlist from banner carousel and is redirected to login
        Given the user is on the homepage for add to wishlist feature
        When the user clicks on the first banner carousel
        And the user is navigated to the second product page
        And the user hovers and clicks on the second product
        And the user clicks on "Add to Wishlist" icon
        Then the user should be redirected to the login page
