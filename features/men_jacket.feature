Feature: Verify Men Jacket Product

    @case11
    Scenario: User filters and selects a men's jacket of size L
        Given the user is on the FabIndia homepage
        When the user hovers over the "Men" category
        And the user clicks on the "Jacket" option
        And the user applies the "Size" filter
        And the user selects "L" size
        Then the user clicks on the first product in the filtered list
