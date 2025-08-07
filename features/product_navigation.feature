Feature: Verify Product Navigation Functionality

    @case14
    Scenario: User navigates through a product and adds it to the cart
        Given the user is on the FabIndia homepage and banner loaded
        When the user clicks on a banner carousel
        And the user verifies the product page
        And the user hovers over and clicks on a product
        And the user verifies the size guide
        Then the user clicks on "Add to Cart" and verify
