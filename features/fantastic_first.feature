Feature: Discover and Interact with Fantastic Finds

    @case3
    Scenario: User explores fantastic finds and interacts with product details
        Given the user is on the homepage for fantastic finds first product
        When the user scrolls to the Fantastic Finds section on the homepage
        When the user selects the first product from the showcased items
        And the product detail page should be displayed
        When the user hovers over the third product and click the product
        Then the size guide should appear for the selected product
