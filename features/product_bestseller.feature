Feature: Verify Product with Bestseller Filter

    @case15
    Scenario: User filters products by Bestseller and verifies a selected product
        Given the user is on the FabIndia homepage and homepage is loaded
        When the user clicks on a first banner carousel
        And the user verifies the product page heading
        And the user selects the "Bestseller" filter
        And the user verifies the filtered bestseller products
        And the user hovers over and clicks on the second product
        Then the user verifies the size guide
