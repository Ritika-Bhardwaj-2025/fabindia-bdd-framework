Feature: Banner Navigation and Product Page Verification

    @case8
    Scenario: User navigates banners and verifies product and URL details
        Given the user is on the homepage with banner carousel visible
        When the user advances the carousel by clicking the right arrow
        And the user click the right arrow twice
        And the user selects the third banner from the carousel
        And the corresponding product detail page should be displayed
        Then the URL should reflect the correct product information
