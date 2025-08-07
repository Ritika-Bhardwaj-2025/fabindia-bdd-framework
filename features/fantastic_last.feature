Feature: Navigate Fantastic Finds and View Product Details

    @case4
    Scenario: User browses fantastic finds and opens a specific product
        Given the user is on the homepage for fantastic finds product
        When the user scrolls to the Fantastic Finds on the homepage
        When the user navigates through the carousel using the right arrow
        And the user selects the fourth product from the displayed list
        Then the product detail view opens with relevant information
