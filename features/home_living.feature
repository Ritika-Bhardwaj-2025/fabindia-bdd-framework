Feature: Verify Product from Home & Living Section

    @case16
    Scenario: User selects and adds a multicolor lamp or lantern to the cart
        Given the user is on the FabIndia homepage and nav bar is loaded
        When the user hovers over the "Home & Living" section
        And the user clicks on "Lamps & Lanterns"
        And the user opens the filter dropdown
        And the user selects the "Multicolor" option
        And the user clicks on the first product in the filtered list
        Then the user clicks on "Add to Cart" and verify button
