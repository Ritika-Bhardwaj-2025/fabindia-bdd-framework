Feature: Verify Store Navigation Functionality

    @case13
    Scenario: User searches for a store using the store icon
        Given the user is on the FabIndia homepage and store icon is fully loaded
        When the user clicks on the store icon
        And the user initiates a store search
        And the user enters the store name or location in the search bar
        Then the user verifies the list of available stores
