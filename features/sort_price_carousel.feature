Feature: Filter Products by Price and Explore Similar Items

    @case7
    Scenario: User filters products by price and views similar recommendations
        Given the user is on the homepage with carousel fully visible
        When the user initiates product discovery by clicking on a banner carousel
        When the product detail page is displayed clearly
        And the user applies a price-based filter to refine the product list
        And the product grid should update to reflect the selected price range
        When the user hovers over and click the second product from the filtered results
        And the size guide should be shown for the selected item
        Then the user scrolls down to the section showcasing similar products
