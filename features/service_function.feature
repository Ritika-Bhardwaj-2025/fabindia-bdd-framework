Feature: Verify Qutumb Service Functionality

    @case12
    Scenario: User interacts with Qutumb service and initiates contact
        Given the user is on the FabIndia and website loaded
        When the user hovers over the "Services" section
        And the user clicks on the "Qutumb" service option
        And the user scrolls to the contact section
        And the user clicks on the contact banner
        And the user scrolls to the form section
        And the user enters their full name
        And the user enters their phone number
        Then the user clicks on "Generate OTP"
