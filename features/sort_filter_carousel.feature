Feature: Filter and Explore Similar Products

    @case2
    Scenario: User filters products, views details, and explores similar items
        Given the user is on the homepage with carousel visible
        When the user clicks on a banner carousel to begin product exploration
        When the product detail page is displayed
        And the user applies the "Bestseller" filter from the available options
        And the product list should update to show bestseller items
        When the user hovers over and selects the second product from the filtered results
        And the size guide should be shown for the selected product
        When the user scrolls down to the "Similar Products" section
        And the user clicks on the first item in the similar products list
        Then the detail page for the selected similar product should be displayed
